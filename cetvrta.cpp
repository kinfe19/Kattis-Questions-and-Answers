#include <iostream>
using namespace std;
int main()
{
	int a,b,c,d,e,f,g,h;
	cin>>a>>b>>c>>d>>e>>f;
	g=a==c?e:(a==e?b:a);
	h=b==d?f:(b==f?d:b);
	cout<<g<<" "<<h;
}
