#include <iostream>
#include <cstring>
using namespace std;

template <typename T1, typename T2>
class Box {
    T1 data1;
    T2 data2;
public :
    Box() {}
    T1 get_first();
    T2 get_second();
    void set_first(T1 value) {
        data1 = value;
    }
    void set_second(T2 value) {
        data2 = value;
    }
};

template <typename T1, typename T2>
T1 Box<T1, T2>::get_first() {
    return data1;
}

template <typename T1, typename T2>
T2 Box<T1, T2>::get_second() {
    return data2;
}

int main() {
    Box<int, int> box;
    box.set_first(10);
    box.set_second(40);
    cout << box.get_first() << box.get_second() << endl;


    return 0;
}