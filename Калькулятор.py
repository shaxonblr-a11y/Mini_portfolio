while True:
    a = float(input("Введите первое число:"))
    operation= input("Введите операцию (+, - , /, *): ")
    b= float(input('Введите второе число:'))
    if operation == "+":
        result= a+b
        print('Результат:', result)
    elif operation == "-":
        result=a-b
        print('Результат:', result)
    elif operation == "/":
        result=a/b
        print('Результат:', result)
        if b==0:
            print("Ошибка деление на ноль")
        else:
            result=a/b
    elif operation== "*":
        result=a*b
        print('Результат:', result)
    else:
        print('Неизвестная операция')
    again= input('Хотите выполнить ещё одно вычисление? (да/нет):')
    if again.lower() != 'да':
        print('Калькулятор off')
        break


