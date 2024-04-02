class Node:
    def __init__(self, ind, c):
        self.ind = ind
        self.c = c

def match_parentheses(A):
    Q = []
    B = [' ' for _ in A]
    
    for i, c in enumerate(A):
        if c == '(':
            Q.append(Node(i, c))
        elif c == ')':
            if Q and Q[-1].c == '(':
                Q.pop()
            else:
                B[i] = '?'
                continue
        B[i] = ' '
    
    while Q:
        K = Q.pop()
        B[K.ind] = 'x'
    
    return A, B

while True:
    A = input()
    if not A:
        break
    A, B = match_parentheses(A)
    print(A)
    print(''.join(B))
