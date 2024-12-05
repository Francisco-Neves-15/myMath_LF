from myMathLF import mySqrt
import numpy as np

def startI_Simple():
    print("= Start: Simple Interest =\n")

    try:
        # Entrada do Capital Inicial
        print("Entry with Starting Capital :")
        startCap = float(input("→ "))
        
        # Entrada da Taxa de Juros
        while True:
            print("Entry with Interest Rate (can be % or decimal, e.g., 5 or 0.05):")
            interstRate = input("→ ").strip()
            if "%" in interstRate:  # Verifica se o usuário usou o símbolo %
                interstRate = float(interstRate.replace("%", "").strip()) / 100
                break
            else:
                try:
                    interstRate = float(interstRate)
                    if 0 <= interstRate <= 1:  # Verifica se já está em decimal
                        break
                    else:
                        print("Invalid value. Please enter a valid percentage (e.g., 5%) or decimal (e.g., 0.05).")
                except ValueError:
                    print("Invalid input. Try again.")
        
        # Entrada do Tempo
        print("Entry with Time (in periods corresponding to the rate, e.g., 5% per year, enter: 1):")
        time = float(input("→ "))

        # Cálculo dos Juros Simples
        interest = startCap * interstRate * time
        finalAmount= startCap + interest

    except ValueError:
        print("Invalid input. Please restart the program and enter numerical values where required.")

    return f'{interest:.2f}', f'{finalAmount:.2f}'

def startI_Compound():
    print("= Start: Simple Compound =\n")

def startI_Nominal():
    print("= Start: Simple Nominal =\n")

def startI_Revolving():
    print("= Start: Simple Revolving =\n")

def main():
    print("\n\n\n\n=== Interest Calculator ===")
    while True:
        try:
            print("\nWhat Interest do you want to calculate?")
            print("\n1. Simple Interest\n2. Simple Compound\n3. Simple Nominal\n4. Simple Revolving")
            entry = int(input("→ "))
            if entry == 1:
                interest, finalAmount = startI_Simple()
                print(f"Simple Interest Calculated: {interest}")
                print(f"Final Amount: {finalAmount}")
                break
            if entry == 2:
                break
            if entry == 3:
                break
            if entry == 4:
                break
            else:
                print("❗ Type a valid option.")
                continue
        except ValueError:
            print("❗ Type a number.")
            continue

if __name__ == "__main__":
    main()