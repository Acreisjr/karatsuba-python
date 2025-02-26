def karatsuba(x: int, y: int) -> int:
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    high1, low1 = divmod(x, 10**half)
    high2, low2 = divmod(y, 10**half)

    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return (z2 * 10**(2 * half)) + ((z1 - z2 - z0) * 10**half) + z0

def main():
    try:
        x = int(input("Digite o primeiro número inteiro: "))
        y = int(input("Digite o segundo número inteiro: "))
    except ValueError:
        print("Por favor, insira apenas números inteiros.")
        return

    resultado = karatsuba(x, y)
    print(f"O resultado da multiplicação entre {x} e {y} é: {resultado}")

if __name__ == "__main__":
    main()
