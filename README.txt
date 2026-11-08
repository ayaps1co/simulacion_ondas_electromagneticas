####################################################
GENERADOR DE GRAFICAS PARA UNA ONDA ELECTROMAGNETICA
####################################################

Para ejecutar el archivo en la teminal una vez situado 
en la carpeta donde esta el programa ejecuta:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Esto instala las librerias necesarias para ejecutar la
aplicacion.
Una vez instaladas, ejecuta:

streamlit run main.py

La aplicacion se abrira en tu navegador predeterminado.

#####################################################
##########COSIDERACONES SOBRE LA APLICACION##########
#####################################################

En los cuadros de texto se puede ingresar pi y hara los
calulos usando pi como np.pi. Se deben utilizar los 
operadores aritméticos habituales: suma (+), resta (-), 
multiplicación (*), división (/) y potencia (**).


Fuera de la expresion "pi" no acepta ningun otro valor
de texto.

El angulo de elipticidad esta limitado a solo valores 
ente (-pi/4 , pi/4) y el angulo de inclinacion entre
(-pi/2, pi/2).

#####################################################
###################CASOS  AISLADOS###################
#####################################################

################POLARIZACION CIRCULAR################
En el caso en el que el angulo de elpiticidad sea pi/4 
o bien -pi/4, desaparecera la caja de texto del angulo 
de inclinacion, ya que al ser una polarizacion circular, 
no tiene sentido hablar de su inclinacion.

###############POLARIZACION  HORIZONTAL###############
En el caso que el angulo de elipticidad y el angulo
de inclinacion sea 0, ambos angulos, tanto de relacion
entre componentes como de diferencia de fases valdran 0, 
es importante mencionar esto poque la diferencia de fases
estaria indeterminada, ya que si una componente desaparece
no tendria sentido hablar sobre la diferencia de fase 
entre estas.
Aunque la aplicación devuelve numéricamente un valor de 
cero para este parámetro, esto corresponde a una convención 
computacional y no a una diferencia de fase físicamente definida.
