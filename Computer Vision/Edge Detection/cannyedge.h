#ifndef CANNYEDGE_H
#define CANNYEDGE_H
#include "kfc.h"
#include <cmath>
#include <vector>
using namespace std;

struct pix_Edge
{
    unsigned int u;
    unsigned int v;
    double wAng;
    int wDir;
};

class CannyEdge
{
    int nHalf;
    KMatrix mKernelX;
    KMatrix mKernelY;

public:
    int height;
    int width;
    vector<pix_Edge> TrueEdge;
    void get_FDG(double dSigma);
    void opCannyEdge(float dLow, float dHigh, double dSigma, KImageGray& igIn, KImageGray& igOut);
};


#endif // CANNYEDGE_H
