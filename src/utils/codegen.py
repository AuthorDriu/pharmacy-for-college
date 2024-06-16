from string import ascii_lowercase, ascii_uppercase, digits
from random import choice


class CodeGenerator:
    def __init__(self):
        self.allowed = ascii_lowercase + ascii_uppercase + digits
    
    def __call__(self) -> str:
        code = ""
        for _ in range(6):
            code += choice(self.allowed)
        return code


codegen = CodeGenerator()