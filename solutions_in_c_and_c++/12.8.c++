struct Node {
    int val;
    Node* left;
    Node* right;
};

Node* copyNode(Node* node) {
    if (!node) return nullptr;
    Node* newNode = new Node{node->val, nullptr, nullptr};
    newNode->left = copyNode(node->left);
    newNode->right = copyNode(node->right);
    return newNode;
}