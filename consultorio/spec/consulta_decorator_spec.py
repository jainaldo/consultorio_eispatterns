import unittest
from should_dsl import should, should_not
from eispatterns.domain.node.machine import Machine
from consultorio.decorators.consulta_decorator import ConsultaDecorator


class ConsultaDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.consulta_decorator = ConsultaDecorator('00001')
        #test doubles won't work given type checking rules, using classic
        self.maquina = Machine()

    def test_decorador_uma_maquina(self):
        #should work
        self.consulta_decorator.decorate(self.maquina)
        self.consulta_decorator.decorated |should| be(self.maquina)
        self.consulta_decorator.decorated |should| have(1).decorators
        #should fail
        decorate, _, _ = self.consulta_decorator.decorate('Nao sou uma consulta')
        decorate |should| equal_to(False)