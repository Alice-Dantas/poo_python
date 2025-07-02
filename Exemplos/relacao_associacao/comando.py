class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Compromisso:
    def __init__(self, descricao, data, hora):
        self.descricao = descricao
        self.data = data
        self.hora = hora

class Agenda:
    def agendar(self, pessoa, compromisso):
        print(f'{pessoa.nome} tem um compromisso: {compromisso.descricao} em {compromisso.data} às {compromisso.hora}')
# a classe Agenda não possui atributos próprios, ela apenas usa objetos de outras classes (Pessoa e Compromisso) temporariamente, por isso não precisa de __init__().

pessoa1 = Pessoa('Julieta', 998765432)
compromisso1 = Compromisso('Estudar POO', '2025-04-05', '13:00')
agenda1 = Agenda() # a classe Agenda não foi definida para receber parâmetros no construtor __init__(), por isso não passamos argumentos na hora de criar objetos dessa classe.
agenda1.agendar(pessoa1, compromisso1)
