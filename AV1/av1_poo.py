class Funcionario:
    """Classe base que representa um funcionário da TechCorp."""

    def __init__(self, nome, cpf, matricula, salario_base):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula
        # Encapsulamento: os dois underscores tornam o salário um atributo privado.
        self.__salario_base = salario_base

    def get_salario_base(self):
        """Retorna o salário base por meio de um getter."""
        return self.__salario_base

    def set_salario_base(self, novo_salario):
        """Altera o salário somente quando o novo valor é positivo."""
        if novo_salario > 0:
            self.__salario_base = novo_salario

    def calcular_salario_final(self):
        """Retorna o salário base, sem adicionais."""
        return self.get_salario_base()


class Gerente(Funcionario):
    """Funcionário que recebe um bônus de gestão."""

    def __init__(self, nome, cpf, matricula, salario_base, bonus_gestao):
        # Herança e super(): reutiliza o construtor da classe Funcionario.
        super().__init__(nome, cpf, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    def calcular_salario_final(self):
        # Sobrescrita: redefine o cálculo para incluir o bônus de gestão.
        return super().get_salario_base() + self.bonus_gestao


class Desenvolvedor(Funcionario):
    """Funcionário que pode receber adicional conforme seu nível."""

    def __init__(self, nome, cpf, matricula, salario_base, nivel):
        # Herança e super(): reaproveita a inicialização da classe base.
        super().__init__(nome, cpf, matricula, salario_base)
        self.nivel = nivel

    def calcular_salario_final(self):
        # Sobrescrita: somente desenvolvedores Senior recebem o adicional.
        adicional = 1500.0 if self.nivel == "Senior" else 0.0
        return super().get_salario_base() + adicional


def exibir_funcionario(funcionario):
    """Imprime os dados públicos e o salário final calculado."""
    print(f"Nome: {funcionario.nome}")
    print(f"CPF: {funcionario.cpf}")
    print(f"Matrícula: {funcionario.matricula}")
    print(f"Salário final: R$ {funcionario.calcular_salario_final():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))


if __name__ == "__main__":
    gerente = Gerente(
        "Marina Albuquerque",
        "272.494.834-28",
        "GR-3021",
        9200.0,
        1800.0,
    )
    desenvolvedor = Desenvolvedor(
        "Rafael Torquato",
        "357.378.687-85",
        "DEV-1187",
        7400.0,
        "Senior",
    )

    # Name mangling: fora da classe, __salario_base não acessa o privado;
    # o Python armazena o atributo real como _Funcionario__salario_base.
    salario_antes = gerente.get_salario_base()
    gerente.__salario_base = -1
    salario_depois = gerente.get_salario_base()
    print(f"Salário protegido antes: R$ {salario_antes:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Salário protegido depois da tentativa: R$ {salario_depois:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print()

    exibir_funcionario(gerente)
    print()
    exibir_funcionario(desenvolvedor)