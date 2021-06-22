#include "cannyedge.h"

void CannyEdge::get_FDG(double dSigma)
{
    nHalf = ( 3.0*dSigma < 2.5 ? 2:(int)(3.0*dSigma+0.5) );
    int nMaskLength = nHalf*2 +1;
    qDebug("Kernel Size: %d",nMaskLength);

    mKernelX.Create(nMaskLength, nMaskLength);
    mKernelY.Create(nMaskLength, nMaskLength);

    // 분산값을 이용하여 FDG 마스크를 계산해냅니다
    int i,j,ii,jj;
    double dTmp, dScale=0.0, dSigma2 = 2.0*_SQR(dSigma);
    for(i=-nHalf,ii=0; i<=nHalf; i++,ii++) {
        dTmp = -i*exp(-(i*i)/2./dSigma/dSigma);
        for(j=-nHalf,jj=0; j<=nHalf; j++,jj++) {
            mKernelY[ii][jj] = dTmp*exp(-(j*j)/dSigma2);
            mKernelX[jj][ii] = mKernelY[ii][jj];
            dScale += (i<0 ? mKernelY[ii][jj] : 0.0);
        }
    }

    for(i=0; i<nMaskLength; i++)
        for(j=0; j<nMaskLength; j++)
        {
            mKernelY[i][j] /= -dScale;
            mKernelX[i][j] /= -dScale;
        }
}

void CannyEdge::opCannyEdge(float dLow, float dHigh, double dSigma, KImageGray& igIn, KImageGray& igOut)
{
    // 초기화
    height = igIn.Row();
    width = igIn.Col();
    get_FDG(dSigma);
    igOut.Create(height, width);

    KImageDouble idMag(height, width);
    KImageDouble iwAng(height, width);
    KImageWord igDir(height, width);
    KImageDouble idBuf(height, width);

    // Gradient
    double dTmp;
    for(int i=nHalf; i< height-nHalf; i++){
        for(int j=nHalf; j< width-nHalf; j++){
            double dGradX = 0.0 ,dGradY = 0.0;

            for(int r=-nHalf,rr=0; r<=nHalf; r++,rr++)
                for(int c=-nHalf,cc=0; c<=nHalf; c++,cc++){
                    // FDG 마스크를 이용하여 X, Y방향 모서리값을 구합니다.
                    dGradX += igIn[i+r][j+c] * mKernelX[rr][cc];
                    dGradY += igIn[i+r][j+c] * mKernelY[rr][cc];
                }

            // 모서리값 크기 계산
            idMag[i][j] = _ABS(dGradX) + _ABS(dGradY);
            // 최소임계값 이상의 모서리값만의 방향(4 * 2 = 총 8방향)을 계산
            if(idMag[i][j] > dLow){
                dTmp = atan2((double)dGradY,(double)dGradX) * 180  / _PI;
                iwAng[i][j] = dTmp; //(unsigned short)(dTmp+0.5); //0~360
                igDir[i][j] = (unsigned char)((((int)(dTmp/22.5)+1)>>1) & 0x00000003); //0~3
            }
            else{
                // 최소임계값 넘지 않은 픽셀을 모두 0(검정)으로
                idMag[i][j] = 0.0;
            }
        }
    }

    // Non-Maxima suppression
    int nShiftX[4] = {1,1,0,-1};
    int nShiftY[4] = {0,1,1,1};
    pix_Edge oEdgeMag;

    for(int i=nHalf+1; i<height-nHalf-1; i++){
        for(int j=nHalf+1; j<width-nHalf-1; j++)
        {
            // 계산 수를 최소화하기 위해 모서리 크기가 0인 픽셀 계산 생략
            if(idMag[i][j] == 0.0)
                continue;
            if(idMag[i][j] > idMag[i+nShiftY[igDir[i][j] ]][j+nShiftX[igDir[i][j] ]] &&
                idMag[i][j] > idMag[i-nShiftY[igDir[i][j] ]][j-nShiftX[igDir[i][j] ]])
            {
                // 최대임계값보다 높은 모서리값은 모두 모서리로 확정 및 픽셀을 흰색으로
                if(idMag[i][j] > dHigh){
                    oEdgeMag.u = (unsigned short)j;
                    oEdgeMag.v = (unsigned short)i;
                    oEdgeMag.wAng = iwAng[i][j];
                    igOut[i][j] = 255;
                    TrueEdge.push_back(oEdgeMag);
                }
                idBuf[i][j] = idMag[i][j];
            }
        }
    }
    //hysteresis thresholding
    int iy,jx;
    for(int k = 0; k < (int)TrueEdge.size(); k++){
        jx = TrueEdge[k].u;
        iy = TrueEdge[k].v;
        // 확정된 모서리 주변을 살피며
        for(int i=-1; i<2; i++)
            for(int j=-1; j<2; j++){
                // 모서리값 크기가 0이 아닌 픽셀들을 모서리로 확정시킨다
                if(idBuf[iy+i][jx+j] && idBuf[iy+i][jx+j]<=dHigh)
                {
                    pix_Edge tp;
                    tp.u = (unsigned short)(jx+j);
                    tp.v = (unsigned short)(iy+i);
                    tp.wAng = iwAng[iy+i][jx+j];
                    //qDebug("Edge!! : (%d, %d)",jx+j,iy+i);
                    igOut[iy+i][jx+j] = 255;
                    TrueEdge.push_back(tp);
                    idBuf[iy+i][jx+j] = 0;
                }
            }
    }
}
