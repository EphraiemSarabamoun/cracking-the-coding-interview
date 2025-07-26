#include <iostream>

template <typename T>
class SmartPtr {
private:
    T* ptr;        
    int* ref_count; 

public:
    explicit SmartPtr(T* p = nullptr) : ptr(p), ref_count(new int(1)) {
        if (p == nullptr) {
            *ref_count = 0;
        }
    }
    SmartPtr(const SmartPtr& other) : ptr(other.ptr), ref_count(other.ref_count) {
        if (ref_count) {
            (*ref_count)++;
        }
    }
    SmartPtr& operator=(const SmartPtr& other) {
        if (this != &other) {
            if (ref_count) {
                (*ref_count)--;
                if (*ref_count == 0) {
                    delete ptr;
                    delete ref_count;
                }
            }
            ptr = other.ptr;
            ref_count = other.ref_count;
            if (ref_count) {
                (*ref_count)++;
            }
        }
        return *this;
    }
    ~SmartPtr() {
        if (ref_count) {
            (*ref_count)--;
            if (*ref_count == 0) {
                delete ptr;
                delete ref_count;
            }
        }
    }
    T& operator*() const {
        return *ptr;
    }
    T* operator->() const {
        return ptr;
    }

    T* get() const {
        return ptr;
    }
    bool isNull() const {
        return ptr == nullptr;
    }

    int useCount() const {
        return ref_count ? *ref_count : 0;
    }
};
int main() {
    SmartPtr<int> sp1(new int(42));
    std::cout << "Value: " << *sp1 << std::endl; // 42
    std::cout << "Use count: " << sp1.useCount() << std::endl; // 1

    {
        SmartPtr<int> sp2 = sp1;
        std::cout << "Value (sp2): " << *sp2 << std::endl; // 42
        std::cout << "Use count: " << sp1.useCount() << std::endl; // 2
    }

    std::cout << "Use count after scope: " << sp1.useCount() << std::endl; // 1

    return 0;
}