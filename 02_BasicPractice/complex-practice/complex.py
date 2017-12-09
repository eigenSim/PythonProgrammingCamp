#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:53:01 2017

@author: junseon
"""


class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image
        
    def __repr__(self):
        return repr('{:.2f}{:+.2f}j'.format(self.real, self.image))
    
    
    
    
    # Getter, Setter
    
    """
    def getReal(self):
        return self.real
    
    def getImage(self):
        return self.image
    
    def setReal(self, real):
        self.real = real
        
    def setImage(self, image):
        self.image = image
    """
        
    # Arithmetic Operation
    
    """
    # + operation
    def __add__(self, right_operand):
        return Complex(self.real + right_operand.real, self.image + right_operand.image)
    
    # - operation
    def __sub__(self, right_operand):
        return Complex(self.real - right_operand.real, self.image - right_operand.image)
    
    # * operation
    def __mul__(self, right_operand):
        return Complex(self.real * right_operand.real - self.image * right_operand.image, 
                       self.real * right_operand.image + self.image * right_operand.real)
    
    # / operation
    def __truediv__(self, right_operand):
        return Complex((self.real * right_operand.real + self.image * right_operand.image)/(right_operand.real**2 + right_operand.image**2), 
                       (self.image * right_operand.real - self.real * right_operand.image)/(right_operand.real**2 + right_operand.image**2)) 
    """
    
    
    
    

if __name__ == "__main__":
    
    """
    # Init two Complex objects
    c1 = Complex(1, 1)
    c2 = Complex(2, -4)
    
    # repr the Complex
    c1
    
    # Setting or Getting value in Complex objects
    c1.getReal()
    
    # Operate the Complex objects
    c_add = c1 + c2
    c_sub = c1 - c2
    c_mul = c1 * c2
    c_div = c1 / c2
    
    print("Add:" + str(c_add) + '\n' + 
          "Sub:" + str(c_sub) + '\n' + 
          "Mul:" + str(c_mul) + '\n' + 
          "Div:" + str(c_div) + '\n')
    """
    