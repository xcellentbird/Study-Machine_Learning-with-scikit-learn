#ifndef HOUGH_H
#define HOUGH_H
#include "kfc.h"
#include "cannyedge.h"
#include <map>
using namespace std;

class Hough_T : public CannyEdge
{
    // General Hough
    unsigned int min_scale, max_scale; //찾으려는 모양의 scale 범위
    unsigned int min_angle, max_angle; // angle 범위
    vector<vector<pair<double, double>>> shape_table; // shape_table[dir_index][n][distance, Angle]
    vector<vector<pair<vector<int>, vector<int>>>> g_votes; // votes[y][x][ first = dist_score, second = angle_score ]


    // Circle Hough
    unsigned int min_r; // 찾으려는 원의 최소 반지름
    unsigned int max_r; // 최대 반지름
    vector<vector<vector<double>>> votes; // 찾은 원의 중심점들에 vote (3차원)

    // region of interest
    unsigned int roi_x1;
    unsigned int roi_x2;
    unsigned int roi_y1;
    unsigned int roi_y2;

public:
    void get_HoughCircle(KImageGray &imgOut, int min_radian, int max_radian);

    void get_shape_table(vector<KPOINT> pixels);
    void find_shape(KImageGray &imgOut, int min_sc, int max_sc, int min_ang, int max_ang);
};

#endif // HOUGH_H
