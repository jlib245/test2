#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<double> scores;

    while (true) {
        double value = 0.0;
        cout << "성적을입력하세요(종료 : -1) : ";
        cin >> value;
        if (value < 0) {
            break;
        }
        scores.push_back(value);
    }
    
    double highest = -100;
    vector<double>::iterator it;
    for (it = scores.begin(); it < scores.end(); it++) {
        if (*it > highest) {
            highest = *it;
        }
    }

    cout << "최고 성적은" << highest << "점입니다.\n";

    return 0;
}