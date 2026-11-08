import plotly.graph_objects as go
import numpy as np
import solver as solver

pi = np.pi

def crear_botones(d):
    updatemenus = [dict(
            type = "buttons",
            showactive = False,
            active = -1,
            bgcolor ="#6185E7",
            bordercolor = "#2E4C9E",
            font=dict(
                color= "white",
                size= 13,
                family = "Courier New"
            ),                
            buttons = [
                dict(
                    args = [None, {"frame": {"duration": d, "redraw": True},
                                    "fromcurrent": True, "transition": {"duration": d}}],
                    label = "▶ Play",
                    method = "animate",

                )])]
    return updatemenus

def polarization(A, sigma, omega, k, ax,  delta_alpha):
    N = 100 # cantidad de muestras temporales
    t = np.linspace(0, 2*np.pi/omega, N) # genera 1000 valores de tiempo que abarca un periodo de tiempo completo
    z = 0
    d = (2*pi/omega)*1000/N

    x, y= solver.components(A, sigma, omega, t, k, z, ax, delta_alpha)# calculos sobre el arreglo de muestras temporales
    #xx, yy = solver.components(A, sigma, omega, t, k, z, ax, delta_alpha)
    


    #definimos los maximos y minimos de la trayectoria que el scatter seguira
    xmax = np.max(x)
    ymax = np.max(y)
    xmin = np.min(x)
    ymin = np.min(y)

    fig = go.Figure(data=[
                        go.Scatter(
                            x=x,
                            y=y,
                            mode='lines',
                            name="Polarizacion",
                            marker=dict(color="#6185E7"),
                            ),
                        go.Scatter(
                            x=[x[0]], 
                            y=[y[0]],
                            mode="markers",
                            name="Trayectoria del campo electrico",
                            marker=dict(color="blue", size=10))
                        ]
                    )
    fig.update_layout(width=600, height=450,
        xaxis=dict(range=[-A, A], autorange=False, zeroline=False, title = 'Ex'),
        yaxis=dict(range=[-A, A], autorange=False, zeroline=False, title = 'Ey'),
        title_text="Polarizacion", title_x=0.5,
        updatemenus = crear_botones(d)
        )
    
    fig.update(frames=[go.Frame(
                        data=[go.Scatter(
                                   x=[x[k]],
                                   y=[y[k]])],
                        traces=[1]) # fig.data[1] is updated by each frame
        for k in range(N)])
    
    fig.update_layout(
        yaxis=dict(
            scaleanchor="x",
            scaleratio=1
        )
    )
    return fig

def prop(A, sigma, omega, k, ax, delta_alpha):
    N = 100
    t = np.linspace(0, 2*np.pi/omega, N)
    z = np.linspace(0, 4*(2*np.pi/k), N)

    Z, T = np.meshgrid(z, t)

    d = (8*np.pi/omega)*1000/N

    x, y = solver.components(
        A, sigma, omega, T, k, Z, ax, delta_alpha
    )

    zmax, zmin = np.max(z), np.min(z)

    fig = go.Figure(data=[
        go.Scatter3d(
            x=x[0, :],
            y=z,
            z=y[0, :],
            mode='lines',
            marker=dict(color="#6185E7")
        )
    ])

    fig.update_layout(
        width=600,
        height=450,
        scene=dict(
            xaxis=dict(range=[-A, A], autorange=False, title = 'Ex'),
            yaxis=dict(range=[zmin, zmax], autorange=False, title = 'Eje Propagacion (z)'),
            zaxis=dict(range=[-A, A], autorange=False, title = 'Ey'),
            aspectmode="manual",
            aspectratio=dict(x=1, y=2, z=1)
        ),
        title_text="Propagación 3D",
        title_x=0.5,
        updatemenus = crear_botones(d)
    )

    fig.update(frames=[
        go.Frame(
            data=[go.Scatter3d(
                x=x[j, :],
                y=z,
                z=y[j, :],
                mode='lines'
            )],
            traces=[0]
        )
        for j in range(N)
    ])

    return fig

