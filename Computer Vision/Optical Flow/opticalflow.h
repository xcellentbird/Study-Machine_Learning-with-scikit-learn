#ifndef OPTICALFLOW_H
#define OPTICALFLOW_H
#include "kfc.h"
#include <vector>
using namespace std;

class OpticalFlow
{
    int kernel_size;
    KMatrix Gkernel;
    vector<vector<pair<double, double>>> uv;
public:
    int KSize;
    int half;
    pair<double, double> UV(int y, int x){return uv[y][x];}
    OpticalFlow(double sigma = 1.0);
    KImageGray get_OFimg(KImageGray img1, KImageGray img2);

};


#endif // OPTICALFLOW_H
