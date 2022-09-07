a = float(input("Enter a number : "))
b = float(input("Enter the second number : "))

operation = input("Enter the operation : ")


if operation == "+":
    print(f"La somme de {a} et de {b} est : {a + b}")
elif operation == "-":
    print(f"La somme de {a} et de {b} est : {a - b}")
elif operation == "*":
    print(f"La multiplication de {a} avec {b} est : {a * b}")
elif operation == "/":
    if b == 0:
        print(f"Division impossible")
    else:
        print(f"La divion de {a} avec {b} est : {a / b}")
