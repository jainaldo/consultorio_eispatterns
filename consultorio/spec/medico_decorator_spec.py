import unittest
from should_dsl import should
from eispatterns.domain.node.person import Person
from eispatterns.domain.node.machine import Machine
from consultorio.decorators.medico_decorator import MedicoDecorator
from consultorio.decorators.paciente_decorator import PacienteDecorator
from consultorio.decorators.consulta_decorator import ConsultaDecorator
from consultorio.decorators.atendente_decorator import AtendenteDecorator
from consultorio.rules.doctors_office_rules_base import DoctorsOfficeRuleBase
from eispatterns.domain.supportive.rule_manager import RuleManager

class MedicoDecoratorSpec(unittest.TestCase):
    ''' Medico Decorator Spec '''

    def setUp(self):
        RuleManager.rule_base = DoctorsOfficeRuleBase()
        self.medico_decorator = MedicoDecorator("Joao", "1234-5")
        #test doubles won't work given type checking rules, using classic
        self.pessoa = Person()

    def test_decorador_uma_pessoa(self):
        #should work
        self.medico_decorator.decorate(self.pessoa)
        self.medico_decorator.decorated |should| be(self.pessoa)
        self.medico_decorator.decorated |should| have(1).decorators
        #should fail
        decorate,_,_ = self.medico_decorator.decorate('Nao sou uma pessoa')
        decorate |should| equal_to(False)



    def test_atender_uma_consulta(self):
        ma_consulta = Machine()
        consulta = ConsultaDecorator("abc-2")
        consulta.set_valor_da_consulta(30)

        pe_atendente = Person()
        atendente = AtendenteDecorator("Joao")
        atendente.decorate(pe_atendente)

        pe_paciente = Person()
        paciente = PacienteDecorator("Pedro")
        paciente.decorate(pe_paciente)

        atendente.solicitar_agendamento(consulta, paciente, "20/01/2014")

        self.medico_decorator.decorate(self.pessoa)
        self.medico_decorator.atender_consulta(consulta)

        self.pessoa.input_area |should| contain("abc-2")
        consulta.atendida |should| equal_to(True)