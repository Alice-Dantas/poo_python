class Processador:
    def __init__(self):
        # Define um tipo fixo de processador ao instanciar
        self.tipo = "Intel i7"

class Memoria:
    def __init__(self):
        # Define a capacidade da memória ao instanciar
        self.capacidade = "16GB"

class Disco:
    def __init__(self):
        # Define o espaço de armazenamento ao instanciar
        self.espaco = "512GB SSD"

class Computador:
    def __init__(self):
        self.processador = Processador()  # Cria um objeto da classe Processador
        self.memoria = Memoria()          # Cria um objeto da classe Memoria
        self.disco = Disco()              # Cria um objeto da classe Disco

    def exibir_configuracao(self):
        print('As configurações do seu computador são: ')
        print(f"Processador: {self.processador.tipo}")
        print(f"Memória: {self.memoria.capacidade}")
        print(f"Disco: {self.disco.espaco}")


meu_pc = Computador()
meu_pc.exibir_configuracao()
