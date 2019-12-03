/*
* Author:Pruthvi Suryadevara
* Email: pruthvi.suryadevara@tifr.res.in
* Description: Find factroial of an number
* Compiled Output: Factorial.out
*/


#include<stdio.h>
#include<stdlib.h>
#include"Factorial_Func.h"
#include<time.h>

int main()
{
  unsigned int n=22; // We can get a accurate result till n=22, after which the round off errors start comming up
  clock_t start_time = clock(); // Notes the start time of the function
  double fac=factorial(n);
  clock_t end_time = clock();  // Notes the end time fo the fucntion
  double time_spent = (double)(end_time-start_time) / CLOCKS_PER_SEC;
  printf("factorial = %f \n",fac);
  printf("time = %f",time_spent);
}
