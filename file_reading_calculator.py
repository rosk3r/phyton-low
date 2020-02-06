read_lines = []
with open("txt.txt", "r") as file:
    for line in file:
        read_lines.append(line.rstrip())

with open("text2.txt", "w") as file:
    for line in read_lines:
        print(line)
        a = line
        b = a.split(" ")
        number1 = int(b[0])
        action = b[1]
        number2 = int(b[2])
        if action == '=':
            file.write(line + "=" + str(number1 + number2) + "\n")
        elif action == '-':
            file.write(line + "=" + str(number1 - number2) + "\n")
        elif action == '/':
            file.write(line + "=" + str(number1 / number2) + "\n")
        elif action == '*':
            file.write(line + "=" + str(number1 * number2) + "\n")
        elif action == '%':
            file.write(line + "=" + str(number1 % number2) + "\n")
        elif action == '^':
            file.write(line + "=" + str(number1 ** number2) + "\n")
        else:
            print("error, pleas try again")