import unittest
from should_dsl import should
from eispatterns.domain.node.person import Person
from eispatterns.domain.node.machine import Machine
from consultorio.decorators.paciente_decorator import PacienteDecorator
from consultorio.decorators.consulta_decorator import ConsultaDecorator
from consultorio.decorators.atendente_decorator import AtendenteDecorator
from consultorio.decorators.medico_decorator import MedicoDecorator
from consultorio.rules.doctors_office_rules_base import DoctorsOfficeRuleBase
from eispatterns.domain.supportive.rule_manager import RuleManager


class PacienteDecoratorSpec(unittest.TestCase):
    ''' Paciente Decorator Spec '''

    def setUp(self):
        RuleManager.rule_base = DoctorsOfficeRuleBase()
        self.paciente_decorator = PacienteDecorator("Joao")
        #test doubles won't work given type checking rules, using classic
        self.pessoa = Person()
        self.atendente = AtendenteDecorator("Joao")
        self.medico = MedicoDecorator("Fernando", "1234-5")

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


    def test_paga_apenas_consulta_atendidas(self):
        ma_consulta = Machine()
        self.consulta = ConsultaDecorator("abc-1")
        self.consulta.set_valor_da_consulta(50)
        self.consulta.decorate(ma_consulta)

        pe_atendente = Person()
        self.atendente.decorate(pe_atendente)

        pe_medico = Person()
        self.medico.decorate(pe_medico)

        self.atendente.solicitar_agendamento(self.consulta, self.paciente_decorator, "20/01/2014")

        #consulta nao atendida, paciente nao paga a consulta
        self.paciente_decorator.pagar_consulta("abc-1")
        self.consulta.paga |should| equal_to(False)


        self.medico.atender_consulta(self.consulta)

        #consulta atendida, paciente paga a consulta
        self.paciente_decorator.pagar_consulta("abc-1")
        self.consulta.paga |should| equal_to(True)

