#include <iostream>

class Base {
    public:
        virtual ~Base() { std::cout << "Base dtor"; }  // Virtual
    };
    
    class Derived : public Base {
        int* data;
    public:
        Derived() { data = new int[10]; }
        ~Derived() { delete[] data; std::cout << "Derived dtor"; }
    };
    
    Base* b = new Derived();
    delete b;