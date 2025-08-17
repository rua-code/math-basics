#nural newtwor that predict if a person will pay a product passed on his income.
import numpy as np
X = np.array([[0.5, 0.2],   
              [0.9, 0.8],  
              [0.4, 0.5],   
              [0.7, 0.3]])  

y = np.array([[0], [1], [0], [1]])# real data 0=> did not pay , 1=> pay

def sigmoid(z): # return any value in range 1-0 عشان نتعامل معها ع اساس الاحتمالات 
 return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
    s = sigmoid(z)         
    return s * (1 - s) 
