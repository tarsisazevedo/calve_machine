calve_machine
=============

Factories for plain old Python objects.


Usage::

    from calve_machine import inseminate, pregnant

    @inseminate
    def programmer(p):
        p.name = 'Sheldon Cooper, Ph.D.'
        p.age = 29
        p.languages = ['eiffel', 'io', 'erlang']

    prog = pregnant.calve('programmer')
    prog.name |should| equal_to('Sheldon Cooper, Ph.D.')
    prog.age |should| be(29)
    prog.languages |should| equal_to(['eiffel', 'io', 'erlang'])


Factories can inherit from other(s)::

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



How to install
--------------

The project is at a very early stage, there's no PyPi release.


How to run tests
----------------

Just run::

    make test

for install all test dependencies (`Should-DSL <http://www.should-dsl.info>`_
and `Specloud <https://github.com/hugobr/specloud>`_, at the moment) and
run the tests. calve_machine itself has no dependencies.

