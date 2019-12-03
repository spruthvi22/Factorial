"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Simple code for finding Factorial of a number using Recurssion Scipy and C-code

"""
import Factorial_Funcpy as fac
import scipy.special as sp
import time
from ctypes import c_double, c_uint, CDLL


n=4 ## Because in C any value above 25 will give a false factorial

## performing using recursion
start_time=time.time()
fact_rec=fac.factorial(n)
end_time=time.time()
print("factorial_recursion= ",fact_rec)
print("execution time recursion = ",(end_time-start_time))

## Performing using SCIPY
start_time=time.time()
fact_scpy=sp.factorial(n)
end_time=time.time()
print("factorial_scipy = ",fact_scpy)
print("execution time scipy = ",(end_time-start_time))


def factorial_c1(n):
    return(fac_cv(c_uint(n)))
    
## Performing using C DLL
fac_c=CDLL("./Factorial_Func.so")
start_time=time.time()
fac_cv=fac_c.factorial
factor=factorial_c1(n)
end_time=time.time()
print("factorial_c= ",fact_rec)
print("execution time using C = ",(end_time-start_time))


