#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
    	int b;
    	cin>>b;
    	if(b>=-10 && b<=10)
    	{
    		if(abs(b)%2==0)
    		cout<<b<<" is even"<<endl;
    		else
    		cout<<b<<" is odd"<<endl;
		}
	}
}
