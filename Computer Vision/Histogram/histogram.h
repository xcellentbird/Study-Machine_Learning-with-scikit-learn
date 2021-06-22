#ifndef HISTOGRAM_H
#define HISTOGRAM_H
#include "kfc.h"

using namespace std;

struct dpH
{
    double r[256];
    double g[256];
    double b[256];
    void get_dpHisto(int H_r[256], int H_g[256], int H_b[256]);
};

class Histo
{
    int H_r[256];
    int H_g[256];
    int H_b[256];

public:
    void get_histo(KImageColor cImg);
    void HEQ(KImageColor& cImg);
    void histo_matching(KImageColor& inImg, KImageColor ref_Img);
};

#endif // HISTOGRAM_H
