# O que é Programação Orientada a Objetos (POO), Classes e Objetos

A **Programação Orientada a Objetos (POO)** é um paradigma de programação que estrutura o código a partir da criação e interação de **objetos**. Esses objetos representam entidades que possuem **estado** (atributos), **comportamento** (métodos) e uma **identidade única**. A POO é amplamente utilizada no desenvolvimento de software moderno devido à sua capacidade de modelar sistemas complexos de maneira modular, reutilizável e escalável.


## Conceitos Fundamentais

### Classe

Uma **classe** é uma estrutura que define um tipo de objeto. Ela funciona como um molde ou modelo a partir do qual objetos são criados. A classe descreve quais atributos (dados) e métodos (funções) os objetos daquele tipo possuirão.

Exemplo em Python:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
```

### Objeto

Um **objeto** é uma instância de uma classe. Ou seja, a partir da definição de uma classe, podemos criar diversos objetos que compartilham a mesma estrutura, mas com dados próprios.

```python
p1 = Pessoa("Lucas", 25)
p2 = Pessoa("Ana", 30)

p1.apresentar()  # Olá, meu nome é Lucas e tenho 25 anos.
p2.apresentar()  # Olá, meu nome é Ana e tenho 30 anos.
```

Cada objeto (p1, p2) é independente e possui seus próprios atributos, apesar de terem sido criados a partir da mesma classe.
