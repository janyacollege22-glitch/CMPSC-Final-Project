# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.top is None:
            return True
        return False
        pass

    def __len__(self): 
        # YOUR CODE STARTS HERE
        return self._lenHelper(self.top)
        pass
    def _lenHelper(self,node):
        if node is None:
            return 0
        else:
            return 1 + self._lenHelper(node.next)

    def push(self,value):
        # YOUR CODE STARTS HERE
        node = Node(value)
        node.next = self.top
        self.top = node

        pass

     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

        pass

    def peek(self):
        # YOUR CODE STARTS HERE
        return self.top.value
    
        pass


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        if txt.strip().replace('.','',1).isdigit():
            return True
        
    
            pass




    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('     2 ^       4')
            '2.0 4.0 ^'
            >>> x._getPostfix('          2 ')
            '2.0'
            >>> x._getPostfix('2.1        * 5        + 3       ^ 2 +         1 +             4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2*5.34+3^2+1+4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( .5 )')
            '0.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * (           ( 5 +-3 ) ^ 2 + (1 + 4 ))')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('(2 * ( ( 5 + 3) ^ 2 + (1 + 4 )))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('((2 *((5 + 3) ^ 2 + (1 +4 ))))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2* (       -5 + 3 ) ^2+ ( 1 +4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('     2 * 5 + 3  ^ * 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5      + 3 ) ^ 2 + ( 1 +4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^  2 + ) 1 + 4 (')
            >>> x._getPostfix('2 *      5% + 3       ^ + -2 +1 +4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        def is_number(token):
            try:
                float(token)
                return True
            except:
                return False

        def tokenize(expr):
            tokens = []
            i = 0
            while i < len(expr):
                c = expr[i]

                if c == ' ':
                    i += 1
                elif c.isdigit() or c == '.':
                    num = c
                    i += 1
                    while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                        num += expr[i]
                        i += 1
                    tokens.append(num)
                elif c == '-' and (len(tokens) == 0 or tokens[-1] in "+-*/^("):
                    num = c
                    i += 1
                    while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                        num += expr[i]
                        i += 1
                    tokens.append(num)
                else:
                    tokens.append(c)
                    i += 1

            return tokens

        # precedence and associativity
        prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
        right_assoc = {'^'}

        output = []
        stack = []

        tokens = tokenize(txt)

        for token in tokens:
            if is_number(token):
                output.append(f"{float(token)}")

            elif token in prec:
                while (stack and stack[-1] in prec and
                       (prec[stack[-1]] > prec[token] or
                        (prec[stack[-1]] == prec[token] and token not in right_assoc))):
                    output.append(stack.pop())
                postfixStack.push(token)

            elif token == '(':
                postfixStack.push(token)

            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(postfixStack.pop())
                if stack:
                    postfixStack.pop()  # remove '('

        while stack:
            output.append(postfixStack.pop())

        return " ".join(output)
      
        pass


    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4        + 3 -       2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 +          3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('      4 +           3.65  - 2        / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25      * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('2-3*4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7^2^3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ((( 10 - 2*3 )) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('      8 / 4 * (3 - 2.45 * ( 4   - 2 ^ 3 )       ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 +        2 * (         5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 +         3 * (2 + ( 3.0) * ( 5^2-2 * 3 ^ ( 2 )         ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 /3 ) ) - 2 / 3^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 ++ 3+ 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 +2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 *( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( *10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('(    3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5) - 15 + 85 ( 12)') 
            >>> x.calculate
            >>> x.setExpr("( -2/6) + ( 5 ( ( 9.4 )))") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        postfix = self._getPostfix(self.__expr)
        if not postfix:
            return None

        stack = []
        tokens = postfix.split()

        for token in tokens:
            try:
                stack.append(float(token))
            except:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
                elif token == '^':
                    stack.append(a ** b)

        return stack[0] if stack else None


        pass

#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if not word:
            return False
        if not word[0].isalpha():
            return False
        for char in word[1:]:
            if not (char.isalnum()):
                return False
            
        return True

       
        pass
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        tokens = expr.split()
        result = []

        for token in tokens:
            if self._isVariable(token):
                if token not in self.states:
                    return None
                result.append(str(float(self.states[token])))
            else:
                result.append(token)

        return " ".join(result)
        pass

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        statements = self.expressions.split(';')
        result = {}

        for stmt in statements:
            stmt = stmt.strip()
            if stmt:
                if stmt.startswith('return'):
                    expr = stmt[len('return'):].strip()
                    replaced = self._replaceVariables(expr)
                    if replaced is None:
                        self.states = {}
                        return None
                    calcObj.setExpr(replaced)
                    val = calcObj.calculate
                    if val is None:
                        self.states = {}
                        return None
                    result['_return_'] = val
                elif '=' in stmt:
                    var, expr = stmt.split('=', 1)
                    var = var.strip()
                    expr = expr.strip()
                    if not self._isVariable(var):
                        self.states = {}
                        return None
                    replaced = self._replaceVariables(expr)
                    if replaced is None:
                        self.states = {}
                        return None
                    calcObj.setExpr(replaced)
                    val = calcObj.calculate
                    if val is None:
                        self.states = {}
                        return None
                    self.states[var] = float(val)
                    result[stmt] = dict(self.states)

        return result
        pass


def run_tests():
    import doctest

    # Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    doctest.run_docstring_examples(Stack, globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()