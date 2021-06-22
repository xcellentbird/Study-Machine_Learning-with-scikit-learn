#include "otsulabeling.h"

void linked::new_link()
{
    vector<int> new_vec;
    label.push_back(new_vec);
}

bool linked::find(int n, int a)
{
    if((int)label.size()<=n) return false;
    else {
        for(int i=0; i<(int)label[n].size();i++)
            if(label[n][i]==a) return true;
    }
    return false;
}

void linked::get_min()
{
    for(int i=0; i<(int)label.size();i++){
        int min = 9999999;
        for(int j=0; j<(int)label[i].size();j++)
            if(label[i][j]<min) min=label[i][j];
        min_label[i] = min;
    }
}

otsu_lbl::otsu_lbl(KImageGray& gimg)
{
    otsu_img = gimg;
    width = (int)otsu_img.Col();
    height = (int)otsu_img.Row();
}

//히스토그램을 구한다
void otsu_lbl::get_hist()
{
    for(int k = 0; k <256; k++) n[k] = 0.0;
    for(int i=0; i<height;i++)
        for(int j =0; j < width;j++)
            for(int k = 0; k<256; k++)
                if(otsu_img[i][j] == k) {
                    n[k]++;
                    break;
                }
}

//Between-Class Variance
int otsu_lbl::otsu_threhold()
{
    double N = width * height;
    double P[256], q1[256], et1[256], et2[256], sigma[256];
    for(int i =0; i <256; i++){
        q1[i]=0.0; et1[i]=0.0; et2[i]=0.0; sigma[i]=0.0;
    }
    double max_sigma=0.0;
    int threshold;

    //0번째 초기화
    q1[0]=P[0]=n[0]/N;
    et1[0]=0;
    for (int i = 1 ; i < 256; i++){
        P[i] = n[i]/N;
        for(int j=0; j<i+1;j++) q1[i]+=P[j];
        // 왼쪽의 기댓값
        et1[i]=q1[i]!=0.0? (q1[i-1]*et1[i-1] + i*P[i])/q1[i] : 0.0;
    }
    for (int i = 0; i < 256; i++){
        // 오른쪽의 기댓값
        et2[i]=q1[i]!=1?(et1[255]-q1[i]*et1[i])/(1-q1[i]):0.0;
        //Variance
        sigma[i] = q1[i]*(q1[255]-q1[i])*pow(et1[i]-et2[i], 2.0);
        //분산이 최소값을 갖는 i 검색
        if(sigma[i] >= max_sigma) {
            max_sigma = sigma[i];
            threshold=i;
        }
    }
    return threshold;
}

// 임계값을 이용한 영상 이진화
void otsu_lbl::binary_transform(int threshold)
{
    for(int i=0; i < height; i++)
        for(int j = 0; j < width; j++)
        {
            if(otsu_img[i][j] > threshold) otsu_img[i][j] = 255;
            else otsu_img[i][j] = 0;
        }
    bin_img = otsu_img;
}

void otsu_lbl::labeling(KImageColor& cimg)
{
    // 8-neighbor dir
    int neib_x[8] = {-1,-1,0,1,1,1,0,-1};
    int neib_y[8] = {0,-1,-1,-1,0,1,1,1};

    // label 모두 0으로 초기화
    for (int i = 0; i < height; i++){
        vector<int> label_pixel2;
        for (int j = 0; j < width; j++)
            label_pixel2.push_back(0);
        label_pixel.push_back(label_pixel2);
    }

    linked linkset;
    int label = 1;

    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++)
        {
            if(otsu_img[i][j] == 255 && label_pixel[j][i] == 0) //흰색이면서 label이 0일 때
            {
                int cnt = 0;
                vector<int> ab;
                set<int> set;
                //왼쪽,왼쪽위,위,오른쪽위 검색
                for(int dir= 0; dir < 4; dir++)
                {
                    if(j+neib_x[dir] >= width || j+neib_x[dir] < 0 || i+neib_y[dir] >= height || i+neib_y[dir] < 0)
                        continue; // 영상크기에 벗어나면 continue;
                    int around = label_pixel[j+neib_x[dir]][i+neib_y[dir]];
                    if(around == 0) cnt++;
                    else { // 4방향 이웃에 Label이 있을 때
                        set.insert(around);
                        ab.push_back(around);
                    }
                }
                if(cnt == 4)label_pixel[j][i] = label++; //이웃 4칸 모두 0이면 새 Label설정
                else label_pixel[j][i] = *set.begin(); //4방향 이웃 Label중 가장 작은 Label로 현 픽셀 Label 설정
                if(ab.size()>=2){ // 4방향 이웃 중 Label이 있는 이웃이 2개일 때
                    bool new_link = true;
                    // 연결Label셋에서 해당 이웃Label이 하나만 있을 때 다른 한개 연결Label셋에 추가, 둘 다 모두 없을 경우 새 연결Label셋 생성
                    for(int z=0; z<(int)linkset.label.size();z++){
                        if(linkset.find(z, ab[0]) && linkset.find(z, ab[1])) {new_link=false;break;}
                        else if(linkset.find(z, ab[0])) {linkset.label[z].push_back(ab[1]); new_link=false;break;}
                        else if(linkset.find(z, ab[1])) {linkset.label[z].push_back(ab[0]); new_link=false;break;}
                    }
                    if(new_link){
                        linkset.new_link();
                        linkset.label[(int)linkset.label.size()-1].push_back(ab[0]);
                        linkset.label[(int)linkset.label.size()-1].push_back(ab[1]);
                    }
                }
            }
        }
    }

    //해당 픽셀의 label이 속한 이웃label에서 가장 작은 label을 해당 픽셀의 label 대체
    linkset.get_min();
    for(int i=0; i <height; i++)
        for(int j=0; j<width; j++)
            if(label_pixel[j][i] != 0){
                for(int k=0; k<(int)linkset.label.size();k++)
                    if(linkset.find(k, label_pixel[j][i]))
                        label_pixel[j][i] = linkset.min_label[k];
                otsu_img[i][j] -= label_pixel[j][i]*100;
            }

    //colorimage 색깔 결정
    for(int i=0; i <height; i++)
        for(int j=0; j<width; j++){
            if(label_pixel[j][i] != 0){
                switch(otsu_img[i][j] % 3){
                case 0:
                    cimg[i][j].r = otsu_img[i][j] + 10;
                    cimg[i][j].g = otsu_img[i][j] * 10;
                    cimg[i][j].b = otsu_img[i][j] * 100;
                    break;
                case 1:
                    cimg[i][j].r = otsu_img[i][j] * 100;
                    cimg[i][j].g = otsu_img[i][j] + 10;
                    cimg[i][j].b = otsu_img[i][j] * 10;
                    break;
                case 2:
                    cimg[i][j].r = otsu_img[i][j] * 10;
                    cimg[i][j].g = otsu_img[i][j] * 100;
                    cimg[i][j].b = otsu_img[i][j] + 10;
                    break;
                default:
                    cimg[i][j].r = otsu_img[i][j] + 10;
                    cimg[i][j].g = otsu_img[i][j] + 10;
                    cimg[i][j].b = otsu_img[i][j] + 10;
                    break;
                }
            }
            else { cimg[i][j].b=0;cimg[i][j].r=0;cimg[i][j].g=0; }
        }
}