def prop_x(A, sigma, omega, k, ax, delta_alpha):
    N = 100
    t = np.linspace(0, 2*np.pi/omega, N)
    z = np.linspace(0, 4*(2*np.pi/k), N)
   
    Z, T = np.meshgrid(z, t)

    # Tiempo de cada frame para mantener la velocidad de fase
    d = (8*np.pi/omega)*1000/N

    
    x, _ = solver.components(
        A, sigma, omega, T, k, Z, ax, delta_alpha
    )
    cero = np.zeros(N)

    zmax, zmin = np.max(z), np.min(z)
    
    fig = go.Figure(data=[
        go.Scatter3d(
            x=x[0, :], y=z, z=cero,
            mode='lines',
            marker=dict(color="#6185E7")
        )
    ])

    fig.update_layout(
        width=600,
        height=450,
        scene=dict(
            xaxis=dict(range=[-A, A], autorange=False, title= 'Ex'),
            yaxis=dict(range=[zmin, zmax], autorange=False, title = 'Eje Propagacion (z)'),
            zaxis=dict(range=[-A, A], autorange=False, title = 'Ey'),
            aspectmode="manual",
            aspectratio=dict(x=1, y=2, z=1)
        ),
        title_text="Propagación Componente Ex",
        title_x=0.5,
        updatemenus = crear_botones(d)
    )

    fig.update(frames=[
        go.Frame(
            data=[go.Scatter3d(
                x=x[j, :],
                y=z,
                z=cero,
            )],
            traces=[0]
        )
        for j in range(N)
    ])

    return fig

def prop_y(A, sigma, omega, k, ax, delta_alpha):
    N = 100
    t = np.linspace(0, 2*np.pi/omega, N)
    z = np.linspace(0, 4*(2*np.pi/k), N)
   
    Z, T = np.meshgrid(z, t)

    # Tiempo de cada frame para mantener la velocidad de fase
    d = (8*np.pi/omega)*1000/N

    
    _, y = solver.components(
        A, sigma, omega, T, k, Z, ax, delta_alpha
    )
    cero = np.zeros(N)

    zmax, zmin = np.max(z), np.min(z)
    
    fig = go.Figure(data=[
        go.Scatter3d(
            x=cero, y=z, z=y[0, :],
            mode='lines',
            marker=dict(color="#ED3B3B")
        )
    ])

    fig.update_layout(
        width=600,
        height=450,
        scene=dict(
            xaxis=dict(range=[-A, A], autorange=False, title= 'Ex'),
            yaxis=dict(range=[zmin, zmax], autorange=False, title = 'Eje Propagacion (z)'),
            zaxis=dict(range=[-A, A], autorange=False, title = 'Ey'),
            aspectmode="manual",
            aspectratio=dict(x=1, y=2, z=1)
        ),
        title_text="Propagación Componente Ey",
        title_x=0.5,
        updatemenus = crear_botones(d)
    )

    fig.update(frames=[
        go.Frame(
            data=[go.Scatter3d(
                x=cero,
                y=z,
                z=y[j, :],
            )],
            traces=[0]
        )
        for j in range(N)
    ])

    return fig

def prop_components(A, sigma, omega, k, ax, delta_alpha):
    N = 100
    t = np.linspace(0, 2*np.pi/omega, N)
    z = np.linspace(0, 4*(2*np.pi/k), N)

    Z, T = np.meshgrid(z, t)

    # Tiempo de cada frame para mantener la velocidad de fase
    d = (8*np.pi/omega)*1000/N

    x, y = solver.components(
        A, sigma, omega, T, k, Z, ax, delta_alpha
    )

    cero = np.zeros(N)

    xmax, xmin = np.max(x), np.min(x)
    ymax, ymin = np.max(z), np.min(z)
    zmax, zmin = np.max(y), np.min(y)

    fig = go.Figure(data=[
        # Componente Ex
        go.Scatter3d(
            x=x[0, :],
            y=z,
            z=cero,
            mode='lines',
            name="Componente Ex",
            marker=dict(color="#6185E7")
        ),

        # Componente Ey
        go.Scatter3d(
            x=cero,
            y=z,
            z=y[0, :],
            mode='lines',
            name="Componente Ey",
            marker=dict(color="#ED3B3B")
        )
    ])

    fig.update_layout(
        width=600,
        height=450,
        scene=dict(
            xaxis=dict(range=[-A, A], autorange=False,
                       title="Ex"),
            yaxis=dict(range=[ymin, ymax], autorange=False,
                       title="Propagación (z)"),
            zaxis=dict(range=[-A, A], autorange=False,
                       title="Ey"),
            aspectmode="manual",
            aspectratio=dict(x=1, y=2, z=1)
        ),
        title_text="Comparacion componentes Ex y Ey",
        title_x=0.5,
        updatemenus = crear_botones(d)
    )

    fig.update(frames=[
        go.Frame(
            data=[
                go.Scatter3d(
                    x=x[j, :],
                    y=z,
                    z=cero
                ),
                go.Scatter3d(
                    x=cero,
                    y=z,
                    z=y[j, :]
                )
            ],
            traces=[0, 1]
        )
        for j in range(N)
    ])

    return fig
