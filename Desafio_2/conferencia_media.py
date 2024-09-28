import matplotlib.pyplot as plt

while True:
    av1 = float(input("Digite a nota da AV1: "))
    av2 = float(input("Digite a nota da AV2: "))
    av3 = float(input("Digite a nota da AV3: "))
   
    media = (av1 + av2 + av3) / 3

    if media >= 6.0:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    print(f"\nA média aritmética é: {media:.2f}")
    print(f"Status: {resultado}")

    # Criar o gráfico de barras
    notas = [av1, av2, av3, media]
    labels = ['AV1', 'AV2', 'AV3', 'Média']

    # Definir as cores das barras
    cores = ['blue', 'blue', 'blue', 'red']

    plt.bar(labels, notas, color=cores)
    plt.xlabel('Avaliações')
    plt.ylabel('Notas')
    plt.title('Notas e Média')
    plt.ylim(0, 10)  
    plt.axhline(y=6, color='gray', linestyle='--')  
    plt.text(0.5, 6.1, 'Nota de Aprovação (6.0)', color='gray', ha='center')

    plt.show()

    continuar = input("Deseja calcular novamente? (s/n): ").strip().lower()
    if continuar != 's':
        break