#include "opticalflow.h"
OpticalFlow::OpticalFlow(double sigma)
{
    // get Gaussian Kernel Weight
    if(sigma <= 0) sigma = 1.0;
    KGaussianMulti gaus;
    Gkernel = gaus.Kernel_2D(sigma);
    KSize = sqrt((int)Gkernel.Size());
    half = KSize / 2;
}

KImageGray OpticalFlow::get_OFimg(KImageGray img1, KImageGray img2)
{

    KImageGray outimg;
    if(img1.Col() != img2.Col() || img1.Row() != img2.Row()){
         outimg.Create(0,0);
         return outimg;
    }

    outimg = img2;
    int width = img1.Col();
    int height = img1.Row();

    // noize exception - gaussian smoothing
    img1 = img1.GaussianSmoothing(1.0);
    img2 = img2.GaussianSmoothing(1.0);

    // uv vector 초기화
    vector<pair<double, double>> row_u(width, {0, 0});
    for(int i = 0; i < height; i++)
        uv.push_back(row_u);

    for(int i = half +1; i < height - half - 1; i++)
        for(int j = half +1; j < width - half - 1; j++){

            KMatrix I_t(KSize * KSize,1);
            KMatrix I_xy(KSize * KSize, 2);
            KMatrix WI_xy = I_xy;

            // in Kernel
            int KIndex = 0;
            int notInK = 0;
            bool pixel_in = false;
            for(int ki = -half; ki <= half; ki++)
                for(int kj = -half; kj <= half; kj++){

                    // kernel안에 똑같은 밝기의 픽셀이 없으면 continue;
                    if(!pixel_in)
                        for(int ki2 = -half; ki2 <= half; ki2++){
                            for(int kj2 = -half; kj2 <= half; kj2++){
                                if (img2[i+ki][j+kj] == img1[i+ki2][j+kj2]){
                                    pixel_in = true; break;
                                }
                            }
                            if(pixel_in) break;
                        }
                    if(!pixel_in) {
                        notInK++;
                        continue;
                    }

                    I_t[KIndex][0] =  (img2[i+ki][j+kj] - img1[i+ki][j+kj]) * Gkernel[ki+half][kj+half]; // Wb
                    I_xy[KIndex][0] = img1[i+ki][j+1+kj] - img1[i+ki][j+kj]; // A
                    I_xy[KIndex][1] = img1[i+1+ki][j+kj] - img1[i+ki][j+kj];
                    WI_xy[KIndex][0] = I_xy[KIndex][0] * Gkernel[ki+half][kj+half]; // WA
                    WI_xy[KIndex][1] = I_xy[KIndex][1] * Gkernel[ki+half][kj+half];
                } // kernel out

            // get d(u, v) using psuedo inversion
            if(notInK == (int)Gkernel.Size()){
                uv[i][j].first = 0;
                uv[i][j].second = 0;
            } else {
                KMatrix ATWA = I_xy.Tr() * WI_xy;
                KMatrix inv_ATWA(2,2);
                double D = (ATWA[0][0]*ATWA[1][1] - ATWA[0][1]*ATWA[1][0]);
                //inv_ATWA = ATWA * D;
                if(D != 0.0){
                    inv_ATWA[0][0] = ATWA[1][1] / D;
                    inv_ATWA[0][1] = -ATWA[0][1] / D;
                    inv_ATWA[1][0] = -ATWA[1][0] / D;
                    inv_ATWA[1][1] = ATWA[0][0] / D;
                }
                KMatrix d = inv_ATWA * I_xy.Tr() * I_t;
                uv[i][j].first = d[0][0]; //x == u
                uv[i][j].second = d[1][0]; //y == v
            }
        }
    return outimg;
}
