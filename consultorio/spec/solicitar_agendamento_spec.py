import unittest
from should_dsl import should, should_not
from eispatterns.domain.supportive.association_error import AssociationError
from consultorio.resources.solicitar_agendamento import SolicitarAgendamento
from consultorio.decorators.consulta_decorator import ConsultaDecorator
from consultorio.decorators.paciente_decorator import PacienteDecorator
from consultorio.rules.doctors_office_rules_base import DoctorsOfficeRuleBase
from eispatterns.domain.supportive.rule_manager import RuleManager


class SolicitarAgendamentoSpec(unittest.TestCase):

    def setUp(self):
        RuleManager.rule_base = DoctorsOfficeRuleBase()


    def test_check_associacao_com_consulta_e_paciente(self):
        #set the rule base
        #
        paciente = PacienteDecorator('Pedro')
        consulta = ConsultaDecorator('abc-123')
        (SolicitarAgendamento, 'Eu nao sou uma consulta', paciente, "02/03/2014") |should| throw(AssociationError)
        (SolicitarAgendamento, consulta, 'Eu nao sou um paciente', "02/03/2014") |should| throw(AssociationError)
        (SolicitarAgendamento, consulta, paciente, "02/03/2014") |should_not| throw(AssociationError)

    def test_verifica_se_consulta_foi_agendada(self):
        paciente2 = PacienteDecorator('Joao')
        consulta2 = ConsultaDecorator('abc-456')
        SolicitarAgendamento(consulta2, paciente2, '22/03/2015')
        consulta2.agendada |should| equal_to(True)