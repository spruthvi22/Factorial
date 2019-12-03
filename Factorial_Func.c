/*
* Author:Pruthvi Suryadevara
* Email: pruthvi.suryadevara@tifr.res.in
* Description: C function to find factorial of a number
*/


#include<stdio.h>
#include<stdlib.h>
#include"Factorial_Func.h"

long double factorial(unsigned int n)
{
  long double fac;
  if(n!=0)
    {
      fac=n*factorial(n-1);  // Calling the function recursively
    }else
    {
      fac=1;
    }
  return(fac);
}
