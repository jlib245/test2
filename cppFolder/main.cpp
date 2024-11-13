#include <iostream>
#include <string>
using namespace std;

int main() {
    int i = 9;
    double f = 3.141592;
    int *pi;
    double *pf = &f;

    i = static_cast<int>(f);
    pi = (int*)pf;
    cout << *pi;
    return 0;

}