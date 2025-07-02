class Relogio:
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos

    def __str__(self):
        # Retorna uma string formatada como HH:MM (ex: 08:05)
        return f"{self.horas:02d}:{self.minutos:02d}"

    def __call__(self, minutos_adiantados):
        # Soma os minutos ao total
        total_minutos = self.horas * 60 + self.minutos + minutos_adiantados
        
        # Calcula nova hora e minuto
        self.horas = (total_minutos // 60) % 24  # % 24 para não passar de 23h
        self.minutos = total_minutos % 60


#Como usar:
relogio = Relogio(14, 45)
print(relogio)  # Saída: 14:45

relogio(80)     # Adianta 1 hora e 20 minutos
print(relogio)  # Saída: 16:05

relogio(500)    # Adianta 8h20min
print(relogio)  # Saída: 00:25
