#include <iostream>
using namespace std;
int main()
{
	int a,b;
	cin>>a>>b;
	int i=0;
	while(a!=0 || b!=0)
	{
		if(a+b==13)
		cout<<"Never speak again."<<endl;
		else if(a>b)
		cout<<"To the convention."<<endl;
		else if(a<b)
		cout<<"Left beehind."<<endl;
		else
		cout<<"Undecided."<<endl;
		cin>>a>>b;
		i++;
	}
}
