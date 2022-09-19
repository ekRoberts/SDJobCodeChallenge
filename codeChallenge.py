def StringReverse(word):
    return word[::-1]


def MaxInt(num1, num2, num3):
    maxNum = 0
    if num1 > num2:
        maxNum = num1
        if num1 < num3:
            maxNum = num3
    if num1 < num2:
        maxNum = num2
        if num2 < num3:
            maxNum = num3

    return maxNum


def Factorial(num):
    if num == 1:
        return 1
    else:
        y = num * Factorial(num-1)
        return y


def Fibonacci(num):
    fib = [0] * num
    if num <= 2:
        return 1
    else:
        fib[0] = 1
        fib[1] = 1

        for i in range(2, num):
            fib[i] = fib[i-1] + fib[i-2]

    return fib[num-1]



