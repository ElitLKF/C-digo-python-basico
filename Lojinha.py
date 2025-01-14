# Barraca
frutas = {
    1: {"nome": "Maçã", "preco": 2.50},
    2: {"nome": "Banana", "preco": 1.20},
    3: {"nome": "Laranja", "preco": 1.80},
    4: {"nome": "Morango", "preco": 3.00},
    5: {"nome": "Abacaxi", "preco": 4.50},
}

def exibir_menu():
    print("\nSalve meu bom deseja algo?!")
    print("ID | Fruta     | Preço")
    print("-----------------------")
    for id, fruta in frutas.items():
        print(f"{id:<3}| {fruta['nome']:<10}| R$ {fruta['preco']:.2f}")
    print("-----------------------")

def main():
    exibir_menu()
    carrinho = []
    
    while True:
        try:
            escolha = int(input("Digite o ID da fruta que deseja comprar (ou 0 para finalizar): "))
            
            if escolha == 0:
                break
            if escolha not in frutas:
                print("ID inválido! Tente novamente.")
                continue
            
            quantidade = int(input(f"Quantas unidades de {frutas[escolha]['nome']} você deseja? "))
            if quantidade <= 0:
                print("A quantidade deve ser maior que 0!")
                continue
            
            carrinho.append({"fruta": frutas[escolha]['nome'], 
                             "quantidade": quantidade, 
                             "total": quantidade * frutas[escolha]['preco']})
            
            print(f"{quantidade} unidade(s) de {frutas[escolha]['nome']} adicionada(s) ao carrinho!")
        
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    if not carrinho:
        print("Seu carrinho está vazio! Volte sempre!")
    else:
        print("\nResumo da Compra:")
        total_compra = 0
        for item in carrinho:
            print(f"{item['quantidade']}x {item['fruta']} - R$ {item['total']:.2f}")
            total_compra += item['total']
        print(f"\nTotal a pagar: R$ {total_compra:.2f}")
        print("Obrigado por comprar conosco!")

if __name__ == "__main__":
    main()
