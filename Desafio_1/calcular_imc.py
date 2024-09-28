def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 25:
        return "Abaixo do peso"
    elif 25 <= imc < 30:
        return "Peso ideal"
    elif 30 <= imc < 35:
        return "Sobrepeso"
    else:
        return "Obeso"

def main():
    while True:
        try:
            peso = float(input("Digite seu peso (kg): "))
            altura = float(input("Digite sua altura (m): "))
            
            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)
            
            print(f"Seu IMC é: {imc:.2f} - Classificação: {classificacao}")
        
        except ValueError:
            print("Por favor, insira valores numéricos válidos para peso e altura.")

        continuar = input("Deseja calcular novamente? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()