print("CONTRLOLE DE ESTOQUE")
print("=-" * 10)
class ControleEstoque:
    def __init__(self):
        self.estoque = {}

    def adicionar_item(self, item, quantidade):
        if item in self.estoque:
            self.estoque[item] += quantidade
        else:
            self.estoque[item] = quantidade

    def dar_baixa_item(self, item, quantidade):
        if item in self.estoque:
            if quantidade <= self.estoque[item]:
                self.estoque[item] -= quantidade
                print(f"Obs: {quantidade} unidades do {item} deram baixa no estoque.")
            else:
                print(f"Quantidade insuficiente em estoque do item {item}. Necessário solicitação de compra.")
        else:
            print(f"Item não encontrado no estoque do item {item}.")

    def exibir_estoque(self):
        print("Estoque atual:")
        for item, quantidade in self.estoque.items():
            print(f"{item}: {quantidade} unidades")

# Lista de itens do estoque com quantidades antes da baixa :
controle_estoque = ControleEstoque()

controle_estoque.adicionar_item("Sabonete líquido", 0)
controle_estoque.adicionar_item("Desinfetante", 0)
controle_estoque.adicionar_item("Limpador de uso geral", 10)
controle_estoque.adicionar_item("Luva 'P'", 0)
controle_estoque.adicionar_item("Luva 'M'", 2)
controle_estoque.adicionar_item("Luva 'G'", 2)
controle_estoque.adicionar_item("Copo descartável", 10000)
controle_estoque.adicionar_item("Copo de água de 200ml", 528)
controle_estoque.adicionar_item("Papel Toalha", 48)
controle_estoque.adicionar_item("Papel Higiênico", 2)
controle_estoque.adicionar_item("Pano listrado", 60)
controle_estoque.adicionar_item("Saco p/ lixo de 20 litros", 250)
controle_estoque.adicionar_item("Saco p/ lixo de 60 litros", 300)
controle_estoque.adicionar_item("Saco p/ lixo de 100 litro", 200)
controle_estoque.adicionar_item("Porta copos", 20)
controle_estoque.adicionar_item("Galão de água de 20 litros", 10)
controle_estoque.adicionar_item("Água garrafinha", 312)
controle_estoque.adicionar_item("Sapato de segurança feminino Nº 34", 1)
controle_estoque.adicionar_item("Sapato de segurança feminino Nº 35", 3)
controle_estoque.adicionar_item("Sapato de segurança feminino Nº 36", 4)
controle_estoque.adicionar_item("Sapato de segurança feminino Nº 37", 2)
controle_estoque.adicionar_item("Sapato de segurança feminino Nº 38", 1)
controle_estoque.adicionar_item("Sapato de segurança feminino Nº 39", 1)
controle_estoque.adicionar_item("Sapato de segurança feminino Nº 40", 2)

controle_estoque.exibir_estoque()
# Lista de itens após a baixa no estoque:

controle_estoque.dar_baixa_item("Sabonete líquido", 1)
controle_estoque.dar_baixa_item("Desinfetante",2)
controle_estoque.dar_baixa_item("Limpador de uso geral", 1)
controle_estoque.dar_baixa_item("Luva 'P'", 1)
controle_estoque.dar_baixa_item("Sapato de segurança feminino Nº 34", 1)
controle_estoque.dar_baixa_item("Papel Higiênico", 1)

controle_estoque.exibir_estoque()
