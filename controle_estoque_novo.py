import json

class ControleEstoque:
    def __init__(self, arquivo_estoque="estoque.json"):
        self.arquivo_estoque = arquivo_estoque
        self.estoque = self.carregar_estoque()

    def carregar_estoque(self):
        try:
            with open(self.arquivo_estoque, 'r', encoding='utf-8') as arquivo:
                estoque = json.load(arquivo)
            return estoque
        except FileNotFoundError:
            print(f"Arquivo {self.arquivo_estoque} nao encontrado. Criando novo arquivo.")
            return {}

    def salvar_estoque(self):
        with open(self.arquivo_estoque, 'w', encoding='utf-8') as arquivo:
            json.dump(self.estoque, arquivo, indent=2)

    def adicionar_item(self, item, quantidade):
        if item in self.estoque:
            self.estoque[item] += quantidade
        else:
            self.estoque[item] = quantidade
        self.salvar_estoque()

    def dar_baixa_item(self, item, quantidade):
        if item in self.estoque:
            if quantidade <= self.estoque[item]:
                self.estoque[item] -= quantidade
                print(f"Obs: {quantidade} unidades do {item} deram baixa no estoque.")
                self.salvar_estoque()
            else:
                print(f"Quantidade insuficiente em estoque do item {item}. Necessario solicitacao de compra.")
        else:
            print(f"Item nao encontrado no estoque do item {item}.")

    def exibir_estoque(self):
        print("Estoque atual:")
        for item, quantidade in self.estoque.items():
            print(f"{item}: {quantidade} unidades")


# Exemplo de uso
controle_estoque = ControleEstoque()

controle_estoque.exibir_estoque()

controle_estoque.dar_baixa_item("Sabonete liquido", 0)
controle_estoque.dar_baixa_item("Desinfetante", 0)
controle_estoque.dar_baixa_item("Limpador de uso geral", 0)
controle_estoque.dar_baixa_item("Luva 'P'", 0)
controle_estoque.dar_baixa_item("Sapato de seguranca feminino N 34", 0)
controle_estoque.dar_baixa_item("Papel Higienico", 0)
controle_estoque.dar_baixa_item("Galao de agua de 20 litros", 0)

controle_estoque.exibir_estoque()
