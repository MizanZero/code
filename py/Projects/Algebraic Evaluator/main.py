"""
private methods: _methName()
"""

class expression():
    opList = '+-*/'


    def __init__(self, inp):
        self.inp = inp
        self.formatted = self._format()
        self.display = ' '.join(self.formatted)

    def __str__(self) -> str:
        return self.display

    def _format(self) -> list: #private method
        result = []
        for char in self.inp:
            if char in self.opList:
                result.extend([' ', char, ' '])
            elif char:
                result.append(char)
        return ''.join(result).split()

    
    class token():
        def __init__(self, type:int, index:int):
            self.type = type
            #1. seperate const
            #2. separate var
            #3. coeff*var
            self.index = index



exp = expression('2x+ 4y*6')
print(exp)
print(exp.formatted)

