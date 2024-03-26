# assignment: programming assignment 4
# author: Fiona Leung
# date: 2/28/2023
# file: calculator.py
# input: takes in user input in the form of string (infix expression or q/quit)
# output: calculates the given expression and returns/prints the evaluated expression

# DO NOT FORGET TO ADD COMMENTS!!!

from stack import Stack
from tree import BinaryTree, ExpTree

def infix_to_postfix(infix):
    postfix = ""
    num = ""
    s = Stack()
    # PEDMAS, ^/*+-
    order = {"^":5, "/":4, "*":3, "+":2, "-":1, None: 0}
    for char in infix:

        # check if the character is a number, if char is an integer or "."" then append it to num
        if char.isdigit() or char == ".":
            num += char 
        
        elif not(char.isdigit()) or char != ".":
            postfix += num 
            num = ""

        if char == "(":
            s.push(char)
    
        # if closing parentheses detected, pop until peek == "(", then remove "(" 
        elif char == ")":
            while s.peek() != "(":
                postfix += " " + s.peek()
                s.pop()
            # remove opening parentheses
            s.pop()

        # first check if the char is an operator or None, stack is not empty, and head is not (, if all conditions are met then:
        # if the operator in the stack has a higher rank than the char operator, pop out the 
        # higher one and then add the char
        # if the operator in the stack has a lower rank than the char operator, just add onto the stack
        elif char in order:   
            if s.peek() == "(":
                s.push(char)
                postfix += " "
            elif s.isEmpty() == False:

                if (order[char] < order[s.peek()]):  
                    postfix += " " + s.peek()      
                    s.pop()
                    s.push(char)
                    postfix += " "
                else:
                    s.push(char)
                    postfix += " "
            else:
                s.push(char)
                postfix += " "



        # for testing
        # print (f'peek: {s.peek()} type: {type(s.peek())} items: {s.items} char: {char} postfix: {postfix}')

    # for testing
    # print (f'remaining: {s.items}')

    # remove remaining items
    postfix += num

    if s.isEmpty() == False:
        postfix += " "
        while s.size() != 0:
            postfix += s.peek() + " "
            s.pop()
    return(postfix.strip())

def calculate(infix):
    postfix = infix_to_postfix(infix)
    postfix_split = postfix.split()
    tree = ExpTree.make_tree(postfix_split)
    evaluate = ExpTree.evaluate(tree)
    return (evaluate)
    
# a driver to test calculate module

if __name__ == '__main__':
    # test infix_to_postfix function
    result = infix_to_postfix('2*(3+4)')
    print (f'infix to postfix: {result}')
    # assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    # assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0

    print ("Welcome to Calculator Program! ")
    while True:
        expression = input("Please enter your expression here. To quit enter 'quit' or 'q':\n")
        if expression == "q" or expression == "quit":
            print ("Goodbye!")
            break
        else:
            print (calculate(expression))