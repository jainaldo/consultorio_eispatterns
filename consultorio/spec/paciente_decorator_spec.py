import unittest
from should_dsl import should
from eispatterns.domain.node.person import Person
from eispatterns.domain.node.machine import Machine
from consultorio.decorators.paciente_decorator import PacienteDecorator
from consultorio.decorators.consulta_decorator import ConsultaDecorator
from consultorio.decorators.atendente_decorator import AtendenteDecorator


class PacienteDecoratorSpec(unittest.TestCase):
    ''' Paciente Decorator Spec '''

    def setUp(self):
        self.paciente_decorator = PacienteDecorator("Joao")
        #test doubles won't work given type checking rules, using classic
        self.pessoa = Person()

    def test_decorador_uma_pessoa(self):
        #should work
        self.paciente_decorator.decorate(self.pessoa)
        self.paciente_decorator.decorated |should| be(self.pessoa)
        self.paciente_decorator.decorated |should| have(1).decorators
        #should fail
        decorate,_,_ = self.paciente_decorator.decorate('Nao sou uma pessoa')
        decorate |should| equal_to(False)

    def test_generates_register(self):
        self.paciente_decorator.generate_register('123456-7')
        self.paciente_decorator.register |should| equal_to('123456-7')

    def test_paga_consulta_atendidas(self):
        ma_consulta = Machine()
        consulta = ConsultaDecorator("abc-1")
        consulta.set_valor_da_consulta(50)

        pe_atendente = Person()
        atendente = AtendenteDecorator("Joao")
        atendente.decorate(pe_atendente)

        atendente.solicitar_agendamento(consulta, self.paciente_decorator, "20/01/2014")

        self.paciente_decorator.pagar_consulta("abc-1")

        if consulta.atendido:
            consulta.pago |should| equal_to(True)
        else:
            consulta.pago |should| equal_to(False)