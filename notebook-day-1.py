import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pour commencer, on va définir les paramètres physiques du booster.
    """)
    return


@app.cell
def _():
    # Constantes du modèle simplifié
    g = 1.0  # Constante de gravité 
    M = 1.0  # Masse (kg)
    l = 2.0  # Longueur (en mètres)
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Maintenant que le système est dimensionné, on passe au bilan des forces. L'unique force vient du réacteur situé à la base du booster.

    La direction de cette force par rapport à la verticale dépend de deux paramètres $\theta$ et $\phi$.

    Si on se place dans un repère global classique ($x$ vers la droite, $y
    $ vers le haut) : des angles $\theta$ et $\phi$ positifs orientent la force de poussée vers le haut et vers la gauche. On doit donc appliquer un signe négatif à la composante horizontale $f_x$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pour justifier rigoureusement l'expression de la force de poussée $\vec{f}$, on effectue une projection depuis le repère local du booster $(x', y')$ vers le repère global $(x, y)$.

    Dans le repère local $(x', y')$ lié au lanceur, la force de poussée s'exprime selon l'angle de braquage $\phi$ (avec une convention anti-horaire) :
    $$\vec{f} = f \cos(\phi) \vec{y'} - f \sin(\phi) \vec{x'}$$

    Ce qui nous donne le vecteur suivant dans la base locale :
    $$\vec{f}_{(x',y')} = \begin{pmatrix} -f \sin(\phi) \\ f \cos(\phi) \end{pmatrix}$$

    Sachant que le repère $(x', y')$ est obtenu par une rotation d'angle $\theta$ par rapport au repère global $(x, y)$, on exprime les vecteurs de la base locale $\vec{x'}$ et $\vec{y'}$ dans la base globale. On remplace ensuite dans notre expression initiale :
    $$\vec{f} = f \cos(\phi) \begin{pmatrix} -\sin(\theta) \\ \cos(\theta) \end{pmatrix}_{(x,y)} - f \sin(\phi) \begin{pmatrix} \cos(\theta) \\ \sin(\theta) \end{pmatrix}_{(x,y)}$$

    En regroupant les termes, on obtient le vecteur force dans le repère global :
    $$\vec{f} = f \begin{pmatrix} -\sin(\theta)\cos(\phi) - \sin(\phi)\cos(\theta) \\ \cos(\theta)\cos(\phi) - \sin(\theta)\sin(\phi) \end{pmatrix}$$

    Enfin, en appliquant les formules d'addition trigonométriques classiques ($\sin(a+b)$ et $\cos(a+b)$), on retombe bien sur l'expression simplifiée de notre force :
    $$\vec{f} = -f \sin(\theta + \phi) \vec{x} + f \cos(\theta + \phi) \vec{y}$$

    On implémente donc ces composantes $f_x$ et $f_y$ sous forme de variables symboliques pour la suite de la modélisation.
    """)
    return


