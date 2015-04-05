from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.base.decorator import Decorator
from eispatterns.domain.node.person import Person
from consultorio.resources.solicitar_agendamento import SolicitarAgendamento


class AtendenteDecorator(Decorator):
    '''Atendente Decorator'''
    decoration_rules = ['should_be_instance_of_person']

    def __init__(self, nome):
        Decorator.__init__(self)
        self.description = "Representa um Atendente"
        self.name = nome

    def generate_register(self, register):
        ''' generates the register number for the atendente '''
        self.register = register


    def solicitar_agendamento(self, consulta, paciente, data):
        ''' Solicitacao de agendamento de consulta para um paciente'''
        if not consulta.agendada:
           agendamento = SolicitarAgendamento(consulta, paciente, data)

           self.decorated.input_area[agendamento.consulta.numero] = agendamento
