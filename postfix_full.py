#declaring the precedence order in the form of list of operators
l1 = ['^']
l2 = ['!']
l3 = ['*','/','%']
l4 = ['+','-']
l5 = ['<','<=','>','>=']
l6 = ['==','!=']
l7 = ['AND','and','&&']
l8 = ['OR','or','||']

#creating a super-set list of the operators available as of now
TL = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8
print(TL)

#function defined to check for oprtator v/s operand (function will be used later)
def is_operator(x):
    if x in TL:
        return True
    else:
        return False

#function defined to check for precedence of operators (function will be used later)
def precedence(x):
    if x in l1:
        return 8 
    elif x in l2:
        return 7
    elif x in l3:
        return 6
    elif x in l4:
        return 5
    elif x in l5:
        return 4
    elif x in l6:
        return 3
    elif x in l7:
        return 2
    elif x in l8:
        return 1

#defining operations for each operator
op = {'^':lambda x,y: x**y,
        '*':lambda x,y: x*y,
        '/':lambda x,y: x/y,
        '%':lambda x,y: x%y,
        '+':lambda x,y: x+y,
        '-':lambda x,y: x-y,
        '<':lambda x,y: x<y,
        '<=':lambda x,y: x<=y,
        '>':lambda x,y: x>y,
        '>=':lambda x,y: x>=y}

#defining the formation of the stack for the postfix expression
def solve(x,y):
    stack = []
    top = -1
    for i in x:
        solve = []
        if i.isalnum() == True:
            c = y[i]
            stack.append(c)
            top = top +1
        elif is_operator(i) == True:
            if i not in l2:
                j = 0
                while j<2:
                    z = stack.pop()
                    j = j+1
                    solve.append(z)
                    top = top -1
            elif i in l2:
                z = stack.pop()

            a = op[i](solve[1],solve[0])
            stack.append(a)
    return stack

#taking the input equation from the user 
a = str(input("Enter your algebraic equation: "))
#to dissolve it into desirable form
x = '(' + a + ')'
ans = []
stack = []
top = -1
l = len(x)
k = 0
#looping and forming the postfix expression 
for i in x:
    if i == '(':
        stack.append(i)
        top = top +1
        k = k+1
    elif i.isalnum() ==  True:
        ans.append(i)
        k = k+1
    elif is_operator(i) == True:
        k = k+1
        if stack[top] == '(':
            stack.append(i)
            top = top+1
        elif is_operator(stack[top]) == True:
            while True:
                if is_operator(stack[top]) == True:
                    if precedence(stack[top]) >= precedence(i):
                        y = stack.pop(top)
                        top =  top -1
                        ans.append(y)
                        y = ''
                    elif precedence(stack[top])< precedence(i):
                        stack.append(i)
                        top = top + 1
                        break
                    if stack[top]=='(':
                        stack.append(i)
                        top = top+1
                        break
                elif is_operator(stack[top]) == False:
                    break
    elif i == ')':
        k = k+1
        while True:
            if stack[top] != '(':
                z = stack.pop()
                top = top -1
                ans.append(z)
            elif stack[top] == '(':
                stack.pop()
                top = top -1
                break
    elif k == l-1:
        break

b = ""
for h in ans:
    b = b + h
print("Postfix expression of your algebraic equation is:", b)
val = []
values = {}

#looping and taking input values for variables present in the equation
for j in b:
    if j.isalpha()==True:
        if j in val:
            continue
        elif j not in val:
            val.append(j)
    elif j.isalnum()==True:
        if j in val:
            continue
        elif j not in val:
            m = int(j)
            values[j] = m
for key in val:
    u = int(input("Enter value of " +key+":"))
    values[key] = u
print(values)

#finally solving the postfix expression and solving the equation provided
print(solve(b,values))


            
            
                    
        




       

