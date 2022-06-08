qtd_alunos = input("Quantidade de alunos: ")

dicionario = {}
lista_dicionario = []
def criar():
        for n in range(1,int(qtd_alunos)+1):
                print(f"\nPreencha as respectivas informações para o Aluno {n}.")
                dicionario["ra"] = input("RA: ")
                dicionario["nome"] = input("Nome: ")
                dicionario["nota"] = input("Nota: ")
                lista_dicionario.append({"ra": dicionario["ra"], "nome": dicionario["nome"], "nota": dicionario["nota"]})

def incluir():
        print(f"\nPreencha as respectivas informações para o Novo Aluno.")
        dicionario["ra"] = input("RA: ")
        dicionario["nome"] = input("Nome: ")
        dicionario["nota"] = input("Nota: ")
        lista_dicionario.append({"ra": dicionario["ra"], "nome": dicionario["nome"], "nota": dicionario["nota"]})

def consultar():
        print("\nConsulta de dados de aluno.")
        ra = input("RA: ")
        for i in range(len(lista_dicionario)):
                if ra == lista_dicionario[i]["ra"]:
                        print(f'''\nRA: {lista_dicionario[i]["ra"]}
Nome: {lista_dicionario[i]["nome"]}
Nota: {lista_dicionario[i]["nota"]}''')

def imprimir():
        print("\nImprimindo informações dos alunos com nota maior ou igual a 5.0...")
        for i in range(len(lista_dicionario)):
                if float(lista_dicionario[i]["nota"]) >= 5:
                        print(f'''\nRA: {lista_dicionario[i]["ra"]}
Nome: {lista_dicionario[i]["nome"]}
Nota: {lista_dicionario[i]["nota"]}''')

def imprimirTODOS():
        print("\nImprimindo informações de todos os alunos...")
        print("\nRA\tNome\tNote")
        for i in range(len(lista_dicionario)):
                print(f"{lista_dicionario[i]['ra']}\t{lista_dicionario[i]['nome']}\t{lista_dicionario[i]['nota']}")

if __name__ == "__main__":
        criar()
        op = True
        while op:
                opt = input('''\n<<< OPERAÇÕES >>>
        1. Consultar DADOS de UM ALUNO;
        2. Incluir um NOVO ALUNO;
        3. Imprimir TODOS OS ALUNOS COM NOTA MAIOR OU IGUAL A 5,0;
        4. Imprimir TODOS OS ALUNOS;
        0. Encerrar programa;

        Escolha <0 a 4>: ''')

                if int(opt) == 1:
                        consultar()
                elif int(opt) == 2:
                        incluir()
                elif int(opt) == 3:
                        imprimir()
                elif int(opt) == 4:
                        imprimirTODOS()
                elif int(opt) == 0:
                        op = False
