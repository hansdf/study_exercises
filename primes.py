import math

def calculatePrimeNumbers(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def main():
    num = int(input())
    primes = []
    for i in range(2, num + 1):
        if calculatePrimeNumbers(i):
            primes.append(i)
    return primes

if __name__ == "__main__":
    prime_numbers = main()
    print(" ".join(map(str, prime_numbers)))