while True:
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    calculate = input('''
Please select the math operation:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
    
    if calculate == '+':
        print(f'{number1} + {number2} = '+ str(number1 + number2))
        print("Do you want to continue? Please type 'y' or 'n'")
        if input().lower() == 'y':
            continue
        elif input().lower() == 'n':
            break
        else:
            print('please try again')
        

    elif calculate == '-':
        print(f'{number1} - {number2} = ' + str(number1 - number2))
        print("Do you want to continue? Please type 'y' or 'n'")
        if input().lower() == 'y':
            continue
        elif input().lower() == 'n':
            break
        else:
            print('please try again')

    elif calculate == '*':
        print(f'{number1} * {number2} = '+ str(number1 * number2))
        print("Do you want to continue? Please type 'y' or 'n'")
        if input().lower() == 'y':
            continue
        elif input().lower() == 'n':
            break
        else:
            print('please try again')

    elif calculate == '/':
        print(f'{number1} / {number2} = '+ str(number1 / number2))


        print("Do you want to continue? Please type 'y' or 'n'")
        if input().lower() == 'y':
            continue
        elif input().lower() == 'n':
            break
        else:
            print('please try again')
        
    else:
        print('You have not typed a valid operator, please run the program again.')
        

calculate()
