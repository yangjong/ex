diary_exe : memo.o calendar.o main.o
	arm-linux-gnueabihf-gcc -o diary_exe memo.o calendar.o main.o

memo.o : memo.c
	arm-linux-gnueabihf-gcc -c -o memo.o memo.c

calendar.o : calendar.c
	arm-linux-gnueabihf-gcc -c -o calendar.o calendar.c

main.o : main.c
	arm-linux-gnueabihf-gcc -c -o main.o main.c

clean :
	rm *.o diary.exe 

