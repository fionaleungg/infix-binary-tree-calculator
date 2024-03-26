# assignment: programming assignment 4
# author: Fiona Leung
# date: 2/28/2023
# file: tree.py
# input: takes in a postfix expression (string) or expression tree (string) or binary tree (string)
# output: expression tree (string) or postorder/inorder/preorder tree-traversed expression (string)


from stack import Stack

class BinaryTree:
    def __init__ (self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft (self, newNodeVal):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.leftChild = self.leftChild
            self.leftChild = t
            
    def insertRight (self, newNodeVal):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild (self):
        return (self.leftChild)
    
    def getRightChild (self):
        return (self.rightChild)
    
    def getRootVal(self):
        return (self.key)
    
    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s


class ExpTree(BinaryTree):
    def make_tree(postfix):
        s = Stack()
        operator = "^/*+-"
        for char in postfix:
            # if the char is a operand, push it into the stack

            if char not in operator or char.isdigit():
                s.push(ExpTree(char))
            # if the char is not a digit (is an operator), make a node with root char and make the first item in the stack its 
            # left child and second item its right child, then add it back into the stack
            else:
                temp = ExpTree(char)

                temp.rightChild = s.pop()
                temp.leftChild = s.pop()

                s.push(temp)
                
        return (s.pop())

    # left right root
    def preorder(tree):
        final = ""

        if tree != None:         
            final += str(tree.getRootVal())
            final += ExpTree.preorder(tree.getLeftChild())
            final += ExpTree.preorder(tree.getRightChild())
        
        return (final)
    
    # left root right
    def inorder(tree):
        final = ""

        if tree != None:         
            if tree.leftChild and tree.rightChild:
                final += "("
            final += ExpTree.inorder(tree.getLeftChild())
            final += str(tree.getRootVal())
            final += ExpTree.inorder(tree.getRightChild()) 
            if tree.leftChild and tree.rightChild:
                final += ")"
            
        return (final)
      
    # left right root
    def postorder(tree):
        final = ""

        if tree != None:         
            final += ExpTree.postorder(tree.getLeftChild())
            final += ExpTree.postorder(tree.getRightChild())
            final += str(tree.getRootVal())

        return str(final)
    
    def evaluate(tree):
        operator = "^/*+-"
        if tree != None:
            if (str(tree.getRootVal())).isdigit() or tree.getRootVal() not in operator:
                return (tree.getRootVal())            # base case
            else:
                left = ExpTree.evaluate(tree.getLeftChild())
                right = ExpTree.evaluate(tree.getRightChild())
                
                # EXPONENT
                if (str(tree.getRootVal())) == "^":
                    return float(left) ** float(right)
                
                # MULTIPLICATION
                elif (tree.getRootVal()) == "*":
                    return float(left) * float(right)
                
                # DIVISION
                elif (tree.getRootVal()) == "/":
                    return float(left) / float(right)
                
                # ADDITION
                elif (tree.getRootVal()) == "+":
                    return float(left) + float(right)
                
                # SUBTRACTION
                elif (tree.getRootVal()) == "-":
                    return float(left) - float(right)

            
    def __str__(self):
        return ExpTree.inorder(self)
   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    # test an ExpTree
    
    postfix = "5 2 3 * +".split()
    tree = ExpTree.make_tree(postfix)
    # print (tree)
    # print (ExpTree.evaluate(tree))

    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0