#include <bits/stdc++.h> 
using namespace std; 
long long findDigits(int n) 
{ 
	if (n < 0) 
		return 0; 

	if (n <= 1) 
		return 1; 

	double x = ((n * log10(n / M_E) + 
				log10(2 * M_PI * n) / 
				2.0)); 

	return floor(x) + 1; 
} 
int main() 
{ 
    string s;cin>>s;
    if(s=="1")cout<<1<<endl;
    else if(s=="2")cout<<2<<endl;
    else if(s=="6")cout<<3<<endl;
    else if(s=="24")cout<<4<<endl;
    else if(s=="120")cout<<5<<endl;
    else if(s=="720")cout<<6<<endl;
	for(int i=7;i<205051;i++)
	{
		if(findDigits(i) ==s.length())
		{
		cout<<i<<endl;
		break;}
	}
	return 0; 
} 



