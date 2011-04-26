class CalveMachine(object):
    def __init__(self):
        self.sperms = {}
        self.sperm_inheritance = {}

    def receive(self, sperm, sperm_from=None):
        self.sperms[sperm.__name__] = sperm
        if sperm_from:
            self.sperm_inheritance[sperm] = self.sperms[sperm_from]

    def calve(self, sperm_name):
        this_sperm = self.sperms[sperm_name]
        ovum = type('object', (object,), {})()
        sperm_hierarchy = [this_sperm]
        while self.sperm_inheritance.has_key(this_sperm):
            ancient_sperm = self.sperm_inheritance[this_sperm]
            sperm_hierarchy.insert(0, ancient_sperm)
            this_sperm = ancient_sperm
        for sperm in sperm_hierarchy:
            sperm(ovum)
        return ovum


_woman = pregnant = CalveMachine()

def inseminate(*sperm, **options):
    if sperm:
        _woman.receive(sperm[0])
    else:
        def decorator(sperm):
            _woman.receive(sperm, sperm_from=options['sperm_from'])
        return decorator

