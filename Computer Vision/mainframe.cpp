#include <QFileDialog>
#include <QPainter>

#include "mainframe.h"
#include "ui_mainframe.h"
#include "imageform.h"
#include "contrast.h"
#include "sepiaTone.h"
#include "otsulabeling.h"
#include "histogram.h"
#include "filtering.h"
#include "cannyedge.h"
#include "hough.h"
#include "opticalflow.h"
#include <stdlib.h>
#include <fstream>

MainFrame::MainFrame(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::MainFrame)
{
    ui->setupUi(this);

    _plpImageForm       = new KPtrList<ImageForm*>(10,false,false);
    _q_pFormFocused     = 0;

    //객체 맴버의 초기화

    //get a current directory
    char st[100];
    GetCurrentDirectoryA(100,st);

    //리스트 출력창을 안보이게
    ui->listWidget->setVisible(false);
    this->adjustSize();

    //UI 활성화 갱신
    UpdateUI();
}

MainFrame::~MainFrame()
{ 
    delete ui;         
    delete _plpImageForm;
}

void MainFrame::CloseImageForm(ImageForm *pForm)
{
    //ImageForm 포인터 삭제
    _plpImageForm->Remove(pForm);

    //활성화 ImageForm 초기화
    _q_pFormFocused     = 0;

    //관련 객체 삭제

    //UI 활성화 갱신
    UpdateUI();
}

void MainFrame::UpdateUI()
{
    if(ui->tabWidget->currentIndex() == 0)
    {
        ui->buttonSepiaTone->setEnabled( _q_pFormFocused &&  _q_pFormFocused->ID() == "OPEN" );
        ui->buttonContrast->setEnabled( _q_pFormFocused &&  _q_pFormFocused->ID() == "OPEN" );
        ui->buttonOtsu_Labeling->setEnabled(_q_pFormFocused &&  _q_pFormFocused->ID() == "OPEN");
    }
    else if(ui->tabWidget->currentIndex() == 1)
    {
        ui->button_Histo_Eq->setEnabled(_q_pFormFocused &&  _q_pFormFocused->ID() == "OPEN");
        ui->button_Histo_Matching->setEnabled(_plpImageForm->Count() == 2);
        ui->buttonMedian->setEnabled(_q_pFormFocused &&  _q_pFormFocused->ID() == "OPEN");
        ui->buttonGaussian->setEnabled(_q_pFormFocused &&  _q_pFormFocused->ID() == "OPEN");
        ui->button_CannyEdge->setEnabled(_q_pFormFocused &&  _q_pFormFocused->ID() == "OPEN");

    }
    else if(ui->tabWidget->currentIndex() == 2)
    {

    }    
}

void MainFrame::OnMousePos(const int &nX, const int &nY, ImageForm* q_pForm)
{
    UpdateUI();
}

void MainFrame::closeEvent(QCloseEvent* event)
{
    //생성된 ImageForm을 닫는다.
    for(int i=_plpImageForm->Count()-1; i>=0; i--)
        _plpImageForm->Item(i)->close();

    //리스트에서 삭제한다.
    _plpImageForm->RemoveAll();
}


void MainFrame::on_buttonOpen_clicked()
{
    //이미지 파일 선택
    QFileDialog::Options    q_Options   =  QFileDialog::DontResolveSymlinks  | QFileDialog::DontUseNativeDialog; // | QFileDialog::ShowDirsOnly
    QString                 q_stFile    =  QFileDialog::getOpenFileName(this, tr("Select a Image File"),  "./data", "Image Files(*.bmp *.ppm *.pgm *.png)",0, q_Options);

    if(q_stFile.length() == 0)
        return;

    //이미지 출력을 위한 ImageForm 생성    
    ImageForm*              q_pForm   = new ImageForm(q_stFile, "OPEN", this);

    _plpImageForm->Add(q_pForm);
    q_pForm->show();

    //UI 활성화 갱신
    UpdateUI();
}

void MainFrame::on_buttonDeleteContents_clicked()
{
    //생성된 ImageForm을 닫는다.
    for(int i=_plpImageForm->Count()-1; i>=0; i--)
        _plpImageForm->Item(i)->close();

    //리스트에서 삭제한다.
    _plpImageForm->RemoveAll();
}

