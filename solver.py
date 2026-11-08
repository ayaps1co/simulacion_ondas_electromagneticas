import numpy as np
pi =  np.pi

def solve_sigma(epsilon, psi):
    if -pi/4 < epsilon < pi/4:
        if -pi/2 <= psi <= pi/2:
          
            a = np.cos(2*psi)*np.cos(2*epsilon)
            sigma = (1/2)*(np.arccos(a))

            y = np.sin(2*epsilon)
            x = np.cos(2*epsilon) * np.sin(2*psi)

            delta_alpha = np.arctan2(y, x)

        else:
            raise ValueError("Psi fuera del intervalo permitido")
    # En los siguientes casos no tiene sentido hablar sobre psi por lo que no usaremos su informacion para los calculos 
    
    elif epsilon == pi/4:
        sigma = pi/4
        delta_alpha = pi/2

    elif epsilon == -pi/4:
        sigma = pi/4
        delta_alpha = -pi/2
    #Cuando ambos son 0 no existe diferencia de fase por lo que delta alpha es 0 
    # y tambien el angulo que relaciona las componentes sera 0 porque no es util hablar de 2 componentes si una no existe
    elif epsilon == psi == 0:
        sigma = 0
        delta_alpha = 0
    else:
        raise ValueError("Epsilon fuera del intervalo permitido")
    ans = (sigma, delta_alpha)
    return ans

def components(A, sigma, omega, t, k, z, ax,  delta_alpha):
    Ax = A * np.cos(sigma)
    Ay = A * np.sin(sigma)
    
    ay = delta_alpha + ax

    Ex = Ax* np.cos(k*z - omega * t + ax)
    Ey = Ay* np.cos(k*z - omega * t + ay)

    return Ex, Ey
