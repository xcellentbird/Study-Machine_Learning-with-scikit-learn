#include "sepiaTone.h"

KImageHSV::KImageHSV() {};
KImageHSV::~KImageHSV()
{
    hsv_pixel.clear();
    vector<vector<HSV>>().swap(hsv_pixel);
}

void KImageHSV::COLORtoHSV(KImageColor icImg)
{
    //icImg의 크기값 저장
    width = icImg.Col();
    height = icImg.Row();
    qDebug("width: %d  height: %d",width,height);

    int max_rgb;
    int min_rgb;

    for (int j = 0; j < width; j++) {
        vector<HSV> hsv_pixel2; // 세로 한줄의 픽셀을 담을 열벡터 선언
        for (int i = 0; i < height; i++)
        {
            HSV hsv;

            // max(r,g,b)와 min(r,g,b) 구하는 과정
            if (icImg[i][j].r > icImg[i][j].g) {
                max_rgb = icImg[i][j].r;
                min_rgb = icImg[i][j].g;
                if (icImg[i][j].b > max_rgb) max_rgb = icImg[i][j].b;
                if (icImg[i][j].b < min_rgb) min_rgb = icImg[i][j].b; 
            } else {
                max_rgb = icImg[i][j].g;
                min_rgb = icImg[i][j].r;
                if (icImg[i][j].b > max_rgb) max_rgb = icImg[i][j].b;
                if (icImg[i][j].b < min_rgb) min_rgb = icImg[i][j].b;
            }

            double diff = (double)(max_rgb - min_rgb);

            if(diff == 0) //max(r,g,b) - min(r,g,b) = 0 일 경우
            {
                hsv.h = 0;
                hsv.s = 0;
            }
            else
            {
                if(max_rgb == icImg[i][j].r) // max(r,g,b) = red
                    hsv.h = 60.0 * (double)(icImg[i][j].g - icImg[i][j].b) / diff;
                else if (max_rgb == icImg[i][j].g) // max(r,g,b) = green
                    hsv.h = 60.0 * (double)(icImg[i][j].b - icImg[i][j].r) / diff + 120.0;
                else // max(r,g,b) = blue
                    hsv.h = 60.0 * (double)(icImg[i][j].r - icImg[i][j].g) / diff + 240.0;
                hsv.h += (hsv.h < 0.0 ? 360.0 : 0.0);
                hsv.s = diff / (double)max_rgb;
            }
            hsv.v = (double)max_rgb;
            hsv_pixel2.push_back(hsv); // hsv픽셀을 열벡터에 넣는다.
        }
        hsv_pixel.push_back(hsv_pixel2); // 열벡터를 행벡터에 넣는다.
    }
}

void KImageHSV::HSVtoSepiaColor(KImageColor &igSepia, double hue, double sat)
{
    double h,s,v;
    for(int j = 0; j < width; j++)
        for(int i = 0; i < height; i++)
        {
            h = hue;
            s = sat;
            v = (double)hsv_pixel[j][i].v;

            int max_rgb = (int)v;
            int min_rgb = (s - 1.0 ) * max_rgb;

            h /= 60.0;
            int max_c = (int)h; // 0,5=red,  1,2=green,  3,4=blue
            double ph = h-max_c;
            min_rgb = (1.0-s)*max_rgb;

            switch(max_c)
            {
                case 0: igSepia[i][j].r=max_rgb; igSepia[i][j].g=max_rgb*(1.0-s*(1.0-ph)); igSepia[i][j].b=min_rgb; break;
                case 1: igSepia[i][j].r=max_rgb*(1.0-s*ph); igSepia[i][j].g=max_rgb; igSepia[i][j].b=min_rgb; break;
                case 2: igSepia[i][j].r=min_rgb; igSepia[i][j].g=max_rgb; igSepia[i][j].b=max_rgb*(1.0-s*(1.0-ph)); break;
                case 3: igSepia[i][j].r=min_rgb; igSepia[i][j].g=max_rgb*(1.0-s*ph); igSepia[i][j].b=max_rgb; break;
                case 4: igSepia[i][j].r=max_rgb*(1.0-s*(1.0-ph)); igSepia[i][j].g=min_rgb; igSepia[i][j].b=max_rgb; break;
                case 5: igSepia[i][j].r=max_rgb; igSepia[i][j].g=min_rgb; igSepia[i][j].b=max_rgb*(1.0-s*ph); break;
            }
        }
}
