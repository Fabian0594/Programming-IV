class calculate:
    def __init__(self, *args):
        self.args = args
        acumulador = 0
        for i in args:
            acumulador += i
        print(acumulador)
    def subtract(self):
        acumulador = 0
        for i in self.args:
            acumulador -= i
        return acumulador
    
sum = calculate(2, 3, 4)
print(sum.subtract())