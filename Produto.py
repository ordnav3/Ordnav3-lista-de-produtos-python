class Produto:
    produtos = {}

    def __init__(self,nome, preco):
        self.nome = nome
        self.preco = preco

        Produto.produtos[self.nome] = {"nome": self.nome, "preco": self.preco}
    
    def __str__(self):
        return f"Produto: {self.nome} Preço : {self.preco}"