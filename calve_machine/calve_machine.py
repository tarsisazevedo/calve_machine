class CalveMachine(object):
    def __init__(self):
        self.sperms = {}

    def receive(self, sperm):
        self.sperms[sperm.__name__] = sperm

    def calve(self, sperm_name):
        sperm = self.sperms[sperm_name]
        ovum = type('object', (object,), {})()
        sperm(ovum)
        return ovum


_woman = pregnant = CalveMachine()

def inseminate(sperm):
    _woman.receive(sperm)

