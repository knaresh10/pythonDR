#include<iostream>
#include<string>
using namespace std;

class countOne{
	public:
		void counting(int c)
		{
			if(c%2)
			{
				cout<<c<<" odd";
			}
			else
			{
				cout<<c<<" even";
			}
		}
};

class tellone:public countOne{
	public:
		int count(string str)
		{
			int c=0;
			for(int i=0;i<str.length();i++)
			{
				if(str[i]=='1')
				{
					c++;
				}
			}
			counting(c);
		}
};
int main()
{
	string st;
	cin>>st;
	tellone t;
	t.count(st);
}
	
	
	
	
	


