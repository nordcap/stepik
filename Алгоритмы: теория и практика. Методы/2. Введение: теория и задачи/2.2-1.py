"""Дано целое число 1≤n≤401≤n≤40, необходимо вычислить n-е число Фибоначчи
(напомним, что F0=0, F1=1 и Fn=Fn−1+Fn−2Fn=Fn−1+Fn−2 при n≥2n≥2).

Sample Input:
3
Sample Output:
2
"""


def fib(n):
    if n == 0 or n == 1:
        return n
    list_fib = [0 for n in range(n + 1)]
    list_fib[0] = 0
    list_fib[1] = 1
    i = 2
    col = len(list_fib)
    while i < col:
        list_fib[i] = list_fib[i - 1] + list_fib[i - 2]
        i += 1
    return list_fib[col - 1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == '__main__':
    main()
