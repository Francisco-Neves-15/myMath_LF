from myMathLF import mySqrt
import numpy as np

def startI_Simple():
    print("= Start: Simple Interest =\n")

    try:
        # Entrada do Capital Inicial
        print("Entry with Starting Capital:")
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
        return f'{interest:.2f}', f'{finalAmount:.2f}'

    except ValueError:
        print("Invalid input. Please restart the program and enter numerical values where required.")
        return None

def startI_Compound():
    print("= Start: Simple Compound =\n")

    try:
        # Entrada do Capital Inicial
        print("Entry with Starting Capital:")
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

        # Cálculo dos Juros Composto
        montant = startCap * (1 + interstRate)**time
        interest = montant - startCap
        finalAmount = montant
        return f'{interest:.2f}', f'{finalAmount:.2f}'

    except ValueError:
        print("Invalid input. Please restart the program and enter numerical values where required.")
        return None

def startI_Nominal():
    print("= Start: Nominal Interest =\n")

    try:
        # Entrada da Taxa de Juros
        while True:
            print("Entry with Nominal rate (Annual nominal rate, e.g., 12%):")
            nominalRate = input("→ ").strip()
            if "%" in nominalRate:  # Verifica se o usuário usou o símbolo %
                nominalRate = float(nominalRate.replace("%", "").strip()) / 100
                break
            else:
                try:
                    nominalRate = float(nominalRate)
                    if 0 <= nominalRate <= 1:  # Verifica se já está em decimal
                        break
                    else:
                        print("Invalid value. Please enter a valid percentage (e.g., 5%) or decimal (e.g., 0.05).")
                except ValueError:
                    print("Invalid input. Try again.")
        
        # Entrada do Número de Capitalizações
        print("Entry with Periodic Capitalization (e.g., Monthly capitalization (n=12)): ")
        nValue = float(input("→ "))

        # Cálculo dos Juros Efetivos
        effectiveInterest = (1 + (nominalRate / nValue))**nValue - 1
        eInterestPerc = effectiveInterest * 100

        return f"{eInterestPerc:.2f}%"

    except ValueError:
        print("Invalid input. Please restart the program and enter numerical values where required.")
        return None

def startI_Revolving():
    print("= Start: Simple Revolving =\n")

    # Entrada do Saldo devolver
    print("Debit balance: ")
    debitBalance = float(input("→ "))

    try:
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
        print("Entry with Time (in periods corresponding to the rate, e.g., 5% per month, enter: 1):")
        time = float(input("→ "))

        # Cálculo dos Juros Efetivos
        interest = debitBalance * interstRate * time
        finalAmount = debitBalance + interest

        return f"{interest:.2f}", f"{finalAmount:.2f}"

    except ValueError:
        print("Invalid input. Please restart the program and enter numerical values where required.")
        return None

def main():
    print("\n\n\n\n=== Interest Calculator ===")
    while True:
        try:
            print("\nWhat Interest do you want to calculate?")
            print("\n1. Simple Interest\n2. Compound Interest\n3. Nominal Interest\n4. Revolving Interest")
            entry = int(input("→ "))
            if entry == 1:
                interest, finalAmount = startI_Simple()
                print(f"Simple Interest Calculated: {interest}")
                print(f"Final Amount: {finalAmount}")
                break
            if entry == 2:
                interest, finalAmount = startI_Compound()
                print(f"Compound Interest Calculated: {interest}")
                print(f"Final Amount: {finalAmount}")
                break
            if entry == 3:
                eInterestPerc = startI_Nominal()
                print(f"Calculated effective interest: {eInterestPerc}")
                break
            if entry == 4:
                interest, finalAmount = startI_Revolving()
                print(f"Revolving Interest Calculated: {interest}")
                print(f"Final Amount: {finalAmount}")
                break
            else:
                print("❗ Type a valid option.")
                continue
        except ValueError:
            print("❗ Type a number.")
            continue

if __name__ == "__main__":
    main()