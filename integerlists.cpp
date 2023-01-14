#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n,m;
    cin>>n;
    for(int i=0; i<n; i++)
    {
        string a,b;
        cin>>a>>m>>b;
        deque<string>v;
        string ss="";
        for(int j=1; j<b.length()-1; j++)
        {
            if(b[j]==',')
            {
                v.push_back(ss);
                ss="";
            }
            else
            {
                ss+=b[j];
            }
        }
        v.push_back(ss);
        int qq=0,dd=0;
        for(int k=0; k<a.length(); k++)if(a[k]=='D')dd++;
        if(dd>m)cout<<"error"<<endl;
        else if(dd==m)cout<<"[]"<<endl;
        else
        {
            for(int k=0; k<a.length(); k++)
            {
                if(a[k]=='R')
                    qq++;
                else if(a[k]=='D')
                {
                    if(qq%2==0)
                        v.pop_front();
                    else if(qq%2==1)
                        v.pop_back();
                }
            }
            if(qq%2==0)
            {
            cout<<"[";
            for(int x=0; x<v.size()-1; x++)
                cout<<v[x]<<",";
            cout<<*(v.end()-1)<<"]"<<endl;
        	}
        	else{
        		cout<<"[";
        		for(int x=v.size()-1; x>0; x--)
                cout<<v[x]<<",";
                cout<<v[0]<<"]"<<endl;
			}



        }
    }

}