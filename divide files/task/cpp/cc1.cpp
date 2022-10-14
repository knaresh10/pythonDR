#include<iostream>
#include<cmath>
using namespace std;

class QuaRoot{
	public:
		int a,b,c,d;
		float r1,r2;
		QuaRoot(int a,int b,int c)
		{
			this->a = a;
			this->b = b;
			this->c = c;
		}
		void calculate_discr()
		{
			this->d = (b*b)-(4*a*c);
		}
		void calculate_roots()
		{
			if(this->d>0)
			{
				this->r1 = (-b+sqrt(this->d))/(2*a);
				this->r2 = (-b-sqrt(this->d))/(2*a);
				cout<<"Roots are real and UnEqual "<<this->r1<<" "<<this->r2;	
			}
			else if(this->d==0)
			{
				this->r1 = -b/(2*a);
				this->r2 = -b/(2*a);
				cout<<"Roots are real and Equal "<<this->r1<<" "<<this->r2;	
			}
			else
			{
				cout<<"Imaginary Roots";
			}
			
		}
		
};

int main()
{
	int a,b,c;
	cin>>a>>b>>c;
	QuaRoot Q1(a,b,c);
	Q1.calculate_discr();
	Q1.calculate_roots();
}

