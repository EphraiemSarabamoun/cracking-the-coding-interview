#include <cstdlib>

void* alignedMalloc(size_t size, size_t align) {
    void* ptr = std::malloc(size + align - 1 + sizeof(void*));
    if (!ptr) return nullptr;
    void* aligned = reinterpret_cast<void*>((reinterpret_cast<size_t>(ptr) + sizeof(void*) + align - 1) & ~(align - 1));
    *(reinterpret_cast<void**>(aligned) - 1) = ptr;
    return aligned;
}

void alignedFree(void* p) {
    if (!p) return;
    void* original = *(reinterpret_cast<void**>(p) - 1);
    std::free(original);
}