import numpy

A = numpy.ones((3,2))
print(A)
print(type(A))
B = numpy.zeros((2,3))
print(B)
a = numpy.linspace(-1.0,1.0,5)
print(a)
print(type(a))
b = numpy.arange(0,10,2)
print(b)

C = numpy.array([[1.0,2.0],[-1.0,-1.0],[0.0,2.0]])
print(C)
print(C.shape)
print(C[1,0])
print(C[0:2,:])  # 提取矩阵C的0、1两行和所有列形成的子矩阵

d = numpy.arange(0,16)
print(d)
D = d.reshape((4,4))
print(D)
print(D[1:3,1:3])
DT = D.transpose()
print(DT)

sin_D = numpy.sin(D)
print(sin_D)
E = sin_D*10
print(E)
print(numpy.around(E))
print(numpy.amax(E))
print(numpy.mean(E))

v1 = numpy.array([1.0,2.0,3.0])
v2 = numpy.array([2.0,1.0,-1.0])
print(numpy.inner(v1,v2))
F = numpy.random.rand(4,3)
print(F)
print(F@v1)
v1T = v1.reshape((3,1))
print(v1T)
print(F@v1T)

#####################################################################

import numpy

# set parameters
N_train = 100
N_test = 20
degree = 7

# target function
f = lambda x: numpy.sin(2*numpy.pi*x)

# generate training/testing sets
x_train = numpy.random.uniform(-1.0,1.0,N_train)
x_test = numpy.random.uniform(-1.0,1.0,N_test)
y_train = f(x_train)
y_test = f(x_test)

# Solve least square problem
A = numpy.zeros((N_train,degree+1))
for i in range(0,N_train): # i =0,1,...,N_train-1
    for j in range(0,degree+1): # j=0,1,...,degree
        A[i,j] = x_train[i]**j
b = y_train
# b = y_train.reshape((N_train,1))
solution = numpy.linalg.lstsq(A,b)
coeff = solution[0]

# Plot
from matplotlib.pyplot import plot
N_plot = 100
x_plot = numpy.linspace(-1,1,N_plot)
poly_plot = numpy.zeros((N_plot,))
for j in range(0,degree+1):
    poly_plot = poly_plot + coeff[j]*x_plot**j
plot(x_plot,poly_plot,'k-')
plot(x_train,y_train,'b.')

poly_test = numpy.zeros((N_test,))
for j in range(0,degree+1):
    poly_test = poly_test + coeff[j]*x_test**j
error_test = numpy.sqrt(numpy.sum((poly_test-y_test)**2)/N_test)
print('Test error = %.3g' % error_test)







