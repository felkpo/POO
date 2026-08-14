class Funcionario:
   def __init__(self, nome, salario_base):
       self.nome = nome
       self.salario_base = salario_base

   def calcular_bonus(self):
       return self.salario_base * 0.05

class Gerente(Funcionario):
   def __init__(self, nome, salario_base):
       super().__init__(nome, salario_base)

   def calcular_bonus(self):
       # Chama o bônus padrão da mãe e soma R$ 1000
       bonus_padrao = super().calcular_bonus()
       return bonus_padrao + 1000.0

class Vendedor(Funcionario):
   def __init__(self, nome, salario_base, total_vendas):
       super().__init__(nome, salario_base)
       self.total_vendas = total_vendas

   def calcular_bonus(self):
       # Sobrescreve totalmente: 10% do valor de suas vendas
       return self.total_vendas * 0.10
# --- TESTES DE EXECUÇÃO ---
g1 = Gerente("Ana Santos", 5000.0)
v1 = Vendedor("Carlos Lima", 2000.0, 30000.0)

print(f"Bônus da Gerente {g1.nome}: R$ {g1.calcular_bonus():.2f}")
print(f"Bônus do Vendedor {v1.nome}: R$ {v1.calcular_bonus():.2f}")
