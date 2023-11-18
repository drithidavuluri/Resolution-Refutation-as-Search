import sympy
import time

def convert_to_cnf(formula):
    """
    This function takes a formula as input and returns its CNF.
    """
    
    # Parse the formula
    parsed_formula = sympy.sympify(formula)
    #print("Parsed formula: {}".format(parsed_formula))

    # Convert to CNF
    cnf = sympy.to_cnf(parsed_formula)

    return cnf

def precedence(op):
    if op == '>':
        return 1
    elif op == '=':
        return 2
    elif op == '&':
        return 3
    elif op == '|':
        return 4
    elif op == '!':
        return 5
    else:
        return 0

def parse_formula(string):
    val=[]
    op=[]
    i=0
    while i<len(string):
        if string[i]==" ":
            i+=1
            continue
        elif string[i]=='(':
            op.append(string[i])
        elif string[i].isalpha():
            variable = ''
            while i < len(string) and string[i].isalpha():
                variable += string[i]
                i += 1
            val.append(sympy.Symbol(variable))
            i-=1
        elif string[i]==')':
            while len(op)!=0 and op[-1]!='(':
                if op[-1] != '!':
                    val2=val.pop()
                    val1=val.pop()
                    op1=op.pop()
                    if op1 == '>':
                        val.append(sympy.Implies(val1, val2))
                    elif op1 == '=':
                        val.append(sympy.Equivalent(val1, val2))
                    elif op1 == '&':
                        val.append(sympy.And(val1, val2))
                    elif op1 == '|':
                        val.append(sympy.Or(val1, val2))
                else:
                    val1=val.pop()
                    op1=op.pop()
                    val.append(sympy.Not(val1))
            op.pop()
        else:
            while len(op)!=0 and precedence(op[-1])>=precedence(string[i]):
                if op[-1] != '!':
                    val2=val.pop()
                    val1=val.pop()
                    op1=op.pop()
                    if op1 == '>':
                        val.append(sympy.Implies(val1, val2))
                    elif op1 == '=':
                        val.append(sympy.Equivalent(val1, val2))
                    elif op1 == '&':
                        val.append(sympy.And(val1, val2))
                    elif op1 == '|':
                        val.append(sympy.Or(val1, val2))
                else:
                    val1=val.pop()
                    op1=op.pop()
                    val.append(sympy.Not(val1))

            op.append(string[i])
        i+=1
    while len(op)!=0:
        if op[-1] != '!':
            val2=val.pop()
            val1=val.pop()
            op1=op.pop()
            if op1 == '>':
                val.append(sympy.Implies(val1, val2))
            elif op1 == '=':
                val.append(sympy.Equivalent(val1, val2))
            elif op1 == '&':
                val.append(sympy.And(val1, val2))
            elif op1 == '|':
                val.append(sympy.Or(val1, val2))
        else:
            val1=val.pop()
            op1=op.pop()
            val.append(sympy.Not(val1))
    return val[0]



def flatten_and_separate(formulas):
    cnf_formulas = []

    for formula in formulas:
        # Convert each formula to CNF
        cnf_formula = convert_to_cnf(parse_formula(formula))
        cnf_formulas.append(cnf_formula)
    #print(cnf_formulas)    

    result = []
    for formula in cnf_formulas:
        # Split formulas at '&'
        if isinstance(formula, sympy.And):
            result.extend(formula.args)
        else:
            result.append(formula)

    return result

def split_at_or(formulas):
    result = []
    for formula in formulas:
        if isinstance(formula, sympy.Or):
            result.append(list(formula.args))
        else:
            result.append([formula])
    return result

def process_query(query, kb):
    
    cnf_query=convert_to_cnf(parse_formula(query))
    #print("cnf query:",cnf_query)

    negated_query = sympy.Not(cnf_query)
    #print("negated query:",negated_query)
    
    kb.append([negated_query])

    result=[]
    if isinstance(negated_query, sympy.And):
        result.extend(negated_query.args)
    else:
        result.append(negated_query)
    result2=[]
    if isinstance(negated_query, sympy.Or):
        result2.append(list(negated_query.args))
    else:
        result2.append([negated_query])    

    return kb

def is_resolvent(clause1, clause2):
    clause1_copy = clause1.copy()
    clause2_copy = clause2.copy()

    c=0
    for literal in clause1_copy[:]:
        negation = ~literal
        if negation in clause2_copy:
            clause1_copy.remove(literal)
            clause2_copy.remove(negation)
            c=1

    resolvent = clause1_copy + clause2_copy
    resolvent = list(set(resolvent))

    if c==0:
        return "not resolved"

    if c==1:
        return resolvent

def resolution(kb, max_iterations=100, print_steps=False):
    c=0
    for _ in range(max_iterations):
        l = len(kb)
        for i in range(l - 1):
            for j in range(i + 1, l):
                resolvent = is_resolvent(kb[i], kb[j])
                c=c+1
                if resolvent != "not resolved":
                    kb.append(resolvent)
                    if resolvent==[]:
                        print("Number of nodes checked=",c)
                        return 1
                    if print_steps:
                        print(f"Resolved {kb[i]} and {kb[j]} to get {resolvent}")
                        #print("updated kb:",kb)
        kb = [list(set(clause)) for clause in kb]

        # Check for empty clause
        #for clause in kb:
            #if clause == []:
                #return 1

    return 0
  

if __name__ == "__main__":
    nm=int(input())
    n=int(nm/10)
    m=nm%10
    array_size = n
    formulas = []

    for i in range(array_size):
        formula = input()
        #formula = input("Enter formula {}: ".format(i + 1))
        formulas.append(formula.strip())

    #print("Input array of formulas: {}".format(formulas))

    result_array_and = flatten_and_separate(formulas)
    #print("Flattened and separated array: {}".format(result_array_and))

    result_split_or = split_at_or(result_array_and)
    #print("Split at OR: {}".format(result_split_or))

    query=input()
    #query = input("Enter the query: ")
    result_kb = process_query(query, result_split_or)
    #print("Updated kb: {}".format(result_kb))
    start_time=time.time()
    #mode = int(input("Enter mode (0 for result, 1 for resolution steps): "))
    result = resolution(result_kb, print_steps=(m == 1))
    end_time=time.time()
    print("Run time=",end_time-start_time)
    print(result)
