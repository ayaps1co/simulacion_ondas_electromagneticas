import ast
import numpy as np
import operator as op
import streamlit as st
import solver as solver
import graphs as graphs

operaciones = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow
}

def evaluar(expresion):

    def resolver(nodo):

        # Números
        if isinstance(nodo, ast.Constant):
            return nodo.value

        # Pi
        elif isinstance(nodo, ast.Name) and nodo.id == "pi":
            return np.pi

        # Operaciones binarias
        elif isinstance(nodo, ast.BinOp):
            operacion = operaciones[type(nodo.op)]

            izquierda = resolver(nodo.left)
            derecha = resolver(nodo.right)

            return operacion(izquierda, derecha)

        # Números negativos
        elif isinstance(nodo, ast.UnaryOp):
            valor = resolver(nodo.operand)

            if isinstance(nodo.op, ast.USub):
                return -valor

            elif isinstance(nodo.op, ast.UAdd):
                return valor

        raise ValueError("Expresión no permitida")

    arbol = ast.parse(expresion, mode="eval")

    return resolver(arbol.body)

def graficas(A, ax, k, omega, epsilon, psi):
    A = evaluar(A)
    ax = evaluar(ax)
    k = evaluar(k)
    omega = evaluar(omega)
    epsilon = evaluar(epsilon)
    psi = evaluar(psi)
    
    sigma, delta_alpha = solver.solve_sigma(epsilon, psi)
    fig_polarization = graphs.polarization(A, sigma, omega, k, ax, delta_alpha)
    fig_prop = graphs.prop(A, sigma, omega, k, ax, delta_alpha)
    fig_prop_y = graphs.prop_y(A, sigma, omega, k, ax, delta_alpha)
    fig_prop_x = graphs.prop_x(A, sigma, omega, k, ax, delta_alpha)
    fig_prop_components = graphs.prop_components(A, sigma, omega, k, ax, delta_alpha)
    
    st.markdown(r"El ángulo $\sigma$ que determina la relacion entre las componentes: ")
    st.write(str(sigma))
    st.markdown(r"El ángulo $\Delta\alpha$ que determina la diferencia de fases:")
    st.write(str(delta_alpha))
    st.plotly_chart(fig_polarization)
    st.plotly_chart(fig_prop)
    st.plotly_chart(fig_prop_x)
    st.plotly_chart(fig_prop_y)
    st.plotly_chart(fig_prop_components)