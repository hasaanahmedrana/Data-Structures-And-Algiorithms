class Term:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power


class Polynomial:
    def __init__(self):
        self.polynomial = []

    def addterm(self, coefficient, power):
        self.polynomial.append(Term(coefficient, power))

    def getDegree(self):
        maxi = 0
        for i in self.polynomial:
            if i.power > maxi:
                maxi = i.power
        return f'The degree of the polynomial is {maxi}'

    def getCoefficient(self, power):
        c = []
        for each in self.polynomial:
            if each.power == power:
                c.append(each.coefficient)
        if c == []:
            return 'No such term exists.'
        if len(c) == 1:
            return f'The coefficient against the power {power} is {c[0]}'
        return f'The coefficient against the power {power} are {c}'

    def evaluate(self, value):
        x = 0
        for each in self.polynomial:
            x += (each.coefficient * (value**each.power))
        return f'The value of the polynomial against {value} is {x}'

    def __str__(self):
        string = ''
        for each in self.polynomial:
            string += str(each.coefficient)
            string += f'x^{each.power}'
            if each != self.polynomial[-1]:
                string += ' + '
        return string

    def __add__(self, other):
        result = Polynomial()
        common_pow = []
        x = self.polynomial
        y = other.polynomial
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i].power == y[j].power:
                    result.addterm(x[i].coefficient + y[j].coefficient, x[i].power)
                    common_pow.append(x[i].power)
        for i in y:
            if i.power not in common_pow:
                result.addterm(i.coefficient, i.power)
        for i in x:
            if i.power not in common_pow:
                result.addterm(i.coefficient, i.power)
        return  f'Sum is {result}'

    def derivative(self):
        result = Polynomial()
        for each in self.polynomial:
            result.addterm(each.coefficient * each.power , each.power - 1)
        return result

    def anti_derivative(self):
        result = Polynomial()
        for each in self.polynomial:
            result.addterm(each.coefficient // (each.power - 1), each.power + 1)
        return result

    def clear(self):
        result = Polynomial()
        for each in self.polynomial:
            result.addterm(0, each.power)
        return result

    def addCoefficient(self, coefficient, power):
        result = Polynomial()
        for each in self.polynomial:
            if power == each.power:
                result.addterm(each.coefficient + coefficient, each.power)
            else:
                result.addterm(each.coefficient, each.power)
        return result

    def setCoefficient(self, coefficient, power):
        result = Polynomial()
        for each in self.polynomial:
            if power == each.power:
                result.addterm(coefficient, each.power)
            else:
                result.addterm(each.coefficient, each.power)
        return result

    def __sub__(self, other):
        result = Polynomial()
        common_pow = []
        x = self.polynomial
        y = other.polynomial
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i].power == y[j].power:
                    result.addterm(x[i].coefficient - y[j].coefficient, x[i].power)
                    common_pow.append(x[i].power)
        for i in y:
            if i.power not in common_pow:
                result.addterm(i.coefficient, i.power)
        for i in x:
            if i.power not in common_pow:
                result.addterm(i.coefficient, i.power)
        return  f'SUB is {result}'

    def __mul__(self, other):
        result = Polynomial()
        for i in self.polynomial:
            for j in other.polynomial:
                result.addterm(i.coefficient * j.coefficient, i.power + j.power)
        return result


def main():
    p1 = Polynomial()
    p1.addterm(2, 5)
    p1.addterm(3, 6)
    p2 = Polynomial()
    p2.addterm(3, 6)
    p2.addterm(2, 5)
    p2.addterm(2, 2)
    print('P1:', p1)
    print('P2:', p2)
    print(p1.getDegree())
    print(p1.getCoefficient(5))
    print(p1.getCoefficient(6))
    print(p1)
    print(p1.evaluate(2))
    print(p1)
    print(p2)
    print(p1 + p2)
    x = p1.derivative()
    print('The derivative of p1 is:', x)
    print('The antiderivative is:', x.anti_derivative())
    print('Product of p1 and p2 is:', p1 * p2)


main()

#TASK-2
def calculateGCD(a, b):
    if b == 0:
        return a
    else:
        return calculateGCD(b, a % b)

print(calculateGCD(15, 5))

print(calculateGCD(40, 60))
