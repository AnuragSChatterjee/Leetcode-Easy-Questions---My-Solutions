#include <stdio.h>
#include <string.h>

int romantointeger(char S)
{
	if (S == 'I')
		return 1;
	if (S == 'V')
		return 5;
	if (S == 'X')
		return 10;
	if (S == 'L')
		return 50;
	if (S == 'C')
		return 100;
	if (S == 'D')
		return 500;
	if (S == 'M')
		return 1000;

	return -1;
}


int romanToDecimal(char str[])
{
	int output = 0;

	for (int i = 0; i < strlen(str); i++)
	{
		// Getting value of symbol s[i]
		int current_value = romantointeger(str[i]);

		if (i + 1 < strlen(str))
		{
			// Getting value of symbol s[i+1]
			int next_value = romantointeger(str[i + 1]);

			// Comparing both values
			if (current_value >= next_value)
			{
				output += current_value;
				i++;
			}

			else
			{
				// Value of current symbol is
				// less than the next symbol
				output += next_value - current_value;
				i++;
			}
		}
		else {
			output += current_value;
		}
	}
	return res;
}
 
// Driver Code
int main()
{
	// Considering inputs given are valid
	char str[10] = "MCMIV";
	printf("Integer form of Roman Numeral is %d",romanToDecimal(str));


	return 0;
}
