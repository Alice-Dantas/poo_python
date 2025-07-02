class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15

class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.05


# Funcionário genérico, sem cargo específico
funcionario1 = Funcionario("Diego", 5000)

# Gerente, Desenvolvedor e Estagiário
gerente1 = Gerente("Alice", 10000)
dev1 = Desenvolvedor("Bruno", 8000)
estagiario1 = Estagiario("Carla", 2000)

# Mostrando os bônus
print(f"{funcionario1.nome} (Funcionário) - Bônus: R${funcionario1.calcular_bonus():.2f}")
print(f"{gerente1.nome} (Gerente) - Bônus: R${gerente1.calcular_bonus():.2f}")
print(f"{dev1.nome} (Desenvolvedor) - Bônus: R${dev1.calcular_bonus():.2f}")
print(f"{estagiario1.nome} (Estagiário) - Bônus: R${estagiario1.calcular_bonus():.2f}")
