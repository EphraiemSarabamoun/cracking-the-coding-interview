#include <iostream>

int main() {
class Base {
public:
virtual void func() { std::cout << "Base"; }
};

class Derived : public Base {
public:
void func() override { std::cout << "Derived"; }
};

Base* b = new Derived();
b->func();
delete b;  // Clean up memory
return 0;
}