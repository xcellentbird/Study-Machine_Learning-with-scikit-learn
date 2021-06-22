#ifndef FILTERING_H
#define FILTERING_H
#include "kfc.h"

class median
{
public:
    void get_st_pp(KImageGray& igImg, float th);
    void filtering(KImageGray& igImg, int f_size);
};

class gaussian
{
public:
    void get_gauss_nz(KImageGray& igImg, double Sigma);
    void filtering(KImageGray& igImg, double sigma, int f_size);
};

#endif // FILTERING_H
