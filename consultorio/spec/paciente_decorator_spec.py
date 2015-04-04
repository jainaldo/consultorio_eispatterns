import unittest
from should_dsl import should
from eispatterns.domain.node.person import Person
from consultorio.decorators.paciente_decorator import PacienteDecorator


class PacienteDecoratorSpec(unittest.TestCase):
    ''' Paciente Decorator Spec '''

    def setUp(self):
        self.paciente_decorator = PacienteDecorator("Joao")
        #test doubles won't work given type checking rules, using classic
        self.pessoa = Person()

    def test_decorador_uma_pessoa(self):
        #should work
        self.paciente_decorator.decorate(self.pessoa)
        self.paciente_decorator.decorated |should| be(self.pessoa)
        self.paciente_decorator.decorated |should| have(1).decorators
        #should fail
        decorate,_,_ = self.paciente_decorator.decorate('Nao sou uma pessoa')
        decorate |should| equal_to(False)

    def test_generates_register(self):
        self.paciente_decorator.generate_register('123456-7')
        self.paciente_decorator.register |should| equal_to('123456-7')