@app.cell
def _(np):
    def f_x(f, theta, phi):
        return -f*np.sin(theta+phi)

    def f_y(f, theta, phi):
        return f*np.cos(theta+phi)

    return f_x, f_y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Simple application de la deuxième loi de Newton. Les seules forces sont la gravité et le réacteur :

    $$M\ddot{x} = f_x = -f\sin(\theta+\phi)$$
    $$M\ddot{y} = f_y - Mg = f\cos(\theta+\phi) - Mg$$

    Rien de complexe ici, mais on a vérifié le signe de la gravité (elle agit vers le bas), d'où $-Mg$ sur la composante $y$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le propulseur est une tige uniforme de longueur totale $\ell$ tournant autour de son centre. Formule classique :

    $$J = \frac{M\ell^2}{12} $$

    Numériquement :
    """)
    return


@app.cell
def _(M, l):
    J = M * l**2 / 12.0
    print(J)
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On passe maintenant à la dynamique de rotation du système. Pour cela, on applique le Théorème du Moment Cinétique (TMC) au centre de masse (noté CM ou $O$) :
    $$J\ddot{\theta} = \sum \mathcal{M}_{CM}(\vec{F}_{ext})$$

    Le poids s'appliquant directement au centre de gravité, son moment est nul ($\mathcal{M}_{CM}(\vec{P}) = 0$). Il ne nous reste donc qu'à calculer le couple généré par la force du réacteur appliquée à la base du booster (qu'on note point $B$).

    Le vecteur position de la base par rapport au centre de masse s'écrit :
    $$\vec{OB} = \frac{\ell}{2} \begin{pmatrix} \sin(\theta) \\ -\cos(\theta) \end{pmatrix}_{(\vec{x},\vec{y})}$$

    Le couple en 2D correspond à la composante sur l'axe $z$ du produit vectoriel $\vec{OB} \wedge \vec{f}$, soit $\tau = r_x f_y - r_y f_x$. En développant avec les composantes de la force trouvées précédemment :
    $$\mathcal{M}_{CM}(\vec{f}) = \left(\frac{\ell}{2}\sin(\theta)\right) \left(f\cos(\theta+\phi)\right) - \left(-\frac{\ell}{2}\cos(\theta)\right) \left(-f\sin(\theta+\phi)\right)$$

    On factorise par $\frac{\ell f}{2}$ :
    $$\mathcal{M}_{CM}(\vec{f}) = \frac{\ell f}{2} \big[ \sin(\theta)\cos(\theta+\phi) - \cos(\theta)\sin(\theta+\phi) \big]$$

    On reconnaît l'identité trigonométrique classique $\sin(a-b) = \sin(a)\cos(b) - \cos(a)\sin(b)$. Ce qui simplifie grandement l'expression :
    $$\mathcal{M}_{CM}(\vec{f}) = \frac{\ell f}{2} \sin\big(\theta - (\theta+\phi)\big) = -\frac{f\ell}{2}\sin(\phi)$$

    On obtient donc notre équation différentielle pour la rotation :
    $$J\ddot{\theta} = -\frac{f\ell}{2}\sin(\phi)$$
    *(Où $J = \frac{M\ell^2}{12}$).*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Nous avons 3 EDO du second ordre ($x$, $y$, $\theta$), soit $n = 6$ après conversion en premier ordre.

    État : $s = (x, v_x, y, v_y, \theta, \omega)$ où $v_x = \dot{x}$, $v_y = \dot{y}$, $\omega = \dot{\theta}$.

    $$\dot{s} = F(s, f, \phi) = \begin{pmatrix} v_x \\ -f\sin(\theta+\phi)/M \\ v_y \\ f\cos(\theta+\phi)/M - g \\ \omega \\ -lf\sin(\phi)/J \end{pmatrix}$$
    """)
    return


