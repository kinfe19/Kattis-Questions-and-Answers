
#include <bits/stdc++.h>
using namespace std;
bitset< 100000000 > arr;
int main(){
	long long n, k, a, b,c=0;
	cin>>n>>a;
	arr[0] = 1;
	arr[1] = 1;
	k = ceil(sqrt(n));
	for(int i=2; i<=k; i++){
		if (arr[i] == 0){
			for(int j=2*i; j<=n; j+=i){
				arr[j] = 1;
			}
		}
	}
	for(int i=0;i<=n;i++){
		if(!arr[i]){
			c++;
		}
	}
	cout<<c<<endl;
	for(int i=0;i<a;i++)
	{
		cin>>b;
		cout<<!arr[b]<<endl;
	}


}
