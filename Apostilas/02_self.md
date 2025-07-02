# Entendendo o *self* em Programação Orientada a Objetos

Ele é usado dentro das classes para representar **a instância atual do objeto**, ou seja, o **próprio objeto que está sendo manipulado** naquele momento.

Sempre que um método é chamado a partir de um objeto, o Python **passa automaticamente esse objeto como o primeiro argumento** para o método — e, por convenção, damos o nome *self* a esse argumento.

## Para que serve o `self`

O *self* permite que **cada objeto manipule seus próprios dados**, mantendo sua identidade separada dos demais.  
Ele é usado para **acessar os atributos e métodos pertencentes àquela instância**.

## Exemplo Prático:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome     # atributo 'nome' do objeto atual
        self.idade = idade   # atributo 'idade' do objeto atual
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
```

### Neste exemplo:

- self.nome e self.idade pertencem àquela pessoa específica (objeto) que foi criada.
- O método apresentar() usa self para acessar os dados daquela mesma instância.

## Criando Objetos com self em Ação:

```python
p1 = Pessoa("Lucas", 25)
p2 = Pessoa("Ana", 30)

p1.apresentar()  # Olá, meu nome é Lucas e tenho 25 anos.
p2.apresentar()  # Olá, meu nome é Ana e tenho 30 anos.
```

### Repare que:

- p1 e p2 são objetos diferentes, cada um com seus próprios atributos.
- Quando p1.apresentar() é chamado, o self dentro do método representa o p1.
- Quando p2.apresentar() é chamado, o self representa o p2.

## Por que não usamos self fora da classe?

- O self só faz sentido dentro da definição de uma classe, pois ele depende do contexto de um objeto.
- Fora de uma classe ou método de instância, o self nem sequer é reconhecido pelo Python.

---

### Curiosidade

Apesar de o nome self ser apenas uma convenção (você poderia usar outro nome),
é altamente recomendado não mudar, para manter a legibilidade e seguir os padrões do Python.
