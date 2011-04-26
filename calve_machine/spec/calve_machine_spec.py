import unittest
from should_dsl import should
from calve_machine import inseminate, pregnant

class CalveMachineSpec(unittest.TestCase):

    def it_calves_an_object_given_plain_attributes(self):
        @inseminate
        def programmer(p):
            p.name = 'Sheldon Cooper'
            p.age = 29
            p.languages = ['eiffel', 'io', 'erlang']

        prog = pregnant.calve('programmer')
        prog.name |should| equal_to('Sheldon Cooper')
        prog.age |should| be(29)
        prog.languages |should| equal_to(['eiffel', 'io', 'erlang'])

