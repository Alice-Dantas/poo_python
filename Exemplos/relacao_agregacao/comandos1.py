class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
    # se você colocasse self.alunos fora do __init__(), o atributo alunos seria compartilhado entre todas as instâncias
    # além disso, esse atributo não precisa ser passado como parâmetro pois sempre criado do zero (vazio) para cada nova instância de Turma

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        print(f'Alunos da turma de {self.nome}')
        for aluno in self.alunos:
            print(f'Aluno: {aluno.nome} - Matrícula: {aluno.matricula}')

aluno1 = Aluno('Violeta', '123456')
aluno2 = Aluno('Leon', '234556')
turma1 = Turma('Programção Orientada a Objetos')
turma1.adicionar_aluno(aluno1)
turma1.adicionar_aluno(aluno2)
turma1.listar_alunos()
