#include <bits/stdc++.h>
using namespace std;



int main(){
	int n, c, e=1;
	while(cin >> n){
		int arr[n];
		for(int i=0; i<n; i++){
			cin>>arr[i];
		}
		vector<int>v;
		for(int i=0; i<n; i++){
			for(int j=i+1; j<n; j++){
				v.push_back(arr[i] + arr[j]);
			}
		}
		cout<<"Case "<<e<<":\n";
		e++;
		//sort(v.begin(), v.end());
		int q;cin>>q;
		for(int i=0; i<q; i++){
			int h; cin>>h;
			vector<int> v2(v.begin(), v.end()); 
			v2.push_back(h);
			sort(v2.begin(), v2.end());
			int dx = distance(v2.begin(), find(v2.begin(), v2.end(), h));
			int bk=h-9999999, fr=h+9999999;
			if(dx-1>=0) bk = v2[dx-1];
			if(dx+1 < v2.size())fr = v2[dx+1];
			if(h-bk <= fr-h)cout<<"Closest sum to "<<h<<" is "<<bk<<".\n";
			else cout<<"Closest sum to "<<h<<" is "<<fr<<".\n";
				
		}
		
	}
	
}