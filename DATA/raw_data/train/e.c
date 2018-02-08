#include <stdio.h>
#include <unistd.h>
//#include "system.h"

int main()
{
	long input_data1 = 0x0000000011111111;
	long input_data2 = 0x1010101010101010;
	long output_data1;
	long output_data2;

	IOWR(SDRAM_0_BASE, 0, input_data1);
	output_data1 = IORD(SDRAM_0_BASE, 0);
	printf("output data1 = %x\n", output_data1);

	IOWR(SDRAM_0_BASE + 1, 0, input_data2);
	output_data2 = IORD(SDRAM_0_BASE + 1, 0);
	printf("output data2 = %x\n", output_data2);

	return 0;
}
