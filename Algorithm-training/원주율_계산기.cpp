#include <iostream>
#include <math.h>
constexpr auto pi = 3.141592;
using namespace std;

int main(void)
{
	int radius;
	cout << "반지름을 입력하시오: ";
	cin >> radius;

	double area = 2*pi*pow(radius,2);
	cout << "원의 넓이는 " << area << "입니다.";
	
	//github edit test
	
	//re-test

	return 0;
}
