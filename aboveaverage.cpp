#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;cin>>t;
	for(int i=0;i<t;i++)
	{
		int a,b;cin>>a;int A[a];double d,s=0,e=0;
		for(int j=0;j<a;j++){
			cin>>b;
			A[j]=b;
			s+=b;
		}
		d=s/a;
		for(int j=0;j<a;j++)
			if(A[j]>d)e++;
		cout<<fixed<<setprecision(3)<<e/a*100<<"%"<<endl;
	}
}