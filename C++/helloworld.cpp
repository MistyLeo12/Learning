#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> msg {"Hello", "World", "Just Learning", "how to compile C++", "in VS Code"};
    for (const string& word: msg)
    {
        cout << word << " ";
    }
    cout << endl; 
}