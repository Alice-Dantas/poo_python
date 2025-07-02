class GerenciadorDeLog:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def __enter__(self):
        # Abre o arquivo em modo append (adiciona conteúdo no final)
        self.arquivo = open(self.nome_arquivo, 'a')
        self.arquivo.write("Iniciando o log...\n")
        return self.arquivo  # Isso será atribuído à variável após o "as" no with

    def __exit__(self, tipo_excecao, valor, traceback):
        self.arquivo.write("Encerrando o log...\n")
        self.arquivo.close()
        if tipo_excecao:
            print("Ocorreu um erro durante a escrita no log!")
            print(f"Tipo: {tipo_excecao.__name__}, Valor: {valor}")
        # Retornar False faz a exceção ser propagada normalmente
        return False



# Uso prático da classe com with:

# Criando uma entrada de log
try:
    with GerenciadorDeLog("log.txt") as log:
        log.write("Usuário acessou o sistema às 10:00.\n")
        log.write("Usuário realizou uma operação crítica.\n")
        # Simulando um erro
        raise ValueError("Simulação de erro!")
        log.write("Esta linha não será executada.\n")
except Exception as e:
    print("Erro tratado fora do contexto with.")


# Resultado no log.txt:
#Iniciando o log...
#Usuário acessou o sistema às 10:00.
#Usuário realizou uma operação crítica.
#Encerrando o log...
