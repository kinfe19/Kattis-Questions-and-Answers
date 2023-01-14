#include <iostream>
using namespace std;
int main()
{
	int a,b,c,m=0;
	cin>>a>>b>>c;
	int a1,a2,b1,b2,c1,c2,mi1,mi2,mi3,min,ma1,ma2,ma3,max;
	cin>>a1>>a2>>b1>>b2>>c1>>c2;
	mi1=a1<a2?a1:a2;
	ma1=a1>a2?a1:a2;
	mi2=b1<b2?b1:b2;
	ma2=b1>b2?b1:b2;
	mi3=c1<c2?c1:c2;
	ma3=c1>c2?c1:c2;
    if(ma1>ma2&&ma1>ma3)
    max=ma1;
    else if(ma2>ma3&&ma2>ma1)
    max=ma2;
    else
    max=ma3;
    if(mi1<mi2&&mi1<mi3)
    min=mi1;
    else if(mi2<mi3&&mi2<mi1)
    min=mi2;
    else
    min=mi3;
	for(int i=min;i<=max;i++)
	{
		int bo=0;
		if(i>a1&&i<=a2)
		bo++;
		if(i>b1&&i<=b2)
		bo++;
		if(i>c1&&i<=c2)
		bo++;
		if(bo==1)
		m+=a*bo;
		else if(bo==2)
		m+=b*bo;
		else if(bo==3)
		m+=c*bo;
	}
	cout<<m;
}
