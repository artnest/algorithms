#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

class BinaryTree {
	private:
	    struct Node {
		    int Info;
	        Node* LSon;
	        Node* RSon;
            int LHeight;
            int RHeight;
            int LSize;
            int RSize;

            void PreOrderCount(Node*, std::vector<int>&) const;
            void CountSubtrees(Node*);
	    };
	    Node* Root;
	public:
	    BinaryTree();
	    ~BinaryTree();
	    BinaryTree::Node* Insert(Node*, const int&);
	    BinaryTree::Node* EraseByValue(Node*, int&);
	    BinaryTree::Node* Search(const int, Node*);
	    BinaryTree::Node* GetRoot();
	    BinaryTree::Node* FindMax(Node*);
	    BinaryTree::Node* FindMin(Node*);
	    BinaryTree::Node* Successor(const int);
        void PreOrder(Node*, void Print(const int)) const;
        void UpdateInfo();
        void CountSpecialKeys(Node*, std::vector<int>&);
	private:
	    BinaryTree::Node* CloneNode(Node*);
	    void Erase(Node*);
        int Height(Node*);
        void PreOrderHeights(Node*);
        void UpdateSubtreesSizes(Node*);
        void UpdateSubtreesHeights(Node*);
};

BinaryTree::BinaryTree() {
    Root = NULL;
}

BinaryTree::~BinaryTree() {
    Erase(Root);
}

void BinaryTree::Erase(Node* t) {
    if (t != NULL) {
        Erase(t->LSon);
        Erase(t->RSon);
        delete t;
    }
}

BinaryTree::Node* BinaryTree::Insert(Node* t, const int &value) {
	if (Search(value, t)) {
        return NULL;
    }

	if (t == NULL) {
		t = new Node;
		t->Info = value;
		t->LSon = t->RSon = NULL;
	} else if (value < t->Info) {
			t->LSon = Insert(t->LSon, value);
    } else {
		t->RSon = Insert(t->RSon, value);
    }

	if (Root == NULL) {
		Root = t;
    }
	return t;
}

BinaryTree::Node* BinaryTree::EraseByValue(Node* t, int &value) {
	if (t == NULL) {
		return t;
    } else if (value < t->Info) {
			t->LSon = EraseByValue(t->LSon, value);
        } else if (value > t->Info) {
				t->RSon = EraseByValue(t->RSon, value);
            } else if (t->LSon == NULL && t->RSon == NULL) {
					if (t == Root) {
						Root = NULL;
                    } else {
						delete t;
						t = NULL;
					}
				} else if (t->LSon == NULL) {
						Node* temp = t;
						t = t->RSon;
						if (temp == Root) {
							Root = t;
                        }
						delete temp;
					} else if (t->RSon == NULL) {
							Node* temp = t;
							t = t->LSon;
							if (temp == Root) {
								Root = t;
                            }
							delete temp;
					} else {
							Node* temp = FindMin(t->RSon);
							t->Info = temp->Info;
							t->RSon = EraseByValue(t->RSon, temp->Info);
					}
	return t;
}

BinaryTree::Node* BinaryTree::Search(const int value, Node* t) {
    if (t == NULL || value == t->Info) {
        return t;
    }

    if (value < t->Info) {
		return Search(value, t->LSon);
	} else {
			return Search(value, t->RSon);
	}
}

void BinaryTree::PreOrder(Node* t, void Print(const int)) const {
	if (Root == NULL) {
		throw "null\n";
    }

	if (t == NULL) {
		return;
    }

    Print(t->Info);
	PreOrder(t->LSon, Print);
	PreOrder(t->RSon, Print);
}

void BinaryTree::Node::PreOrderCount(Node* node, std::vector<int>& v) const {
    if (node == NULL) {
        return;
    }

    v.push_back(node->Info);
    PreOrderCount(node->LSon, v);
    PreOrderCount(node->RSon, v);
}

void BinaryTree::Node::CountSubtrees(Node* node) {
    if (node->LSon != NULL) {
        std::vector<int> v;
        Node::PreOrderCount(node->LSon, v);
        node->LSize = v.size();
    }

    if (node->RSon != NULL) {
        std::vector<int> v;
        Node::PreOrderCount(node->RSon, v);
        node->RSize = v.size();
    }
}

int BinaryTree::Height(Node* node) {
    if (node == NULL) {
        return 0;
    }

    if (node->LSon != NULL) {
        node->LHeight = Height(node->LSon);
    } else {
        node->LHeight = -1;
    }

    if (node->RSon != NULL) {
        node->RHeight = Height(node->RSon);
    } else {
        node->RHeight = -1;
    }

    return std::max(node->LHeight, node->RHeight) + 1;
}

void BinaryTree::PreOrderHeights(Node* node) {
	if (node == NULL) {
		return;
    }

    node->LHeight = Height(node->LSon);
    node->RHeight = Height(node->RSon);
	PreOrderHeights(node->LSon);
	PreOrderHeights(node->RSon);
}

void BinaryTree::UpdateSubtreesHeights(Node* node) {
    if (node == NULL) {
        return;
    }

    PreOrderHeights(node);
    UpdateSubtreesHeights(node->LSon);
    UpdateSubtreesHeights(node->RSon);
}

void BinaryTree::UpdateSubtreesSizes(Node* node) {
    if (node == NULL) {
        return;
    }

    node->CountSubtrees(node);
    UpdateSubtreesSizes(node->LSon);
    UpdateSubtreesSizes(node->RSon);
}

void BinaryTree::UpdateInfo() {
    UpdateSubtreesSizes(Root);
    UpdateSubtreesHeights(Root);
}

void BinaryTree::CountSpecialKeys(Node* node, std::vector<int>& v) {
    if (node == NULL) {
        return;
    }

    if (node->LSon != NULL && node->RSon != NULL) {
        if (node->LHeight == node->RHeight && node->LSize != node->RSize) {
            v.push_back(node->Info);
        }
    }
    CountSpecialKeys(node->LSon, v);
    CountSpecialKeys(node->RSon, v);
}

BinaryTree::Node* BinaryTree::GetRoot() {
    return Root;
}

BinaryTree::Node* BinaryTree::FindMax(Node* x) {
    if (x == NULL || x->RSon == NULL) {
        return x;
    }
    return FindMax(x->RSon);
}

BinaryTree::Node* BinaryTree::FindMin(Node* x) {
    if (x == NULL || x->LSon == NULL) {
        return x;
    }
    return FindMin(x->LSon);
}

BinaryTree::Node* BinaryTree::Successor(const int value) {
    Node* Current = Root;
    Node* SuccessorEl = NULL;
    while (Current != NULL) {
        if (value < Current->Info) {
            SuccessorEl = Current;
            Current = Current->LSon;
        } else {
            Current = Current->RSon;
        }
    }
    return SuccessorEl;
}

std::ifstream in("in.txt");
std::ofstream out("out.txt");

void Print(const int v) {
    out << v << std::endl;
}

int main() {
    int key;

    BinaryTree* bst = new BinaryTree();
    while (in >> key) {
        bst->Insert(bst->GetRoot(), key);
    }
    in.close();

    bst->UpdateInfo();
    std::vector<int> v_keys;
    bst->CountSpecialKeys(bst->GetRoot(), v_keys);
    if (v_keys.size() % 2 != 0) {
        std::sort(v_keys.begin(), v_keys.end());
        int key_to_remove = v_keys[v_keys.size() / 2];
        bst->EraseByValue(bst->GetRoot(), key_to_remove);
    }

    bst->PreOrder(bst->GetRoot(), Print);
    out.close();

    delete bst;
    return 0;
}

