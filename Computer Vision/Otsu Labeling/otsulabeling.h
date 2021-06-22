#ifndef OTSULABELING_H
#define OTSULABELING_H
#include "kfc.h"
#include <map>
#include <set>
using namespace std;

//연결Label셋을 넣기 위한 구조체
struct linked
{
    map<int,int> min_label; //연결label셋 중 가장 작은 label들을 모아 보관
    vector<vector<int>> label;
    void new_link(); //새 연결label셋 생성
    bool find(int n, int a); //n번째 연결label셋 중에서 a label이 있는지 검색
    void get_min(); // min_label을 구하는 함수
};

class otsu_lbl
{
    double n[256]; //히스토그램
    int width;
    int height;
    vector<vector<int>> label_pixel; //픽셀의 라벨을 담기위한 2차원 vector
    KImageGray otsu_img;
    KImageGray bin_img;
public:
    otsu_lbl(KImageGray& gimg);
    KImageGray img() {return bin_img;}
    void get_hist(); //히스토그램을 구한다
    int otsu_threhold(); //Otsu 임계점을 구해 반환
    void binary_transform(int threshold); //영상 이진화
    void labeling(KImageColor& cimg); //Labeling
};

#endif // OTSULABELING_H
