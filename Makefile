Factorial_out: Factorial_Main.c Factorial_Func.c Factorial_Func.h
	gcc Factorial_Main.c Factorial_Func.c -o Factorial.out

clean:
	rm Factorial.out
