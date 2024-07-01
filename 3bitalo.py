import uuid

class GerenciadorDeFuncionarios: #definição da classe de gerenciamento
    def __init__(self):
        self.funcionarios = {} #definição da lista no caso, como vázia considerando um ponto 0

    def adicionar_funcionario(self, nome, cargo, salario): #definição do comando de adição, junto de categorias e definições à
        id_funcionario = str(uuid.uuid4()) #aplicação do id, sistema automático isso
        self.funcionarios[id_funcionario] = {
            'nome': nome,
            'cargo': cargo,
            'salario': salario
        }
        return id_funcionario

    def remover_funcionario(self, id_funcionario): #definição do comando de remoção
        if id_funcionario in self.funcionarios: #remove por id definido.
            del self.funcionarios[id_funcionario]
            return True
        return False

    def atualizar_funcionario(self, id_funcionario, nome=None, cargo=None, salario=None):
        if id_funcionario in self.funcionarios: #Definição do comando de atualização
            if nome:
                self.funcionarios[id_funcionario]['nome'] = nome #No caso, de forma separada essa ordem
            if cargo:
                self.funcionarios[id_funcionario]['cargo'] = cargo
            if salario:
                self.funcionarios[id_funcionario]['salario'] = salario
            return True
        return False
    def obter_funcionario(self, id_funcionario) :
        return self.funcionarios.get(id_funcionario, None)
    def listar_funcionarios(self): #esses dois últimos, o obter é para definir e falar sobre o funcionário pesquisado, já o da lista vai listar cada um desses funcionários já existentes na lista
        return self.funcionarios

# Uso interativo:
if __name__ == "__main__":
    gerenciador = GerenciadorDeFuncionarios()
#Ativação da parte interativa, menu de escolha por numeração com inputs relativos as intenções da opção escolhida
    while True: 
        print("\nOpções:")
        print("1. Adicionar funcionário")
        print("2. Remover funcionário")
        print("3. Atualizar funcionário")
        print("4. Obter informações de um funcionário")
        print("5. Listar todos os funcionários")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            id_funcionario = gerenciador.adicionar_funcionario(nome, cargo, salario)
            print(f"Funcionário adicionado com ID: {id_funcionario}")

        elif opcao == '2':
            id_funcionario = input("ID do funcionário a ser removido: ")
            if gerenciador.remover_funcionario(id_funcionario):
                print("Funcionário removido com sucesso.")
            else:
                print("Funcionário não encontrado.")

        elif opcao == '3':
            id_funcionario = input("ID do funcionário a ser atualizado: ")
            nome = input("Novo nome (deixe em branco para não alterar): ")
            cargo = input("Novo cargo (deixe em branco para não alterar): ")
            salario = input("Novo salário (deixe em branco para não alterar): ")
            salario = float(salario) if salario else None
            if gerenciador.atualizar_funcionario(id_funcionario, nome, cargo, salario):
                print("Funcionário atualizado com sucesso.")
            else:
                print("Funcionário não encontrado.")

        elif opcao == '4':
            id_funcionario = input("ID do funcionário: ")
            funcionario = gerenciador.obter_funcionario(id_funcionario)
            if funcionario:
                print("Informações do funcionário:", funcionario)
            else:
                print("Funcionário não encontrado.")

        elif opcao == '5':
            funcionarios = gerenciador.listar_funcionarios()
            if funcionarios:
                for id_func, info in funcionarios.items():
                    print(f"ID: {id_func}, Nome: {info['nome']}, Cargo: {info['cargo']}, Salário: {info['salario']}")
            else:
                print("Nenhum funcionário cadastrado.")

        elif opcao == '6': #break nesse caso é o fechamento do sistema
            print("Saindo...")
            break

        else: #Isso ocorre em caso de opção inválida, que gera o recomeço do código.
            print("Opção inválida, tente novamente.")