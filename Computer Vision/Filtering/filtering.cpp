#include "filtering.h"
#include <vector>
#include <algorithm>
using namespace std;

// 솔트 페퍼 노이즈를 씌우는 함수입니다.
void median::get_st_pp(KImageGray &igImg, float th)
{
    KRandom seed(igImg.Size()); // 이미지 크기만큼 난수 생성

    // 임계점 최대값 최소값을 설정합니다.
    float t = th;
    if(th < 0) t = -th;
    else if (th > 1.0) t = 1.0;

    for (int i = 0; i < (int)igImg.Row(); i++){
        for(int j= 0; j < (int)igImg.Col(); j++){
            float rndm = seed.Generate(); // 난수를 불러옵니다
            if(rndm < t) igImg[i][j] = 0; // 난수가 t보다 작으면 0
            else if(rndm > 1 - t) igImg[i][j] = 255; // 난수가 t보다 크면 1
        }
    }
}

void median::filtering(KImageGray &igImg, int f_size)
{
    KImageGray tmp_img = igImg; // 계산을 위한 임시 이미지를 만듭니다.
    int haf = f_size/2;
    for(int y = haf; y < (int)igImg.Row() - haf; y++)
        for(int x = haf; x < (int)igImg.Col() - haf; x++){

                // filtering
                vector<int> filter; // 필터 내의 픽셀값을 담아놓기 위한 vector입니다.
                for(int yy = -haf; yy< haf+1; yy++)
                    for(int xx = -haf; xx< haf+1; xx++){
                        filter.push_back(igImg[y+yy][x+xx]);
                    }
                sort(filter.begin(), filter.end()); // 담긴 벡터를 정렬시킵니다
                tmp_img[y][x] = filter[haf]; // 중간값을 픽셀값으로 설정합니다.
        }
    igImg = tmp_img; // 필터링 씌워진 이미지를 결과 이미지에 씌웁니다.
}

void gaussian::get_gauss_nz(KImageGray &igImg, double Sigma)
{
    KGaussian gaus;
    gaus.Create(0, Sigma); // Sigma 표준편차를 가진 가우스 함수를 생성합니다
    gaus.OnRandom(igImg.Size()); // 이미지 크기만큼 가우스 함수 랜덤값을 생성합니다.

    for(int y = 0; y < (int)igImg.Row(); y++)
        for(int x = 0; x < (int)igImg.Col(); x++){

            double seed = gaus.Generate();
            if(igImg[y][x] + seed > 255 || igImg[y][x] + seed < 0) seed = 0;
            igImg[y][x] += seed; // 픽셀에 가우스 랜던 값을 더해줍니다
        }
}

void gaussian::filtering(KImageGray &igImg, double sigma, int f_size)
{
    KGaussianMulti gausm;
    // 표준편차가 sigma, f_size 커널 크기를 가진 가우시안 2차원 마스크를 생성합니다
    KMatrix mk = gausm.Kernel_2D(sigma, f_size);
    int haf = f_size/2;

    KImageGray tmp_img = igImg;
    for(int y = haf; y < (int)igImg.Row()-haf; y++)
        for(int x = haf; x < (int)igImg.Col()-haf; x++)
        {
            // filtering
            double f_mulsum = 0;
            for(int yy = -haf, ky = 0; yy < haf+1; ky++, yy++)
                for(int xx = -haf, kx = 0; xx < haf+1; kx++, xx++)
                {
                    f_mulsum += tmp_img[y+yy][x+xx] * mk[ky][kx];
                }
            igImg[y][x] = f_mulsum;
        }
}
