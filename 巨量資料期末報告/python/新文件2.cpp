#include<iostream>
using namespace std;
int main(){
//	string a="asd";
//	string *b;
//	b=&a;
//	*(b+1)=new string;
//	*(b+1)=a;
//	cout<<*(b+0)<<endl<<*(b+1)<<endl;
	char *ps;
	char **a;
	ps="C Language";
	a=&ps;
	a[1]=ps;
	//a[1]="asd";
	cout<<a[1];
}

