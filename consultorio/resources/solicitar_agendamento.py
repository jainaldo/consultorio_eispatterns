from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.supportive.association_error import AssociationError
from eispatterns.domain.resource.work_item import WorkItem
from eispatterns.domain.supportive.rule_manager import RuleManager
from consultorio.rules.doctors_office_rules_base import DoctorsOfficeRuleBase


class SolicitarAgendamento(WorkItem):
    ''' Agendar a consulta, precisar de uma consulta, um paciente e a data do agendamento '''
    def __init__(self, consulta, paciente, data):
        WorkItem.__init__(self)
        self.data = data
        RuleManager.rule_base = DoctorsOfficeRuleBase()
        if not RuleManager.get_instance().check_rule('should_be_instance_of_consulta', consulta):
            raise AssociationError('Consulta instance expected, instead %s passed' % type(consulta))
        self.consulta = consulta
        if not RuleManager.get_instance().check_rule('should_be_instance_of_paciente', paciente):
           raise AssociationError('Paciente instance expected, instead %s passed' % type(paciente))
        self.paciente = paciente
        paciente.consultas_agendadas.append(self)