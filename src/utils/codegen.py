from string import ascii_lowercase, ascii_uppercase, digits
from random import choice


class CodeGenerator:
    def __init__(self, allowed: str):
        self.allowed = allowed
    
    def __call__(self, length: int) -> str:
        code = ""
        for _ in range(length):
            code += choice(self.allowed)
        return code


codegen = CodeGenerator(ascii_lowercase + ascii_uppercase + digits)