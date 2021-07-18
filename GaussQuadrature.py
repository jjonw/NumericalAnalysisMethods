# Programas para calcular quadratura de Gauss
# Obs: para utilizar funções da biblioteca math, importe-as antes 
#
from math import sqrt, cos, sin, pi

def gaussLegendre(func, quad):
    #x**3 + x**2 + x + 1
    #1/(3+x)   
    # 0.5*math.log(2 - 2*((1+x)/2)**2)   
    # 0.5*math.sin(math.pi*(1+x)/2)/(1 - ((1+x)/2)**2)
    
    f = func
    n = quad   # quadratura 
    integral = 0

    x = [[0.], 
         [sqrt(3)/3., -sqrt(3)/3.],
         [sqrt(3./5), -sqrt(3./5), 0],
         [sqrt((3. - 2*sqrt(6/5)) / 7), -sqrt((3. - 2*sqrt(6/5)) / 7),
          sqrt((3. + 2*sqrt(6/5)) / 7), -sqrt((3. + 2*sqrt(6/5)) / 7)],
          [0, sqrt(5. - 2*sqrt(10/7)) / 3, -sqrt(5. - 2*sqrt(10/7)) / 3,
           sqrt(5. + 2*sqrt(10/7)) / 3, -sqrt(5. + 2*sqrt(10/7)) / 3]
          ]
          
    a = [[2.], 
         [1., 1.], 
         [5./9, 5./9, 8./9], 
         [(18+sqrt(30))/36, (18+sqrt(30))/36, (18-sqrt(30))/36, (18-sqrt(30))/36], 
         [128./225, (322. + 13*sqrt(70))/900, (322. + 13*sqrt(70))/900, 
          (322. - 13*sqrt(70))/900, (322. - 13*sqrt(70))/900,]]

    for i in range(n):
        integral += a[n-1][i]*f(x[n-1][i])
        print("integral ", i+1, a[n-1][i], " ", f(x[n-1][i]))
    
    print("Integral = %.20f" % integral)
    
    
def gaussChebyshev(func, quad, caso):
    #0.5 * ( log(2 - ((1+x)/2)**2) / sqrt(1 - ((1+x)/2)**2) )  
    #sqrt(1 - ((3 + x)/2)**2) / (3 + x)
    # 0.5 * ( log(2 - ((1+x)/2)**2) / sqrt(1 - ((1+x)/2)**2) )  
    # 0.5 * ( sin(pi * ((1+x)/2)) / sqrt(1 - ((1+x)/2)**2))    
    # (x**3 + x**2 + x + 1) / sqrt(1 - x**2)
    
    # caso 1: f(x)/sqrt(1-x^2)
    # caso 2: f(x)*sqrt(1-x^2)
    f = func
    n = quad # quadratura
    integral = 0

    if caso == 1:
        a = (pi/n)
        for i in range(n):
            xi = cos((2*i + 1)/(2*n) * pi)
            integral += a * f(xi)
            print("&+ %.10f * %0.10f + \\\\" % (a, f(xi)))
        
    elif caso == 2:
        ti = (pi/(n+1))
        for i in range(n):
            xi = cos((1+i) * ti)
            ai = (pi)/(n+1)*(sin(ti * (i+1)))**2
            integral += ai * f(xi)
            print("&+ %.10f * %0.10f + \\\\" % (ai, f(xi)))

    print("Integral = %.10f" % integral)
        
        
def gaussLaguerre(func, quad):
    #2 * e**(-pi*sqrt(x) + x) / (2 + x**2)   
    # e**(x - sqrt(x)) / (1 + x**2)  
    # (x**3 + 4*x + 2  )
    # 1/(x+1)
    n = quad
    f = func
    integral = 0
    
    # quadratura comeca em 2, por isso o a[n-2]
    x = [[0.585786, 3.41421],
         [0.415775, 2.29428, 6.28995],
         [0.322548, 1.74576, 4.53662, 9.39507]]
    
    a = [[0.853553, 0.146447],
         [0.711093, 0.278518, 0.0103893],
         [0.603154, 0.357419, 0.0388879, 0.000539295]
         ]
    
    for i in range(n):
        integral += a[n-2][i] * f(x[n-2][i])
        print("&+ %.6f * %0.6f + \\\\" % (a[n-2][i], f(x[n-2][i])))
        
    
    print("Integral = %.6f" % integral)
    
    
def gaussHermite(func, quad):
#0.5*(e**(-sqrt(abs(x)) + x**2)/(1 + x**2))   
#e**(-abs(x) + x**2)*cos(x)  
#e**(-pi * sqrt(abs(x)) + x**2)/(2 + x**2)    
#sin(x)
    f = func
    n = quad
    integral = 0 
    
    x = [[sqrt(2)/2., -sqrt(2)/2.],
          [0, sqrt(6)/2., -sqrt(6)/2.],
          [sqrt((3 - sqrt(6))/2), -sqrt((3 - sqrt(6))/2),
           sqrt((3 + sqrt(6))/2), -sqrt((3 + sqrt(6))/2)]
        ]
    
    a = [[sqrt(pi)/2, sqrt(pi)/2],
         [(2 * sqrt(pi))/3, sqrt(pi)/6,
          sqrt(pi)/6],
         [sqrt(pi) / (4 * (3 - sqrt(6))), 
          sqrt(pi) / (4 * (3 - sqrt(6))),
          sqrt(pi) / (4 * (3 + sqrt(6))),
          sqrt(pi) / (4 * (3 + sqrt(6)))]
        ]
    
    for i in range(n):
        integral += a[n-2][i] * f(x[n-2][i])
        print("&+ %.6f * %0.10f + \\\\" % (a[n-2][i], f(x[n-2][i])))    
    
    print("Integral = %0.10f" % integral)
