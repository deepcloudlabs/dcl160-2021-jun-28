class Employee:
    """
    variable arguments
    def __init__(self, *args):
        self.identity = args[0]
        self.fullname = args[1]
    """

    def __init__(self, identity, fullname):
        self.identity = identity
        self.fullname = fullname