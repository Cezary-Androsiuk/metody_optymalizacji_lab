# python -m venv env
# env\Scripts\activate
# where pip

import sympy as sp
from typing import List

# symbols = ['x', 'y']
# raw_function = 'x*x + y*y'
# raw_limits = ['2*x + y - 2']

symbols = ['x', 'y', 'h']
raw_function = 'x * y * h'
raw_limits = ['6 - x - y - h']

# (𝑥 + 𝑦 + ℎ = 6) == (𝑥 + 𝑦 + ℎ − 6 = 0)
# i
# (𝑥 + 𝑦 + ℎ = 6) == (0 = 6 − 𝑥 − 𝑦 − ℎ)
# ale
# (0 = 6 − 𝑥 − 𝑦 − ℎ) != (𝑥 + 𝑦 + ℎ − 6 = 0)
# dlaczego ??

print("initial data:")
# make variables
variables = []
for sym in symbols:
    variables.append(sp.symbols(sym))
print(f"declared variables: {variables}")

# make expression from function string
tmp_expression = sp.simplify(raw_function)
func_variables = tmp_expression.free_symbols
if len(tmp_expression.free_symbols) != len(variables):
    print(f"declared varaiables count {len(variables)} is not equal to function variables {len(tmp_expression.free_symbols)}")
    exit(1)
for func_var, var in zip(func_variables, variables):
    tmp_expression.subs(func_var, var)
function = tmp_expression
print(f"declared function: {function}")

# make expressions from limits strings
limits = []
for raw_limit in raw_limits:
    tmp_expression = sp.simplify(raw_limit)
    limit_variables = tmp_expression.free_symbols
    if len(tmp_expression.free_symbols) != len(variables):
        print(f"declared varaiables count {variables} is not equal to limit variables {tmp_expression.free_symbols}")
        exit(1)
    for func_var, var in zip(limit_variables, variables):
        tmp_expression.subs(func_var, var)
    limits.append(tmp_expression)
print(f"declared limits: {limits}")

print("\n")
print("internal data:")
# create lambdas
lambdas = []
for i in range(len(limits)):
    lambdas.append(sp.symbols(f'lambda_{i}'))
print(f"lambdas: {lambdas}")

# build L function
L = function
for i in range(len(limits)):
    L += lambdas[i] * limits[i]
print(f"L function: {L}")

# combine all variables of L function
L_variables = []
L_variables.extend(variables)
L_variables.extend(lambdas)
print(f"all L arguments: {L_variables}")

# make all derivatives
dL_d = []
for var in L_variables:
    dL_d.append(sp.diff(L, var))
print(f"all derivatives: {dL_d}")

# solve equation
solutions = sp.solve(dL_d, L_variables)

print("\n")
print("final results:")
print("variables:",L_variables)
print("solutions:",solutions)
