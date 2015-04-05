from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.supportive.rule import rule
from eispatterns.domain.supportive.core_rules import CoreRules


class DoctorsOfficeRuleBase(CoreRules):
    @rule('association')
    def should_be_instance_of_consulta(self, associated):
        '''Associated object should be instance of Consulta Decorator'''
        from consultorio.decorators.consulta_decorator import ConsultaDecorator
        try: associated |should| be_instance_of(ConsultaDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_paciente(self, associated):
        '''Associated object should be instance of Paciente Decorator'''
        from consultorio.decorators.paciente_decorator import PacienteDecorator
        try: associated |should| be_instance_of(PacienteDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_medico(self, associated):
        '''Associated object should be instance of Medico'''
        from consultorio.decorators.medico_decorator import MedicoDecorator
        try: associated |should| be_instance_of(MedicoDecorator)
        except ShouldNotSatisfied: return False
        else: return True