#ifndef SEPIATONE_H
#define SEPIATONE_H
#include "kfc.h"
#include <vector>


using namespace std;

struct HSV //HSV 구조체
{
    double h;
    double s;
    double v;
};

class KImageHSV
{
    int width;
    int height;
    vector<vector<HSV>> hsv_pixel; //HSV를 담을 2차원 벡터
public:
    KImageHSV();
    ~KImageHSV();
    // icImg의 rgb를 이용하여 h,s,v 값 계산, hsv이미지 생성
    void COLORtoHSV(KImageColor icImg);
    // hsv이미지의 v값과 인수로 받은 hue, sat갑을 이용하여 rgb로 변환 후 igSepia에 반환
    void HSVtoSepiaColor(KImageColor& igSepia, double hue, double sat);
};



#endif // SEPIATONE_H
