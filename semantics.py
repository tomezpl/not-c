# Author : Macauley Scullion
# Interpreter version

#Import symtable functions
import symtable
import errorhandling


# Class defintion - will be removed, require by syntax and functions can simply be imported and called

class Node: 
    #def __init__(self, type, value, lhn = None, rhn = None):
     #   self.catagory = None
      #  self.type = type
       # self.value = value
        #self.lhn = lhn
        #self.rhn = rhn

    def __init__( self,catagory, type, value= None, lhn = None, rhn = None):
        self.catagory = catagory
        self.type = type
        self.value = value
        self.lhn = lhn
        self.rhn = rhn
    
    def PrintTree(self,i = 0): #tree print function
        print(self.type , " - \'" , self.value, "\'")
        if self.lhn != None : 
            print(i* " ", "L: ", end = '')
            self.lhn.PrintTree(i+1)
        if self.rhn != None : 
            print(i* " ", "R: ", end = '')
            self.rhn.PrintTree(i+1)


# Node evaluation function - will evaluate the root node or passed node through a swither and call function
def eval(node):
    switcher = {
        "equal": equal,
        "addition": add,
        "subtraction": sub,
        "multiply": mult,
        "divide": div,
        "variable": var,
        "constant": const
        }
    function = switcher[node.type]
    return function(node)

# Equal function - evals right side, assigns left return value from right eval
def equal(node):
    l = symtable.lookup(node.lhn.value) 
    r = eval(node.rhn)
    type_check_assign(node)
    symtable.set_attribute(l, r)
    return

# Add function - returns left and right addition
def add(node):
    l = eval(node.lhn)
    r = eval(node.rhn)
    type_check_sum(l, r)
    return l + r

# Sub function - returns left and right subtraction 
def sub(node):
    l = eval(node.lhn)
    r = eval(node.rhn)
    type_check_sum(l, r)
    return l - r

# mult function - returns left and right multiplication 
def mult(node):
    l = eval(node.lhn)
    r = eval(node.rhn)
    type_check_sum(l, r)
    return l * r

# div function - returns left and right division
def div(node):
    l = eval(node.lhn)
    r = eval(node.rhn)
    type_check_sum(l, r)
    return l / r

# var function - returns variable value after lookup 
def var(node):
    var = symtable.lookup(node.value)
    return var.value

# const function - returns the constant i.e. its name
def const(node):
    return node.value

# Type checking function - will check if the variables/constants being summed are of the same type
def type_check_sum(leftnode, rightnode):  
    if (isinstance(leftnode,int) and isinstance(rightnode,int)):
        return

    else:
        errorhandling.errornodetype(1)

# Type checking function - will check if the variables/constants being assigned are of the same type
def type_check_assign(node):  
    # Only if left handside is a variable otherwise run an error
    if (node.lhn.type == 'variable'):
        # if left and right both return a symbol, match types otherwise run error
        if (symtable.lookup(node.lhn.value) != False and symtable.lookup(node.rhn.value) != False):
            if ((symtable.lookup(node.lhn.value)).type == 'Int' and (symtable.lookup(node.rhn.value)).type == 'Int'):
                return

            elif ((symtable.lookup(node.lhn.value)).type == 'Str' and (symtable.lookup(node.rhn.value)).type == 'Str'):
                return

            else: 
                errorhandling.errornodetype(node)

        # if left returns a symbol and right is a constant, match types otherwise run error
        elif (symtable.lookup(node.lhn.value) != False and node.rhn.type == 'constant'):
            if ((symtable.lookup(node.lhn.value)).type == 'Int' and isinstance(node.rhn.value, int)):
                return
            
            elif ((symtable.lookup(node.lhn.value)).type == 'Str' and isinstance(node.rhn.value, str)):
                return

            else: 
                errorhandling.errornodetype(node)

    else:
        errorhandling.errornodetype(node)

    ## Test node eval code - will have to remove all code from file to test - PLEASE DO THIS IN A SEPERATE FILE
    #symtable.insert("X", "Int", 5)
    #nodel = Node("variable", "X")
    #noder = Node("constant", 5)
    #root = Node("divide", "+", nodel, noder)
    #print(eval(root))
    #symtable.printTable()

    #symtable.insert("X", "Int", 5)
    #symtable.insert("Y", "Int", 5)
    #nodel = Node("variable", "X")
    #noder = Node("variable", "Y")
    #root = Node("multiply", "+", noder, nodel)
    #print(eval(root))

    #symtable.insert("X", "Int", 0)
    #symtable.insert("y", "Str", 6)
    #symtable.printTable()
    #nodel = Node("variable", "X")
    #noder = Node("variable", "y")
    #root = Node("equal", "+", nodel, noder)
    #print(eval(root))
    #symtable.printTable()

    def const(node):
        return node.char



