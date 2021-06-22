#include "hough.h"

void Hough_T::get_HoughCircle(KImageGray &imgOut, int min_radian, int max_radian)
{
    min_r = min_radian;
    max_r = max_radian;
    roi_x1 = 270;

    // votes 이미지 개수 width, height만큼 0으로 초기화
    vector<double> rad_sc(max_radian + 2);
    vector<vector<double>> row_sc(width, rad_sc);
    for(int i = 0; i <height; i++)
        votes.push_back(row_sc);

    // cannyedge에서 실행하여 발견한 edge pixel을 모두 훝어보며
    for(int e = 0; e < (int)TrueEdge.size(); e++){
        pix_Edge oEdge = TrueEdge[e];
        if(oEdge.u < roi_x1 ) continue; // roi 설정

        // 찾으려는 반지름 범위 내에서
        for(int radius = min_r; radius <= (int)max_r; radius++)
        {
            double dAngle = _RADIAN(oEdge.wAng); // cannyedge에서 실행하여 얻은 각도를 radian으로
            // Edge의 방향과 찾으려는 원 반지름, edge pixel을 이용하여 원의 중심을 찾는다
            int center_x = (int)(oEdge.u - radius*cos(dAngle));
            int center_y = (int)(oEdge.v - radius*sin(dAngle));

            // 찾은 원의 중심에서 5x5 크기에 중심점 점수를 준다
            for(int i = -5; i < 6; i++)
                for(int j = -5; j < 6; j++){
                    // 이미지 크기에 벗어나면 continue
                    if(center_x+j <=0 || center_y+i <= 0 || center_x+j >= width || center_y+i >= height)
                        continue;
                    // 원의 반지름 -1, +1 에서도 점수 취득
                    votes[center_y+i][center_x+j][radius-1] +=0.5;
                    votes[center_y+i][center_x+j][radius] +=0.5;
                    votes[center_y+i][center_x+j][radius+1] +=0.5;
                }
            votes[center_y][center_x][radius] +=0.5; // 중심점에 부가 점수
        }
    }

    // votes가 가장 높은 반지름 max_rad을 저장
    double max_rad;
    double max_vote = 0;
    for(int i = 0; i<height; i++)
        for(int j = 0; j < width; j++)
            for(int k = min_r; k <= (int)max_r; k++)
                if(votes[i][j][k] > max_vote) {
                    max_vote = votes[i][j][k];
                    max_rad = k;
                }
    qDebug("High Scored Radius %d",(int)max_rad);

    // 고득점을 받은 픽셀들을 maxs_yx에 저장
    vector<pair<int,int>> maxs_yx;
    int cnt = 1;
    for(int i = 0; i<height; i++)
        for(int j = 0; j < width; j++){
            for(int k = min_r; k <= (int)max_r; k++)
                if(max_vote == votes[i][j][k]) {
                    maxs_yx.push_back({i,j});
                    qDebug("Center of %d th Circle: x, y = %d, %d", cnt++, j, i);
                }
        }

    for(int m = 0; m < (int)maxs_yx.size(); m++){
        int cx = maxs_yx[m].second;
        int cy = maxs_yx[m].first;

        // 찾은 중점에서 반지름만큼의 roi를 설정하고
        // 그 안에서 중심점과의 거리가 max_rad인만큼인 픽셀들을 흰색으로 설정
        for(int i = cy-1-max_rad; i<= cy+1+max_rad; i++)
            for(int j = cx-1-max_rad; j <= cx+1+max_rad; j++){
                double d = sqrt(pow(cx - j, 2) + pow(cy - i, 2));
                if(max_rad-0.5 <= d && d <= max_rad+0.5)
                    imgOut[i][j] = 255;
            }
    }
}

void Hough_T::get_shape_table(vector<KPOINT> pixels)
{
    // 받은 픽셀의 중심점(평균)을 구합니다
    double c_x = 0, c_y = 0;
    float n = pixels.size();
    for(int i = 0; i < n; i++){
        c_x += pixels[i].nX;
        c_y += pixels[i].nY;
    }
    c_x /= n; c_y/= n;
    qDebug("table center: %f, %f", c_x, c_y);

    // shape_table nDir만큼(0~3) 담을 수 있도록 4개 초기화
    vector<pair<double, double>> init;
    for(int i = 0; i <4; i ++)
        shape_table.push_back(init);

    // 중심점으로부터의 거리 및 각도를 구해 픽셀의 방향 인덱스 구조체에 넣습니다
    for(int j = 1, jj = n-2; jj; j++, jj--){
        float dTmp = atan2((float)(pixels[j+1].nY - pixels[j-1].nY), (float)(pixels[j+1].nX - pixels[j-1].nX)) * 180 / _PI;
        dTmp += 90;
        int nDir = ((((int)(dTmp/22.5)+1) >> 1) & 0x00000003);
        double dDist = sqrt(_SQR(c_x - pixels[j].nX) + _SQR(c_y - pixels[j].nY));
        double dAng = atan2(pixels[j].nY - c_y, pixels[j].nX - c_x);
        shape_table[nDir].push_back({dDist, dAng});
    }
}

