#include "histogram.h"

void dpH::get_dpHisto(int H_r[256], int H_g[256], int H_b[256])
{
    r[0] = H_r[0]; g[0] = H_g[0]; b[0] = H_b[0];
    for(int i=1; i<256; i++) {
        r[i] = H_r[i] + r[i-1];
        g[i] = H_g[i] + g[i-1];
        b[i] = H_b[i] + b[i-1];
    }
}

void Histo::get_histo(KImageColor cImg)
{
    //히스토그램 0으로 초기화
    for(int c = 0; c <256; c++) {
        H_r[c] = 0; H_g[c] = 0; H_b[c] = 0;
    }
    for(int y=0; y<(int)cImg.Row(); y++)
        for(int x=0; x<(int)cImg.Col(); x++)
            for(int c=0; c<256; c++){
                if(c == cImg[y][x].r) H_r[c]++;
                if(c == cImg[y][x].g) H_g[c]++;
                if(c == cImg[y][x].b) H_b[c]++;
            }
}

void Histo::HEQ(KImageColor& cImg)
{
    dpH dp_H;
    get_histo(cImg);
    dp_H.get_dpHisto(H_r,H_g,H_b);

    for(int i=0; i<256; i++){
        dp_H.r[i] = dp_H.r[i]/(double)cImg.Size();
        dp_H.g[i] = dp_H.g[i]/(double)cImg.Size();
        dp_H.b[i] = dp_H.b[i]/(double)cImg.Size();
    }

    for(int y=0; y<(int)cImg.Row(); y++)
        for(int x=0; x<(int)cImg.Col(); x++){
            cImg[y][x].r = (unsigned char)(dp_H.r[cImg[y][x].r]*255.0);
            cImg[y][x].g = (unsigned char)(dp_H.g[cImg[y][x].g]*255.0);
            cImg[y][x].b = (unsigned char)(dp_H.b[cImg[y][x].b]*255.0);
        }
}

void Histo::histo_matching(KImageColor& inImg, KImageColor ref_Img)
{
    //누적 히스토그램 생성
    dpH dpH1; //input inmage의 누적 히스토그램
    dpH dpH2; //reference image의 누적 히스토그램
    get_histo(inImg);
    dpH1.get_dpHisto(H_r, H_g, H_b);
    get_histo(ref_Img);
    dpH2.get_dpHisto(H_r, H_g, H_b);

    // 0~1.0 사이 값을 갖도록, 크기로 나눠 비율값으로 재설정
    for(int i=0; i<256; i++){
        dpH1.r[i] /= dpH1.r[255];
        dpH1.g[i] /= dpH1.g[255];
        dpH1.b[i] /= dpH1.b[255];
        dpH2.r[i] /= dpH2.r[255];
        dpH2.g[i] /= dpH2.g[255];
        dpH2.b[i] /= dpH2.b[255];
    }

    // input image와 reference image의 히스토그램을 비교하여
    // 비율이 같거나 가장 비슷하게 매칭되는 색을 기억해놓는다
    int ad_r[256], ad_g[256], ad_b[256];
    for(int i=0; i<256; i++){
        double min_r = 9999999, min_g = 9999999, min_b = 9999999;
        for(int rf=0; rf<256; rf++){
            if(abs(dpH1.r[i] - dpH2.r[rf]) < min_r ) {
                min_r = abs(dpH1.r[i] - dpH2.r[rf]);
                ad_r[i] = rf;
            }
            if(abs(dpH1.g[i] - dpH2.g[rf]) < min_g ) {
                min_g = abs(dpH1.g[i] - dpH2.g[rf]);
                ad_g[i] = rf;
            }
            if(abs(dpH1.b[i] - dpH2.b[rf]) < min_b ) {
                min_b = abs(dpH1.b[i] - dpH2.b[rf]);
                ad_b[i] = rf;
            }
        }
    }

    // 기억해놓은 매칭된 색을 input image에 적용시킨다
    for(int y=0; y<(int)inImg.Row(); y++)
        for(int x=0; x<(int)inImg.Col(); x++) {
            inImg[y][x].r = ad_r[inImg[y][x].r];
            inImg[y][x].g = ad_g[inImg[y][x].g];
            inImg[y][x].b = ad_b[inImg[y][x].b];
        }
}