void MainFrame::on_buttonSepiaTone_clicked()
{
    //포커스 된 ImageForm으로부터 영상을 가져옴
    KImageColor   icMain;    
    if(_q_pFormFocused != 0 && _q_pFormFocused->ImageColor().Address() &&  _q_pFormFocused->ID() == "OPEN")
        icMain = _q_pFormFocused->ImageColor();
    else
        return;

    //hue, saturation 값 가져오기
    double dHue = ui->spinHue->text().toDouble();
    double dSat = ui->spinSaturation->text().toDouble(); ;

    KImageHSV HSV_img; //비어있는 HSV 객체 선언
    HSV_img.COLORtoHSV(icMain); //icMain의 rgb를 이용하여 h,s,v 값을 계산 후 HSV_img 객체에 저장
    HSV_img.HSVtoSepiaColor(icMain,dHue,dSat); // dHue, dSat값을 바탕으로 icMain 이미지 변환

    //출력을 위한 ImageForm 생성
    ImageForm*  q_pForm = new ImageForm(icMain, "Sepia Tone", this);

    _plpImageForm->Add(q_pForm);
    q_pForm->show();

    //UI 활성화 갱신
    UpdateUI();
}


void MainFrame::on_buttonShowList_clicked()
{
    static int nWidthOld = ui->tabWidget->width();

    if(ui->listWidget->isVisible())
    {
        nWidthOld = ui->listWidget->width();
        ui->listWidget->hide();
        this->adjustSize();
    }
    else
    {        
        ui->listWidget->show();
        QRect q_rcWin = this->geometry();

        this->setGeometry(q_rcWin.left(), q_rcWin.top(), q_rcWin.width()+nWidthOld, q_rcWin.height());
    }
}

void MainFrame::on_buttonContrast_clicked()
{
    //포커스 된 ImageForm으로부터 영상을 가져옴
    KImageGray   igMain;
    if(_q_pFormFocused != 0 && _q_pFormFocused->ImageColor().Address() &&  _q_pFormFocused->ID() == "OPEN")
        igMain = _q_pFormFocused->ImageColor().ColorToGray(); // Color이미지일 경우 GrayScale로 변환
    else if(_q_pFormFocused != 0 &&  _q_pFormFocused->ImageGray().Address() && _q_pFormFocused->ID() == "OPEN")
        igMain = _q_pFormFocused->ImageGray(); //GrayScale의 경우 그대로
    else
        return;

    // ui spinbox에서 변수를 가져옴
    int max = ui->spinMax->text().toInt(); //픽셀의 최대값 설정
    int min = ui->spinMin->text().toInt(); //픽셀의 최소값 설정
    // x_out = inc*(x_in - x_icpt) : 2차 방정식 이용.
    double inc = ui->doubleInc->text().toDouble(); //직선의 기울기 설정
    double x_icpt = ui->doubleIcpt_x->text().toDouble(); //직선의 x절편 설정

    contrast con_t(max, min, inc, x_icpt); //인수를 참고하여 contrast transform을 위한 식 설정 및 변환 준비
    con_t.transform(igMain); //igMain을 설정된 변수를 참고하여 contrast transform 실행

    //출력을 위한 ImageForm 생성
    ImageForm*  q_pForm = new ImageForm(igMain, "Luminance Transform", this);

    _plpImageForm->Add(q_pForm);
    q_pForm->show();

    //UI 활성화 갱신
    UpdateUI();
}

void MainFrame::on_buttonOtsu_Labeling_clicked()
{
    KImageGray   igMain;
    if(_q_pFormFocused != 0 &&  _q_pFormFocused->ImageGray().Address() && _q_pFormFocused->ID() == "OPEN")
        igMain = _q_pFormFocused->ImageGray();
    else
        return;

    otsu_lbl otsu(igMain); //igMain영상의 정보를 저장
    otsu.get_hist(); //저장된 정보로 히스토그램을 구한다
    int th = otsu.otsu_threhold(); // 히스토그램을 이용해 Otsu임계점을 구한다
    qDebug("th == %d",th);
    otsu.binary_transform(th); // 찾은 Otsu임계점을 이용하여 영상 이진화
    KImageColor cimg(igMain.Row(),igMain.Col()); // 라벨링 영상을 담기 위한 KImageColor 객체
    otsu.labeling(cimg); // 이진화된 영싱을 라벨링 후 cimg에 반환

    ImageForm*  q_pForm = new ImageForm(otsu.img(), "Otsu Thresholding", this);
    ImageForm*  q_pForm2 = new ImageForm(cimg, "Color Labeling", this);
    _plpImageForm->Add(q_pForm);
    _plpImageForm->Add(q_pForm2);
    q_pForm2->show();
    q_pForm->show();

    //UI 활성화 갱신
    UpdateUI();

}

