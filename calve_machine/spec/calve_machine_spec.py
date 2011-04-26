import unittest
from should_dsl import should
from calve_machine import inseminate, pregnant

class CalveMachineSpec(unittest.TestCase):

    def it_calves_an_object_given_plain_attributes(self):
        @inseminate
        def programmer(p):
            p.name = 'Sheldon Cooper, Ph.D.'
            p.age = 29
            p.languages = ['eiffel', 'io', 'erlang']

        prog = pregnant.calve('programmer')
        prog.name |should| equal_to('Sheldon Cooper, Ph.D.')
        prog.age |should| be(29)
        prog.languages |should| equal_to(['eiffel', 'io', 'erlang'])


    def it_inherits_insemination(self):
        @inseminate
        def programmer(p):
            p.name = 'Sheldon Cooper, Ph.D.'
            p.age = 29
            p.languages = ['eiffel', 'io', 'erlang']

        @inseminate(sperm_from='programmer')
        def python_programmer(p):
            p.languages = ['python']
            p.foo = 'spam'

        prog = pregnant.calve('python_programmer')
        prog.name |should| equal_to('Sheldon Cooper, Ph.D.')
        prog.age |should| be(29)
        prog.languages |should| equal_to(['python'])
        prog.foo |should| equal_to('spam')

        @inseminate(sperm_from='python_programmer')
        def zope_programmer(p):
            p.languages = ['zcml']
            p.age = 30

        prog = pregnant.calve('zope_programmer')
        prog.name |should| equal_to('Sheldon Cooper, Ph.D.')
        prog.age |should| be(30)
        prog.languages |should| equal_to(['zcml'])
        prog.foo |should| equal_to('spam')

