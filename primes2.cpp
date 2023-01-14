#include <bits/stdc++.h>
#define ll long long
// g++ -std=c++17    -o out.exe

using namespace std;

bool prime(ll n){

    bool f = true;
    for(ll i=2; i<=sqrt(n); i++){
        if(n%i == 0){
            f = false;
            break;
        }
    }
    if(n<2){f=false;}
    return f;
}

void print(int cc, int sm){
    int g = __gcd(cc, sm);
    cout<<cc/g<<"/"<<sm/g<<endl;
    }

int main(){
	int t, cc, b, o, d, h;
	string s;
	cin>>t;

	while(t--){
		b=1; o=1; d=1; h=1;
		cin >> s;
		for(int j=0; j<s.length(); j++){
            if(s[j] > 'F'){
                b = 0;
                o = 0;
                d = 0;
                h = 0;
                break;
            }
			else if(s[j] > '9'){
                b = 0;
                o = 0;
                d = 0;
			}
			else if(s[j] > '7'){
                o = 0;
                b = 0;
            }
            else if(s[j] > '1'){
                b = 0;
            }
		}

        cc = 0;
		if(b && prime(stoll(s, nullptr, 2))){
            cc++;
		}
		if(o && prime(stoll(s, nullptr, 8))){
            cc++;
		}
		if(d && prime(stoll(s, nullptr, 10))){
            cc++;
		}
		if(h && prime(stoll(s, nullptr, 16))){
            cc++;
		}
		print(cc, b+d+o+h);
	}
}

