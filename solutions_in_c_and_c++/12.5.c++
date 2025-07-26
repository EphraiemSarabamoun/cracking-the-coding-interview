class Deep {
    int* data;
public:
    Deep(int val) { data = new int(val); }
    // Shallow copy ctor (default)
    // Deep copy ctor
    Deep(const Deep& other) {
        data = new int(*other.data);  // Deep
    }
    ~Deep() { delete data; }
};