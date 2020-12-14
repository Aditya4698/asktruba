#include<iostream>
using namespace std;
void func(int n);
int main()
{
    int n;
    cout<<"Enter no. of terms";
    cin>>n;
    func(n);
    return 0;
}
void func(int n)
{
    int a1=0,a2=1;
    int next;
    for (int i = 1; i <= n; i++)
    {
        if (i==0)
        {
            cout<<"0 ";
        }
        if (i==1)
        {
            cout<<"1 ";
        }
        else
        {
            next=a1+a2;
            a1=a2;
            a2=next;
            cout<<next<<" ";   
        }
    }   
}