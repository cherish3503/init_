def fib(num):
    if num == 0: 
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)


def zeckendorf(num):
    fib_arr = list()
    sum = num;

    while sum != 0:

        i = 1
        while True:
            if sum < fib(i):
                fib_arr.append(i-1)
                sum -= fib(i-1)
                break
            else:
                i += 1

    result = 0
    for i in fib_arr:
        result += fib(i-1)

    return result


print(zeckendorf(int(input())))
