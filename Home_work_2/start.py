from lib.calc import sum, minus, mult, dev

a = int(input('Enter first digin: '))
b = int(input('Enter second digin: '))

choice = int(input('Enter choice (1 - "+", 2 - "-", 3 - "*", 4 - "/", 5)'))

if choice == 1:
    res = sum(a, b)
    print(a, '+', b, '=', res)
elif choice == 2:
    res2 = minus(a, b)
    print(a, '-', b, '=', res2)
elif choice == 3:
    if b != 0:
        res3 = mult(a, b)
        print(a, '*', b, '=', res3)
    else:
        print("Error!!!")
elif choice == 4:
    if  b != 0:
        res4 = dev(a, b)
        print(a, '/', b, '=', res4) 
    else:
        print("Error!!!")
else:
    print("enter number 1 - 4")