@app.cell
def _(J, M, f_x, f_y, g, l, np):
    def s(x, v_x, y, v_y, theta, omega):
        return [x, v_x, y, v_y, theta, omega]

    def F(s: list, f, phi):
        x, v_x, y, v_y, theta, omega = s
        return [
            v_x,
            f_x(f, theta, phi)/M,
            v_y,
            f_y(f, theta, phi)/M - g,
            omega,                 
            -f*l/(2*J) * np.sin(phi) 
        ]

    return (F,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell
def _(F):
    from scipy.integrate import solve_ivp

    def redstart_solve(t_span, y0, f_phi):
        def dynamics(t, y):
            f, phi = f_phi(t, y)
            return F(y, f, phi)
    
        result = solve_ivp(
            dynamics,
            t_span,
            y0,
            method="RK45",
            dense_output=True,
            rtol=1e-9,
            atol=1e-9,
        )
    
        def sol(t):
            return result.sol(t)
    
        return sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Avec $f = 0$, pas de poussée, chute libre pure. Le mouvement vertical est simplement :

    $$y(t) = y_0 - \frac{g}{2}t^2 = 10 - \frac{t^2}{2}$$

    On veut $y(t^*) = \ell = 2$ :

    $$10 - \frac{t^{*2}}{2} = 2 \implies t^{*2} = 16 \implies t^* = 4 \text{ s}$$

    Vérifions avec la simulation :
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pour cet atterrissage contrôlé, on a préféré poser le problème analytiquement sur le papier. L'idée est de trouver une loi de commande affine pour la poussée : $f(t) = at + b$.

    En isolant la dynamique sur l'axe vertical (et sachant que $M=1$ et $g=1$), le Principe Fondamental de la Dynamique nous donne :
    $$\ddot{y} = at + b - 1$$

    On intègre une première fois pour obtenir la vitesse. En sachant qu'à l'instant initial $t=0$, la fusée chute à $\dot{y}(0) = -2$ m/s, on trouve notre première constante d'intégration :
    $$\dot{y}(t) = a\frac{t^2}{2} + bt - t - 2$$

    On intègre une seconde fois pour la position. À $t=0$, l'altitude initiale est $y(0) = 10$ m. Ce qui nous donne :
    $$y(t) = a\frac{t^3}{6} + b\frac{t^2}{2} - \frac{t^2}{2} - 2t + 10$$

    L'objectif est d'atterrir en douceur à $t=5$ s. "En douceur" signifie deux choses :
    1. **La vitesse doit être nulle :** $\dot{y}(5) = 0$
    2. **Le booster doit toucher le sol :** $y(5) = \ell/2 = 1$ m

    En injectant $t=5$ dans nos deux équations intégrées, on se retrouve avec un système linéaire classique de la forme $A \begin{pmatrix} a \\ b \end{pmatrix} = B$.

    Après avoir isolé $a$ et $b$ à gauche, on obtient exactement la matrice $A$ et le vecteur $B$ implémentés dans le code ci-dessous :
    - $A = \begin{pmatrix} 25/2 & 5 \\ 125/6 & 25/2 \end{pmatrix}$
    - $B = \begin{pmatrix} 7.0 \\ 13.5 \end{pmatrix}$

    Il ne reste plus qu'à laisser `numpy.linalg.solve` faire le travail ingrat de l'inversion matricielle pour extraire les coefficients $a$ et $b$, puis simuler la trajectoire.
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    def controlled_landing():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]  # [x, vx, y, vy, theta, omega]

        # Exact coefficients from the linear system
        A_mat = np.array([[25/2, 5], [125/6, 25/2]])
        rhs   = np.array([7.0, 13.5])
        a, b  = np.linalg.solve(A_mat, rhs)

        def f_phi(t, y):
            return np.array([a * t + b, 0.0])     # [f, phi]

        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        vy_t = sol(t)[3]

        fig, axes = plt.subplots(1, 2, figsize=(14, 4))
        ax = axes[0]
    
        ax.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        ax.plot(t, l * np.ones_like(t),   color="grey",   ls="--", label=r"$y = \ell = 2$ m")
        ax.plot(t, l/2 * np.ones_like(t), color="crimson", ls="--", label=r"$y = \ell/2 = 1$ m (ground)")
        ax.scatter([5], [l/2], color="crimson", zorder=5, label=rf"landing target $(t=5,\ y=1)$")
        ax.set_title("Controlled Landing")
        ax.set_xlabel("time $t$ (s)")
        ax.set_ylabel("$y$ (m)")
        ax.grid(True)
        ax.legend()

        ax = axes[1]
        ax.plot(t, vy_t, color="seagreen", label=r"$\dot{y}(t)$")
        ax.scatter([5], [0], color="crimson", zorder=5, label=r"target $\dot{y}(5)=0$")
        ax.axhline(0, color="grey", ls="--")
        ax.set_title(r"Vertical velocity $\dot{y}(t)$")
        ax.set_xlabel("time $t$ (s)")
        ax.set_ylabel(r"$\dot{y}$ (m/s)")
        ax.legend(fontsize=8); ax.grid(True)

        return plt.gcf()

    controlled_landing()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return animate_transform, svg, transform


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La fonction world configure la scène SVG.

    La partie délicate est l'inversion de l'axe $y$ : SVG a l'axe  $y$ pointant vers le bas, mais on veut des coordonnées cartésiennes (y vers le haut).

    On gère cela avec un $scale(1, -1)$ dans un groupe translaté.
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box
        w = x_max - x_min
        h = y_max - y_min
        sky    = svg.rect(x=x_min, y=y_min, width=w, height=h,      fill="lightskyblue")
        ground = svg.rect(x=x_min, y=y_min, width=w,
                          height=(-y_min if y_min < 0 else h - y_max), fill="sienna")
        pad    = svg.rect(x=-1, y=-0.1, width=2, height=0.1,         fill="green")
        content = transform.translate(x=-x_min, y=y_max)(
            transform.scale(x=1, y=-1)(
                sky, ground, pad, *objects
            )
        )
        return str(svg.svg(viewBox=f"0 0 {w} {h}", xmlns="http://www.w3.org/2000/svg")(content))

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        body_w = 0.15
        body_h = l
        flame_scale = l / (2 * M * g)  # flame_len = l/2 when f = Mg
        flame_len = f * flame_scale
    
        body = svg.rect(x=-body_w/2, y=0, width=body_w, height=body_h, fill="gray")
    
        flame_group = ""
    
        if flame_len > 0:
        
            flame = svg.rect(x=-body_w/2, y=-flame_len, width=body_w, height=flame_len, fill="orange")
        
            flame_group = str(transform.rotate(a=-np.degrees(phi), x=0, y=0)(flame))
    
        deg = -np.degrees(theta)
    
        return str(
            transform.translate(x=x, y=y)(
                transform.rotate(a=deg, x=0, y=0)(
                    transform.translate(x=0, y=-l/2)(
                        body, flame_group
                    )
                )
            )
        )

    return (booster,)


