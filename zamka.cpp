#include <iostream>
using namespace std;
int main()
{
	int l,d,x,n,m;
	cin>>l>>d>>x;
	for(int i=l;i<=d;i++){
		int k=0,f=0;
		int l=i;
		while(f<9)
		{
			k+=l%10;
			l=(l-(l%10))/10;
			f++;
		}
		if(k==x)
		{
			n=i;
			break;
		}
	}
	for(int j=d;j>=l;j--){
		int k=0,f=0;
		int l=j;
		while(f<9)
		{
			k+=l%10;
			l=(l-(l%10))/10;
			f++;
		}
		if(k==x)
		{
			m=j;
			break;
		}
	}
	cout<<n<<endl<<m<<endl;
}
