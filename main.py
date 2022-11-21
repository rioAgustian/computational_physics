import numpy as np  
pi = np.pi 

def nr(T, x0=5e-7, eps=1e-9, h=1e-9):
  # T = suhu
  # x0 = tebakan awal
  # eps = toleransi error
  # h = time-step
  # f(L)  adalah fungsi rapat energi
  def f(L):
    hp = 6.6261e-34                   
    c  = 2.99e8                       
    k  = 1.38e-23                      
    atas  = (8 * pi * hp * c)
    expon = (hp * c) / (L * k * T)
    bawah = (L**5*(np.exp(expon)-1))   # L = panjang gelombang
    hasil = atas/bawah
    return hasil
    
  # algoritma newton raphson
  error = 10  
  x = x0                    
  while error >= eps:
    xr    = x
    atas  = (f(x + h) - f(x - h))
    bawah = (f(x + h) - 2*f(x) + f(x - h))
    x     = x - h/2 * atas/bawah
    error = abs(xr - x)

  # menghitung hasil analitik
  x_ana = 2.989e-3 / T

  return print("Suhu = ", T, " Kelvin\n", 
               "Tebakan awal = ", x0, " meter\n\n", 
               "Panjang gelombang maksimum:\n\n", 
               "Analitik       = ", x_ana, " meter\n",
               "Newton Raphson = ", x, " meter\n")

suhu = 4000
tebakan = 5e-7 
hasil = nr(T=suhu, x0=tebakan)
print(hasil)