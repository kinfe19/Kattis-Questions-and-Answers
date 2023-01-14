#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,a[45]={1,1};
	for(int i=2;i<45;i++)a[i]=a[i-1]+a[i-2];
	cin>>n;
	if(n==0)cout<<"1 0\n";
	else if(n==1)cout<<"0 1\n";
	else{
		cout<<a[n-2]<<" "<<a[n-1]<<endl;
	}
}
