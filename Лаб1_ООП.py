import math

class Bqe:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.D = -1
        self.roots = []
    
    def get_coef(self, prompt):
        print(prompt)
        coef_str = input()
        while (True):
            try:
                coef = float(coef_str)
                break
            except:
                print(prompt)
                coef_str = input()
        return coef
        
    def get_coefs(self):
        while(self.D < 0):
            self.a = self.get_coef('Введите коэффициент A: ')
            self.b = self.get_coef('Введите коэффициент B: ')
            self.c = self.get_coef('Введите коэффициент C: ')
            self.D = self.b*self.b - 4*self.a*self.c
            if (self.D < 0):
                print('Дискриминант D =', self.D, 'меньше нуля')

    def calculate_roots(self):
        D = math.sqrt(self.D)
        root1 = (-self.b + D) / (2 * self.a)
        root2 = (-self.b - D) / (2 * self.a)
        if (root1 >= 0):
            self.roots.append(math.sqrt(root1))
            self.roots.append(-self.roots[-1])
            
        if (root2 >= 0 and root2 != root1):
            self.roots.append(math.sqrt(root2))
            self.roots.append(-self.roots[-1])

    def print_roots(self):
        if (len(self.roots) == 0):
            print('Нет корней')
        else:
            print('Корни уравнения: ', end = '')
            for j in self.roots:
                print(j, end = ' ')
            print('')


def main():
    r = Bqe()
    r.get_coefs()
    r.calculate_roots()
    r.print_roots()

if __name__ == "__main__":
    main()