void MainFrame::on_button_Histo_Eq_clicked()
{
    KImageColor   icMain;
    if(_q_pFormFocused != 0 && _q_pFormFocused->ImageColor().Address() &&  _q_pFormFocused->ID() == "OPEN")
        icMain = _q_pFormFocused->ImageColor();
    else
        return;

    Histo hist;
    hist.HEQ(icMain);

    ImageForm*  q_pForm = new ImageForm(icMain, "HEQ", this);
    _plpImageForm->Add(q_pForm);
    q_pForm->show();
    UpdateUI();
}

void MainFrame::on_button_Histo_Matching_clicked()
{
    KImageColor   icMain1;
    KImageColor   icMain2;
    if(_plpImageForm != 0 && _plpImageForm->First()->ImageColor().Address()
            && _plpImageForm->Last()->ImageColor().Address() && _plpImageForm->Count() == 2){
        icMain1 = _plpImageForm->First()->ImageColor();
        icMain2 = _plpImageForm->Last()->ImageColor();
    } else
        return;

    Histo hist;
    hist.histo_matching(icMain1, icMain2);

    ImageForm*  q_pForm = new ImageForm(icMain1, "Hist Match", this);
    _plpImageForm->Add(q_pForm);
    q_pForm->show();
    UpdateUI();
}

void MainFrame::on_buttonGaussian_clicked()
{
    KImageGray   igMain;
    if(_q_pFormFocused != 0 &&  _q_pFormFocused->ImageGray().Address() && _q_pFormFocused->ID() == "OPEN")
        igMain = _q_pFormFocused->ImageGray();
    else
        return;

    gaussian gaus;
    gaus.get_gauss_nz(igMain, 500);
    ImageForm*  q_pForm = new ImageForm(igMain, "Gaussian Noise", this);

    gaus.filtering(igMain, 2, 3);
    ImageForm*  q_pForm2 = new ImageForm(igMain, "Gaussian Filtering", this);

    _plpImageForm->Add(q_pForm);
    _plpImageForm->Add(q_pForm2);
    q_pForm->show();
    q_pForm2->show();
    UpdateUI();
}

void MainFrame::on_buttonMedian_clicked()
{
    KImageGray   igMain;
    if(_q_pFormFocused != 0 &&  _q_pFormFocused->ImageGray().Address() && _q_pFormFocused->ID() == "OPEN")
        igMain = _q_pFormFocused->ImageGray();
    else
        return;

    median md;
    md.get_st_pp(igMain, 0.003);
    ImageForm*  q_pForm = new ImageForm(igMain, "Salt Pepper Noise", this);


    md.filtering(igMain, 3);
    ImageForm*  q_pForm2 = new ImageForm(igMain, "Median Filtering", this);

    _plpImageForm->Add(q_pForm);
    _plpImageForm->Add(q_pForm2);
    q_pForm->show();
    q_pForm2->show();
    UpdateUI();
}

void MainFrame::on_button_CannyEdge_clicked()
{
    KImageGray   igMain;
    if(_q_pFormFocused != 0 &&  _q_pFormFocused->ImageGray().Address() && _q_pFormFocused->ID() == "OPEN")
        igMain = _q_pFormFocused->ImageGray();
    else
        return;

    KImageGray outimg;
    CannyEdge CE;
    CE.opCannyEdge(17,50,1.0,igMain,outimg);

    ImageForm*  q_pForm = new ImageForm(outimg, "Canny Edge", this);
    _plpImageForm->Add(q_pForm);
    q_pForm->show();

    UpdateUI();
}

void MainFrame::on_buttn_HoughCircle_clicked()
{
    KImageGray   igMain;
    if(_q_pFormFocused != 0 &&  _q_pFormFocused->ImageGray().Address() && _q_pFormFocused->ID() == "OPEN")
        igMain = _q_pFormFocused->ImageGray();
    else
        return;

    KImageGray outimg;
    Hough_T HC;
    // CannyEdge실행 (min_thres, max_thres, sigma, img_in, img_out)
    HC.opCannyEdge(3,30,1.0,igMain,outimg);

    // Find Hough Circle (img_out, min_radian, max_radian)
    HC.get_HoughCircle(igMain, 50, 53);

    ImageForm*  q_pForm = new ImageForm(igMain, "Find Circle of Coin", this);
    _plpImageForm->Add(q_pForm);
    q_pForm->show();

    UpdateUI();
}

