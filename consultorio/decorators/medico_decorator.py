from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.base.decorator import Decorator
from eispatterns.domain.node.person import Person
from consultorio.resources.solicitar_agendamento import SolicitarAgendamento
from consultorio.resources.atender_consulta import AtenderConsulta


class MedicoDecorator(Decorator):
    '''Medico Decorator'''
    decoration_rules = ['should_be_instance_of_person']

    def __init__(self, nome, crm):
        Decorator.__init__(self)
        self.description = "Representa um Medico"
        self.name = nome
        self.crm = crm

    def atender_consulta(self, consulta):
        if not consulta.atendida:
            consulta_antedida = AtenderConsulta(consulta, self)
            self.decorated.input_area[consulta.numero] = consulta_antedida