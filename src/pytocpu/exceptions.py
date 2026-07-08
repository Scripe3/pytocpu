class PyToCPUError(Exception):
    pass


class InvalidRegisterError(PyToCPUError):
    pass


class InvalidInstructionError(PyToCPUError):
    pass