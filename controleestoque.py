print("CONTROLE DE ESTOQUE CCLIMP BOITUVA :")
print("=" * 35)
class ControleEstoque:
    def __init__(self):
        self.estoque = {}

    def adicionar_produto(self, produto, quantidade):
        if produto in self.estoque:
            self.estoque[produto] += quantidade
        else:
            self.estoque[produto] = quantidade

    def remover_produto(self, produto, quantidade):
        if produto in self.estoque:
            if quantidade <= self.estoque[produto]:
                self.estoque[produto] -= quantidade
                if self.estoque[produto] == 0:
                    del self.estoque[produto]
            else:
                print(f"Quantidade insuficiente de {produto} em estoque.")
        else:
            print(f"{produto} não encontrado em estoque.")

    def verificar_estoque(self):
        print("\nEstoque atual:")
        for produto, quantidade in self.estoque.items():
            print(f"{produto}: {quantidade} unidades")


# Exemplo de uso do ControleEstoque
controle = ControleEstoque()

# Adicionar produtos ao estoque
controle.adicionar_produto("Sabonete líquido", 15)
controle.adicionar_produto("Desinfetante", 30)
controle.adicionar_produto("Limpador de uso geral", 100)
controle.adicionar_produto("Luva P", 300)
controle.adicionar_produto("Luva G", 200)
controle.adicionar_produto("Luva M", 300)
controle.adicionar_produto("Copo descartável", 37500)
controle.adicionar_produto("Copo de água de 200ml", 912)
controle.adicionar_produto("Papel Toalha", 150)
controle.adicionar_produto("Papel Higiênico", 150)
# Verificar estoque
controle.verificar_estoque()

# Remover produtos do estoque
controle.remover_produto("Lima", 20)
controle.remover_produto("escova", 40)

# Verificar estoque novamente
controle.verificar_estoque()
