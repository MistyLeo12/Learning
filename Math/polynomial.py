import numpy as np
import matplotlib.pyplot as plt

class Polynomial:
    def __init__(self, coefficents):
        #coffeicients go from a^n....a^0
        self.coefficients = coefficents
    
    def __repr__(self):
        #returns string representation of the given polynomial
        return "Polynomial Coefficents: " + str((self.coefficients))
    
    def __call__(self, x):
        result = 0
        # coefficents[i]*x[i]**degree
        for coefficent in self.coefficients:
            result = result * x + coefficent
        return result

def createPolynomial():
    coefficents = []
    print("Enter a number corresponding to the polynomial's coefficents:")
    print("(To end enter any nonnumber)")
    try: 
        while True:
            coefficents.append(int(input()))
    except:
         p = Polynomial(coefficents)
         plotPolynomial(p)
 

def plotPolynomial(p):
    x = np.linspace(-10, 10, num=100, endpoint=True)
    fx = p(x)
    plt.plot(x, fx)
    plt.grid()
    plt.show()
         
createPolynomial()
