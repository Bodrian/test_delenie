def delenie_razriad(n):
    result = []
    i, num = 0, 0
    while i != int(n):
        if num % len(str(num)) == 0:
            result.append(num)
            i += 1
        num += 1
    return result

if __name__ == '__main__':
    print('Программа выводит числа, которые без остатка делятся на количество разрядов этого числа')
    n = input('Сколько чисел необходимо вывести: ')
    print(delenie_razriad(n))
