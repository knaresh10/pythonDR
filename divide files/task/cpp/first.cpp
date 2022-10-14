#include<iostream>
#include <bits/stdc++.h>
#include<string>
using namespace std;

class frequency{
	string bin;
	public:
		void stringLength(string str)
		{
			cout<<" "<<str.length();
		}
		void distinctChars(string str)
		{
			unordered_set<char> s;
    		for (int i = 0; i < str.size(); i++) {
			s.insert(str[i]);
    		}
    		cout<<" "<<s.size();
		}
};

class counting:public frequency{
	public:
		void count(string str)
		{
			cout<<str;
			stringLength(str);
			distinctChars(str);
		}
};
int main()
{
	string st;
	cin>>st;
	counting t;
	t.count();
}
	
	
	
	
	


