#include <iostream>
#include <iostream>

template <typename K, typename V>
class HashTable {
    std::vector<std::list<std::pair<K, V>>> buckets;
    size_t size;
};