print("CONTROLE DE ESTOQUE DE PRODUTOS CCLIMP BOITUVA :")
print("Local: Delorenzi - Boituva")
print("Responsáveis : Reginaldo Trivinho e Luiz Gonzaga Moreira")
print("=" * 56)

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
            mensagem = f"{produto}: {quantidade} unidades"
            if quantidade <= 10:
                mensagem += " (Estoque insuficiente. Atenção - Necessário solicitação de compra.) "
            print(mensagem)


# Exemplo de uso do ControleEstoque
controle = ControleEstoque()

# Adicionar produtos ao estoque
controle.adicionar_produto("_Sabonete líquido", 3)
controle.adicionar_produto("_Desinfetante", 30)
controle.adicionar_produto("_Limpador de uso geral", 10)
controle.adicionar_produto("_Luva P", 2)
controle.adicionar_produto("_Luva M", 2)
controle.adicionar_produto("_Luva G", 2)
controle.adicionar_produto("_Copo descartável", 37500)
controle.adicionar_produto("_Copo de água de 200ml", 912)
controle.adicionar_produto("_Papel Toalha", 48)
controle.adicionar_produto("_Papel Higiênico", 0)
controle.adicionar_produto("_Pano listrado", 30)
controle.adicionar_produto("_Saco p/ lixo de 20 litros", 250)
controle.adicionar_produto("_Saco p/ lixo de 60 litros", 300)
controle.adicionar_produto("_Saco p/ lixo de 100 litro", 200)
controle.adicionar_produto("_Porta copos", 20)
controle.adicionar_produto("_Galão de água de 20 litros", 10)
controle.adicionar_produto("_Água garrafinha", 252)
# Verificar estoque
controle.verificar_estoque()

# Remover produtos do estoque
controle.remover_produto("Lima :", 20)
controle.remover_produto("escova:", 40)

# Verificar estoque novamente
controle.verificar_estoque()
