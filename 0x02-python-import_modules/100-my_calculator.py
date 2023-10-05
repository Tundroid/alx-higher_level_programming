#!/usr/bin/python3
if __name__ == "__main__":
    import sys, calculator_1 as calc
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)
    op = sys.argv[2]
    if op not in {'+', '-', '*', '/'}:
        print("Unknown operator. Available operators: +, -, * and /")
        exit (1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    res = 0
    if op == '+':
        res = calc.add(a, b)
    elif op == '-':
        res = calc.sub(a, b)
    elif op == '*':
        res = calc.mul(a, b)
    elif op == '/':
        res = calc.div(a, b)
    print("{} {} {} = {}".format(a, op, b, res))
