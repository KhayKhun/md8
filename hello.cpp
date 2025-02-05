#include <iostream>
using namespace std;

int x = 69;
// x = 90; // No assignement in root, only in functions and methods

const string name = "dfsdf";
char a = 'a';
int num1, num2;
int main()
{
    x = 90;

    cout << "Num 1: ";
    cin >> num1;
    cout << "Num 2: ";
    cin >> num2;

    cout << num1 + num2;
    return 0;
}