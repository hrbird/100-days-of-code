# A program that demonstrates how to handle FileNotFound 
# exceptions/errors whenever you open a file in Python.

filename = "a_file.txt"

try:
    # Try to open the given file.
    file = open(filename)

except FileNotFoundError:
    # If the file doesn't exist, create it.
    print(f"\nError: Could not find file named {filename}")
    file = open(filename, "w")
    file.write("Something")

else:
    # If the file was opened, print its contents to the console.
    print(f"\n{filename} contains:")
    print(file.read())

finally:
    # Close the file whether it successfully opened or not.
    file.close()
    print("Closed the file.")

