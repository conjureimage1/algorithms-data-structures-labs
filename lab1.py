#1.1
from math import *
def f(x): #Заданная функция 
  return (2*x*x + 1.2 - cos(x))**0.5 - 1

L = 0   #Левая граница отрезка
R = 1   #Правая граница отрезка
eps = float(input()) #Погрешность вычисления
cnt  = 0

while R-L > eps:
  cnt += 1
  B = (L + R)/2       #Делим отрезок пополам
  if f(L) * f(B) > 0: #Смотрим, с каком стороны находится корень 
    L = B 
  else:
    R = B

  print(cnt, B)

print(B, f(B))



#1.2

from math import *
def f(x): #Заданная функция
  return (2*x*x + 1.2 - cos(x))**0.5 - 1

def xk(L, R): # Расчет приближения корня
  return L - ((f(L)*(R-L))/(f(R)-f(L)))


L = 0                      #Левая граница отрезка
R = 1                     #Правая граница отрезка
eps = float(input())      #Погрешность вычисления
cnt = 0

while R-L > eps:
  cnt += 1
  B = xk(L, R) #Вычисляем новое приближение
  if f(L) * f(B) > 0: #Смотрим, с каком стороны находится корень и
    L = B             #сужаем интервал
  else:
    R = B

  print(cnt, B)

print(B, f(B))
