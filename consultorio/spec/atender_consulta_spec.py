import unittest
from should_dsl import should, should_not
from eispatterns.domain.supportive.association_error import AssociationError
from consultorio.resources.atender_consulta import AtenderConsulta
from consultorio.decorators.consulta_decorator import ConsultaDecorator
from consultorio.decorators.medico_decorator import MedicoDecorator
from consultorio.rules.doctors_office_rules_base import DoctorsOfficeRuleBase
from eispatterns.domain.supportive.rule_manager import RuleManager


class AtenderConsultaSpec(unittest.TestCase):

    def setUp(self):
        RuleManager.rule_base = DoctorsOfficeRuleBase()


    def test_check_associacao_com_consulta_e_medico(self):
        #set the rule base
        #
        medico = MedicoDecorator('Pedro', '1234-5')
        consulta = ConsultaDecorator('abc-123')
        (AtenderConsulta, 'Eu nao sou uma consulta', medico) |should| throw(AssociationError)
        (AtenderConsulta, consulta, 'Eu nao sou um medico') |should| throw(AssociationError)
        (AtenderConsulta, consulta, medico) |should_not| throw(AssociationError)

    def test_verifica_se_consulta_foi_atendida(self):
        medico2 = MedicoDecorator('Joao', '9876-9')
        consulta2 = ConsultaDecorator('abc-456')
        AtenderConsulta(consulta2, medico2)
        consulta2.atendida |should| equal_to(True)