void MainFrame::on_button_General_Hough_clicked()
{
    KImageGray   igMain;
    if(_q_pFormFocused != 0 &&  _q_pFormFocused->ImageGray().Address() && _q_pFormFocused->ID() == "OPEN")
        igMain = _q_pFormFocused->ImageGray();
    else
        return;


    // txt파일을 읽어옵니다
    QString q_stFile = QFileDialog::getOpenFileName(this, tr("Select a Plug File"), "./");
    if(q_stFile.length() == 0) {
            return;
    }

    const char *szMap = q_stFile.toStdString().c_str();
    FILE* fp = fopen(szMap,"rt");
    vector<KPOINT> pixels;
    int nX, nY;
    while(true){
        fscanf(fp,"%d %d", &nX, &nY); // n각형 n번 꼭지점 모두 읽어오기
        if(feof(fp)) break;
        pixels.push_back(KPOINT(nX,nY)); // 해당 픽셀 pixels 벡터에 저장
    }
    fclose(fp);

    KImageGray outimg;
    Hough_T GH;
    GH.opCannyEdge(17,50,1.0,igMain, outimg); // CannyEdge 실행
    GH.get_shape_table(pixels); // shape_table을 만듭니다
    GH.find_shape(igMain, 80, 84, 270, 300); // 해당 shape를 찾습니다
    GH.get_HoughCircle(igMain,50, 53); // hough circle을 찾습니다

    ImageForm*  q_pForm = new ImageForm(igMain, "Find Plug", this);
    _plpImageForm->Add(q_pForm);
    q_pForm->show();

    UpdateUI();
}

void MainFrame::on_button_image_load_clicked()
{
    QFileDialog::Options    q_Options   =  QFileDialog::DontResolveSymlinks  | QFileDialog::DontUseNativeDialog; // | QFileDialog::ShowDirsOnly
    QString q_stFile;

    int img_nums = 2; // 이미지의 개수

    for(int i = 0; i < img_nums; i++){
        q_stFile    =  QFileDialog::getOpenFileName(this, tr("Select a Image File"),  "./data", "Image Files(*.bmp *.ppm *.pgm *.png)",0, q_Options);

        if(q_stFile.length() == 0)
            return;

        QString window_name = "Image";
        window_name.append(to_string(i+1).c_str());

        ImageForm*  q_pForm = new ImageForm(q_stFile, window_name, this);
        _plpImageForm->Add(q_pForm);
        q_pForm->show();
    }

    UpdateUI();
}

void MainFrame::on_button_Opticalflow_clicked()
{
    int img_nums = 2; // 이미지의 개수
    int res = 3; // 선의 밀도. 낮을수록 촘촘하다

    vector<KImageGray> Images;
    for(int i = 0; i < (int)_plpImageForm->Count(); i++)
        Images.push_back(_plpImageForm->Item(i)->_igMain);

    for(int i = 0; i < img_nums - 1; i++){
        OpticalFlow OF(1.0);
        KImageGray outimg = OF.get_OFimg(Images[i], Images[i+1]);
        QString window_name = "Image";
        window_name.append(to_string(i+1).c_str());
        ImageForm*  q_pForm = new ImageForm(outimg.GrayToRGB(), window_name, this);

        // draw line
        for(int i = 0; i < (int)outimg.Row(); i+=res)
            for(int j = 0; j < (int)outimg.Col(); j+=res){
                int u = OF.UV(i,j).first;
                int v = OF.UV(i,j).second;
                if(i+u < 0 || i+u >= (int)outimg.Row() || j+v < 0 || j+v >= (int)outimg.Col()) continue;
                if(u == 0 && v == 0) continue; // 움직임이 없는 부분 제외
                if(u > OF.KSize || v > OF.KSize || u < -OF.KSize || v < -OF.KSize) continue;
                q_pForm->DrawLine(j+u,i+v,j,i,QColor(255,255,255));
            }
        q_pForm->show();
        UpdateUI();
    }
}
