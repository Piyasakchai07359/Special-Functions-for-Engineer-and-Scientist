'''
This program show how to calculate factorial where order of factorial is not only integer but include decimal number.

we know => 'gamma_function(order_factorial+1)=order_factorial!'
'''

import scipy as sp

order_factorial=3.67

order_gamma_function=order_factorial+1
result=sp.special.gamma(order_gamma_function)
print('This is result of gamma function to calculate factorial order {} = {}'.format(order_factorial,result))