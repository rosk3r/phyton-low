print("enter code")
a = input()
b = a.split(" ")
number1 = int(b[0])
action = b[1]
number2 = int(b[2])
if action == '=':
    print("=" + str(number1 + number2) + "\n")
elif action == '-':
    print("=" + str(number1 - number2) + "\n")
elif action == '/':
    print("=" + str(number1 / number2) + "\n")
elif action == '*':
    print("=" + str(number1 * number2) + "\n")
elif action == '%':
    print("=" + str(number1 % number2) + "\n")
elif action == '^':
    print("=" + str(number1 ** number2) + "\n")
else:
    print("error, pleas try again")
