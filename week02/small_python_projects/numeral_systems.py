# Counts to a given number in different numeral systems: 
# decimal (base 10), binary (base 2), hexadecimal (base 16), and octal (base 8).

def print_numbers_list(lowest_num, highest_num):
    """Prints a list of numbers in different numeral systems.
    Counts from the given lowest num to the given highest num.
    Each number is shown in decimal, hexadecimal, and binary forms.

    Args:
        lowest_num (int): the low number to start counting from
        highest_num (int): the high number to stop counting at
    """

    print(f"Numbers in different numeral systems, from {lowest_num} to {highest_num}:\n")

    print(f"{'DECIMAL':^12}|{'BINARY':^12}|{'HEXADECIMAL':^12}|{'OCTAL':^12}")
    print(f"{'(base 10)':^12}|{'(base 2)':^12}|{'(base 16)':^12}|{'(base 8)':^12}")
    sep = "~"*12
    print(f"{sep}|{sep}|{sep}|{sep}")

    for i in range(lowest_num, highest_num + 1, 1):
        dec_num = str(i)
        bin_num = bin(i)[2:]            # Convert to binary and remove "0b" prefix
        hex_num = hex(i)[2:].upper()    # Convert to hex and remove "0X" prefix
        oct_num = oct(i)[2:]            # Convert to octal and remove "0o" prefix

        # Print each formatted line, with the numbers right-aligned.
        print(f"{dec_num:>10}  |{bin_num:>10}  |{hex_num:>10}  |{oct_num:>10}")

def main():
    print_numbers_list(1, 100)

if __name__ == "__main__":
    main()