void Hough_T::find_shape(KImageGray &imgOut, int min_sc, int max_sc, int min_ang, int max_ang)
{
    // RoI 설정
    roi_x2 = 270;
    min_scale = min_sc;
    max_scale = max_sc;
    min_angle = min_ang;
    max_angle = max_ang;

    // g_votes 0으로 초기화
    vector<int> scale_vote(max_scale+2);
    vector<int> angle_vote(360);
    vector<pair<vector<int>, vector<int>>> row_sc(width, make_pair(scale_vote, angle_vote));
    for(int i = 0; i <height; i++)
        g_votes.push_back(row_sc);

    // 모든 엣지 픽셀을 훝어가며
    for(int e = 0; e < (int)TrueEdge.size(); e++){
        pix_Edge oEdge = TrueEdge[e];
        if(oEdge.u > roi_x2) continue; // RoI 범위가 아니면 continue;

        // Scale과 Angle을 바꿔가며
        for(int dScale = min_scale; dScale <= (int)max_scale; dScale++)
            for(int dAng = 270 ; dAng < 300; dAng++){
                double dTmp = oEdge.wAng - dAng;
                oEdge.wDir = ((((int)(dTmp/22.5)+1)>>1) & 0x00000003);

                // 같은 방향 wDir에 있는 픽셀을 shape_table을 참고하여 중심점을 잡고 점수를 매깁니다
                for(int i = 0, ii = shape_table[oEdge.wDir].size(); ii; i++, ii--){
                    int c_x = oEdge.u - shape_table[oEdge.wDir][i].first * dScale / 100.0 * cos(shape_table[oEdge.wDir][i].second + dAng);
                    int c_y = oEdge.v - shape_table[oEdge.wDir][i].first * dScale / 100.0 * sin(shape_table[oEdge.wDir][i].second + dAng);

                    g_votes[c_y][c_x].first[dScale] += 1; // scale 점수
                    g_votes[c_y][c_x].second[dAng] += 1; // angle 점수
                }
            }
    }

    // 가장 높은 점수를 받은 Angle을 구합니다
    double max_Ang;
    double max_vote = 0;
    for(int i = 0; i<height; i++)
        for(int j = 0; j < width; j++)
            for(int a = 0; a < 360; a++)
                if(g_votes[i][j].second[a] > max_vote) {
                    max_vote = g_votes[i][j].second[a];
                    max_Ang = a;
                }
    qDebug("High Scored Radius %d",(int)max_Ang);

    // 가장 높은 점수를 받은 Scale과 해당 픽셀의 위치를 구합니다
    double max_dist;
    max_vote = 0;
    int max_x = 0, max_y = 0;
    for(int i = 0; i<height; i++)
        for(int j = 0; j < width; j++)
            for(int a = min_scale; a < (int)max_scale; a++)
                if(g_votes[i][j].first[a] > max_vote) {
                    max_vote = g_votes[i][j].first[a];
                    max_dist = a; max_x = j; max_y = i;
                }


    qDebug("High Scored Distance %d",(int)max_dist);
    qDebug("High Scored Point (%d, %d)",max_x, max_y);
    imgOut[max_y][max_x] = 255; // 높은 점수를 받은 중심점을 흰색으로 표시합니다

    // shape_table의 angle, distance에서 점수 높은 scale, angle을 고려하여 삼각함수를 이용해 plug를 검출합니다.
    for(int i = 0; i < (int)shape_table.size(); i++)
        for(int j = 0; j < (int)shape_table[i].size(); j++){
            int y = max_y + shape_table[i][j].first * sin(shape_table[i][j].second + max_Ang) * max_dist / 100.0;
            int x = max_x + shape_table[i][j].first * cos(shape_table[i][j].second + max_Ang) * max_dist / 100.0;
            imgOut[y][x] = 255;
        }
}
