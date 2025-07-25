class calculator:
    def __init__(self):
        self.history=[]
    def add(self,a,b):
        c=a+b
        self.history.append(f"add={a}+{b}={c}")
        return c
    def mul(self,a,b):
        c=a*b
        self.history.append(f"mul={a}*{b}={c}")
        return c
    def sub(self,a,b):
        c=a-b
        self.history.append(f"sub={a}-{b}={c}")
        return c
    def mod(self,a,b):
        c=a%b
        self.history.append(f"mod={a}%{b}={c}")
        return c

    def div(self, a, b):
        if b == 0:
            entry = f"div={a}/{b}=Error"
            self.history.append(entry)
            return None
        else:
            c = a / b
            self.history.append(f"div={a}/{b}={c}")
            return c

    def show_history(self):
        for entry in self.history:
            print(entry)


if __name__ == "__main__":
    calc = calculator()
    print("Add:      ", calc.add(2, 3))
    print("Subtract: ", calc.sub(5, 2))
    print("Multiply: ", calc.mul(4, 6))
    print("Modulo:   ", calc.mod(10, 3))
    print("Divide:   ", calc.div(10, 2))
    print("Divide 0: ", calc.div(1, 0))
    print("\nHistory:")
    calc.show_history()
