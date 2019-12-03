"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Function to Geat the Factorial

"""

def factorial(n):
    if n!=0:
        fac=n*factorial(n-1)
    else:
        fac=1;
    return fac
