from Produto import Produto

resposta = input("Deseja cadastrar um produto ? ")

while resposta.lower() == "sim":
    nome = input("Qual nome do produto que deseja cadastrar ? ")
    preco = input(f"Qual preço do {nome}? ")

    produto = Produto(nome, float(preco))
    print(f'{nome} foi cadastrado com sucesso!')


    print("\n", "#"*50 ,"\n")
    resposta = input("Deseja cadastrar outro produto ? ")

print("\n", "#"*50 ,"\n")

for chave, produto in sorted(Produto.produtos.items(), key=lambda item: item[1].preco):
    print(f"{produto.nome}: R${produto.preco:.2f}")


print("\n", "#"*50 ,"\n")

print("Muito Obrigado!!!")