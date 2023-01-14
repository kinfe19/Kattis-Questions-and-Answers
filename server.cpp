#include <bits/stdc++.h>
using namespace std;
int main()
{
	int a,b,l=0,h=0;
	cin>>a>>b;
	for(int i=0;i<a;i++)
	{
		int s;
		cin>>s;
		h=h+s;
		if(h<=b)
		{
			l++;
		}

	}
	cout<<l;
}