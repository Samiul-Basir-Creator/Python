dec = int(input("Enter decimal number : "))

octal = "{0:o}".format(dec)
hexadecimal = "{0:x}".format(dec)
binary ="{0:b}".format(dec)

print("Octal : ",octal)
print("Hexadecimal : ",hexadecimal)
print("Binary : ",binary)