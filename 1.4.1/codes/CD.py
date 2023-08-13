import numpy as np



#vertices of triangle
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])
#direction vector
def dir_vec(C,B):
  return B-C
def sum_vec(C,B):
  return (C+B)/2
print("the perpendicular bisector of AB is:x-",sum_vec(B,A),dir_vec(B,A),"=0")
print("the perpendicular bisector of BC is:x-",sum_vec(C,B),dir_vec(C,B),"=0")
print("the perpendicular bisector of CA is:x-",sum_vec(A,C),dir_vec(A,C),"=0")
D=sum_vec(A,B)
