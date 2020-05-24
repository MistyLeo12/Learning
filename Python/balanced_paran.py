from stack import Stack

"""
Use a stack to check if a string has a balanced usage of paranthesis

(), (()), [[]], {([])} <-- Balanced
[}], }}, [({})]) <-- Not balanced

"""
def match(p1, p2):
    if p1+p2 in ["()", "{}", "[]"]:
        return True
    else:
        return False

def isBalanced(paran_string):
    s = Stack()
    index = 0
    balanced = True
    while index < len(paran_string) and balanced:
        paren = paran_string[index]
        
        if paren in "{[(":
            s.push(paren)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not match(top, paren):
                    balanced = False
        index += 1
    if s.isEmpty() and balanced:
        return True
    else:
        return False