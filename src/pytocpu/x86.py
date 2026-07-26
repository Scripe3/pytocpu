from .code import Code
from .exceptions import InvalidRegisterError

REG32 = {
    "eax": 0xB8,
    "ecx": 0xB9,
    "edx": 0xBA,
    "ebx": 0xBB,
    "esp": 0xBC,
    "ebp": 0xBD,
    "esi": 0xBE,
    "edi": 0xBF,
}

class X86(Code):
    def mov(self, register, value):
        register = register.lower()

        if register not in REG32:
            raise InvalidRegisterError(f"Invalid operand '{register}' for register eax")

        self.emit(
            REG32[register],
            value & 0xFF,
            (value >> 8) & 0xFF,
            (value >> 16) & 0xFF,
            (value >> 24) & 0xFF
        )

    def ret(self):
        self.emit(0xC3)

    def nop(self):
        self.emit(0x90)
