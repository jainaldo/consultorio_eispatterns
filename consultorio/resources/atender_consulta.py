from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.supportive.association_error import AssociationError
from eispatterns.domain.resource.work_item import WorkItem
from eispatterns.domain.supportive.rule_manager import RuleManager
from consultorio.rules.doctors_office_rules_base import DoctorsOfficeRuleBase


class AtenderConsulta(WorkItem):
    ''' Atender uma consulta, precisar de uma consulta e o medico '''
    def __init__(self, consulta, medico):
        WorkItem.__init__(self)

        RuleManager.rule_base = DoctorsOfficeRuleBase()
        if not RuleManager.get_instance().check_rule('should_be_instance_of_consulta', consulta):
            raise AssociationError('Consulta instance expected, instead %s passed' % type(consulta))
        self.consulta = consulta
        if not RuleManager.get_instance().check_rule('should_be_instance_of_medico', medico):
           raise AssociationError('Medico instance expected, instead %s passed' % type(medico))
        self.medico = medico
        consulta.atendida = True