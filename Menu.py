# Main menu
import os

menu = [1, 2, 3]
while 1:
    os.system('cls')
    optiona = int(input("Choose lab number:\n(0) Exit program\n(1)\n(2)\n"))
    if optiona == 0:
        os.system('cls')
        break
    if optiona == 1:
        os.system('cls')
        from Lab1 import Ex1
        from Lab1 import Ex2
        from Lab1 import Ex3
        from Lab1 import Ex4
        optionb = int(input("Choose exercise number:\n(1) Degree convertor\n(2) n!\n(3) rows\n(4) GCD\n(5)"))
        if optionb == 1:
            os.system('cls')
            cel = float(input("Enter a temperature in Celsius: "))
            print("The temperature in fahrenheit is: ", Ex1.deg(cel))
        if optionb == 2:
            os.system('cls')
            Ex2.n019()
        if optionb == 3:
            os.system('cls')
            Ex3.rows()
        if optionb == 4:
            os.system('cls')
            print("Enter two integers:")
            a, b = int(input()), int(input())
            print("gcd=", Ex4.gcd(a, b))
        if optionb != 1 and optionb != 2 and optionb != 3 and optionb != 4:
            os.system('cls')
            print("Wrong input, try again.")
    if optiona == 2:
        os.system('cls')
        from Lab2 import Ex1
        from Lab2 import Ex2
        from Lab2 import Ex3
        from Lab2 import Ex4
        from Lab2 import Ex5
        optionb = int(input("Choose exercise number:\n(1) Triangle surface area\n(2) Absolute value\n(3)"
                            " Mul 2 of 3\n(4) Class average\n(5) Root\n"))
        if optionb == 1:
            os.system('cls')
            x, y = int(input("Enter 2 legs of a right triangle:\n")), int(input())
            print("The surface area of the triangle is", Ex1.trisurf(x, y))
        if optionb == 2:
            os.system('cls')
            x = int(input("Enter an integer:"))
            print("Absolute value of", x, "is", Ex2.absolute(x))
        if optionb == 3:
            os.system('cls')
            x, y, z = int(input("Input 3 integers:\n")), int(input()), int(input())
            Ex3.mul2_3(x, y, z)
        if optionb == 4:
            os.system('cls')
            mylist = [13, 22, 53, 64, 76, 23, 199, 57, 100, 54, 96, 199, 199]  # demo list
            print("Average is", Ex4.classAvg(mylist))
        if optionb == 5:
            os.system('cls')
            x = float(input("Enter a positive integer:"))
            print("root of", x, "is", Ex5.mySqrt(x))
        if optionb != 1 and optionb != 2 and optionb != 3 and optionb != 4 and optionb != 5:
            os.system('cls')
            print("Wrong input, try again.")
    if optiona != 1 and optiona != 2 and optiona != 3:
        os.system('cls')
        print("Wrong input, try again.")
    pause = input()
print("Exiting, goodbye.")
pause = input()
