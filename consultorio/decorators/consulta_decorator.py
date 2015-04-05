from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.base.decorator import Decorator
from eispatterns.domain.node.machine import Machine
from eispatterns.domain.resource.operation import operation
from eispatterns.domain.supportive.association_error import AssociationError
from datetime import datetime



class ConsultaDecorator(Decorator):
    '''Consulta Decorator'''
    decoration_rules = ['should_be_instance_of_machine']

    def __init__(self, numero):
        Decorator.__init__(self)
        self.description = "Uma consulta de consultorio"
        self.numero = numero
        self.valor = 0
        self.pago = False
        self.agendado = False
        self.atendido = False

    def set_valor_da_consulta(self, valor):
        ''' Valor da consulta'''
        self.valor += valor

