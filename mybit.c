#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

unsigned char swap_bits(unsigned char octet)
{
	return ((octet >> 4) | (octet << 4));
}

unsigned char	reverse_bits(unsigned char octet)
{
	int i = 7;
	unsigned char res = 0;

	while(i >= 0)
	{
		res = res << 1;
		res = res | (octet & 1);
		octet = octet >> 1;
		i--;
	}
	return(res);
}

void print_bits(unsigned char octet)
{
	int i = 7;

	while(i >= 0)
	{
		if((octet >> i) & 1)
			write(1, "1", 1);
		else
			write(1, "0", 1);
		i--;
	}
}

int main(void)
{
	printf("print_bits\n");
	print_bits(5);
	printf("\n\n");
	printf("reverse_bits\n");
	print_bits(reverse_bits(5));
	printf("\n\n");
	printf("swap_bits\n");
	print_bits(swap_bits(5));
	printf("\n\n");

	return(0);
}