@app.cell
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x_fn, y_fn, theta_fn, f_fn, phi_fn, T=5.0):
        body_w = 0.15
        body_h = l
        flame_scale = l / (2 * M * g)
        body = svg.rect(x=-body_w/2, y=0, width=body_w, height=body_h, fill="gray")
        flame_base = svg.rect(x=-body_w/2, y=-1, width=body_w, height=1, fill="orange")
        animated_flame = animate_transform.scale(
            x=1,
            y=lambda t: f_fn(t) * flame_scale,
            T=T
        )(
            animate_transform.rotate(
                a=lambda t: -np.degrees(phi_fn(t)),
                T=T
            )(flame_base)
        )
        inner = animate_transform.translate(x=0, y=lambda t: -l, T=T)(body, animated_flame)
        rotated = animate_transform.rotate(a=lambda t: -np.degrees(theta_fn(t)), T=T)(inner)
        positioned = animate_transform.translate(x=x_fn, y=y_fn, T=T)(rotated)
        return str(positioned)

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, mo, np, world):
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell
def _(booster_anim, l, np, plt, redstart_solve):
    def make_anim(y0, f_val, phi_val, T=5.0):
        def f_phi_const(t, y):
            return np.array([f_val, phi_val])
    
        sol = redstart_solve([0.0, T], y0, f_phi_const)
        return booster_anim(
            lambda t: sol(t)[0], lambda t: sol(t)[2] + 1,
            lambda t: sol(t)[4], lambda t: f_val,
            lambda t: phi_val, T=T
        )
    
    y0_std = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

    A_mat = np.array([[25/2, 5], [125/6, 25/2]])
    rhs   = np.array([7.0, 13.5])
    a, b  = np.linalg.solve(A_mat, rhs)

    # scenario 4: controlled landing
    def f_phi_land(t, y):
        return np.array([a*t + b, 0.0])

    sol_l = redstart_solve([0,5], [0,0,10,-2,0,0], f_phi_land)

    t = np.linspace(0, 8, 1000)

    y_t = sol_l(t)[2]
    plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
    plt.plot(t, l/2 * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
    plt.title("Free Fall")
    plt.xlabel("time $t$")
    plt.grid(True)
    plt.legend()
    plt.gcf()
    return a, b, make_anim, sol_l, y0_std


@app.cell
def _(M, a, b, booster_anim, g, l, make_anim, mo, np, sol_l, world, y0_std):
    anim4 = booster_anim(
        lambda t: sol_l(t)[0], lambda t: sol_l(t)[2] + l/2,
        lambda t: sol_l(t)[4], lambda t: a*t + b,
        lambda t: 0.0, T=5.0
    )

    mo.md("### Animated scenarios 1–4")
    vb = [-5, 5, -2, 12]
    mo.hstack([
        mo.Html(world(vb, make_anim(y0_std, 0, 0))),
        mo.Html(world(vb, make_anim(y0_std, M*g, 0))),
        mo.Html(world(vb, make_anim(y0_std, M*g, np.pi/8))),
        mo.Html(world(vb, anim4)),
    ], justify="space-around")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
