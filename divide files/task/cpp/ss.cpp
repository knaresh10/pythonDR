#include<iostream>
using namespace std;
inline void fun(int n)// request
{
	cout<<n;
}
int main()
{
	int n;
	cin>>n;
	fun(n);//fun call cout<<n;
}
