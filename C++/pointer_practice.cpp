#include <iostream>
using namespace std;


int main(){
    int ExampleArray[10];
    
    int *pointerLocation2 = &ExampleArray[2];
    int *pointerLocation0 = &ExampleArray[0];

    cout << "pointerLocation2 = " << (int)pointerLocation2 << endl;
    cout << "pointerLocation0 = " << (int)pointerLocation0 << endl;
    cout << "pointerLocation6 = " << pointerLocation2 - pointerLocation0 << endl;
    cout << endl; 
    system("pause");
    return 0;
}