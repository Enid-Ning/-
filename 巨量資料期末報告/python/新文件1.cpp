#include <iostream>

using namespace std;

int main()
{string *a;
string b="d";
string c="sdf";
    a=&b;
    //*(a+0)="sdfg";
    *(a+1)=c;
    //*(a+2)="hhh";
    int i=0;
//    while(cin>>b){
//    	cout<<"b "<<b<<endl;
//        *(a+i)=b;
//        cout<<*(a+i);
//        i++;
//    }
cout<<a[1]<<endl;
//    for(int c=0;c<2;c++){
//        cout<<a[c]<<endl;
//    }
}

