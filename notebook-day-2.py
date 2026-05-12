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

    return la, np, plt, sci, scipy


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
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
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
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
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
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
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

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
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
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

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Un système est à l'équilibre si et seulement si toutes ses accélérations sont parfaitement nulles. On pose donc logiquement $\ddot{x} = 0$, $\ddot{y} = 0$ et $\ddot{\theta} = 0$ à partir de nos équations du mouvement, et on résout le système.

    **1. Équilibre sur l'axe horizontal ($x$) :**
    L'équation nous donne :
    $$M\ddot{x} = -f\sin(\theta+\phi) = 0$$
    On a $f > 0$. Par conséquent, c'est le terme en sinus qui doit s'annuler, soit $\sin(\theta+\phi) = 0$.
    Sachant que les angles sont physiquement contraints par $|\theta| < \pi/2$ et $|\phi| < \pi/2$, on a l'encadrement $-\pi < \theta+\phi < \pi$. Sur cet intervalle, la seule solution possible pour annuler le sinus est :
    $$\theta + \phi = 0$$

    **2. Équilibre sur l'axe vertical ($y$) :**
    On passe à l'altitude :
    $$M\ddot{y} = f\cos(\theta+\phi) - Mg = 0$$
    Puisque l'on vient de démontrer que $\theta + \phi = 0$, le cosinus vaut tout simplement 1. L'équation se simplifie de manière triviale :
    $$f = Mg$$
    La physique est bien faite : pour ne pas tomber, la poussée doit exactement compenser le poids du lanceur.

    **3. Équilibre en rotation ($\theta$) :**
    Enfin, pour éviter que le booster ne se mette à tournoyer sur lui-même :
    $$J\ddot{\theta} = -\frac{f\ell}{2}\sin(\phi) = 0$$
    Comme $f = Mg > 0$ et que $\ell$ est une longueur non nulle, c'est obligatoirement $\sin(\phi)$ qui s'annule. Avec la contrainte $|\phi| < \pi/2$, on en déduit directement :
    $$\phi = 0$$
    Et comme on avait établi plus haut que $\theta + \phi = 0$, on trouve inévitablement $\theta = 0$.

    **Conclusion sur l'état d'équilibre :**
    Sans grande surprise, la seule configuration permettant un vol stationnaire (Hovering) correspond à un lanceur parfaitement vertical, sans braquage de la tuyère, avec une poussée égale à son poids. L'unique point d'équilibre $(x_e, y_e, \theta_e, f_e, \phi_e)$ est donc caractérisé par :
    $$s = (x, 0, y, 0, 0, 0),$$
    $$f = Mg \quad ; \quad \theta = 0 \quad ; \quad \phi = 0$$
    *(Note : les positions $x$ et $y$ peuvent être quelconques, le système est invariant par translation spatiale).*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On introduit nos variables d'erreur (les $\Delta$) autour du point d'équilibre stationnaire qu'on vient de trouver ($\theta_e = 0$, $f_e = Mg$, $\phi_e = 0$) :
    $$x = x_e + \Delta x \quad ; \quad y = y_e + \Delta y \quad ; \quad \theta = \Delta\theta$$
    $$f = Mg + \Delta f \quad ; \quad \phi = \Delta\phi$$

    On injecte ça dans nos équations du mouvement en utilisant le développement de Taylor à l'ordre 1 (les approximations des petits angles $\sin(\epsilon) \approx \epsilon$ et $\cos(\epsilon) \approx 1$). Et surtout, on jette sans remords tous les termes d'ordre 2 (les produits de deux $\Delta$).

    **1. Dynamique horizontale ($\Delta x$) :**
    $$M\Delta\ddot{x} = -(Mg + \Delta f)\sin(\Delta\theta + \Delta\phi)$$
    Avec les petits angles, on a $\sin(\Delta\theta + \Delta\phi) \approx \Delta\theta + \Delta\phi$. En développant, on obtient le terme croisé $-\Delta f(\Delta\theta + \Delta\phi)$ qui est d'ordre 2. On le néglige allègrement :
    $$M\Delta\ddot{x} \approx -Mg(\Delta\theta + \Delta\phi)$$
    Ce qui nous donne :
    $$\Delta\ddot{x} = -g(\Delta\theta + \Delta\phi)$$

    **2. Dynamique verticale ($\Delta y$) :**
    $$M\Delta\ddot{y} = (Mg + \Delta f)\cos(\Delta\theta + \Delta\phi) - Mg$$
    Ici, $\cos(\Delta\theta + \Delta\phi) \approx 1$. L'équation devient merveilleusement simple, les $Mg$ s'annulent :
    $$M\Delta\ddot{y} = Mg + \Delta f - Mg$$
    $$\Delta\ddot{y} = \frac{1}{M}\Delta f$$

    **3. Dynamique de rotation ($\Delta \theta$) :**
    $$J\Delta\ddot{\theta} = -\frac{(Mg + \Delta f)\ell}{2}\sin(\Delta\phi)$$
    On passe le sinus en $\Delta\phi$, et on développe. Là encore, on tombe sur un terme d'ordre 2 : $-\frac{\ell}{2}\Delta f \Delta\phi$ qu'on annule :
    $$J\Delta\ddot{\theta} \approx -\frac{Mg\ell}{2}\Delta\phi$$
    Ce qui donne :
    $$\Delta\ddot{\theta} = -\frac{Mg\ell}{2J}\Delta\phi$$

    **Bilan de la linéarisation :**
    Les équations sont complètement découplées !
    * La dynamique verticale ($\Delta y, \Delta v_y$) ne dépend QUE de la variation de poussée $\Delta f$.
    * La dynamique latérale et de rotation ($\Delta x, \Delta v_x, \Delta\theta, \Delta\omega$) ne dépend QUE de l'angle de braquage de la tuyère $\Delta\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On commence par définir notre vecteur d'état $\Delta s$ (qui regroupe les positions et leurs dérivées) et notre vecteur d'entrée $u$ (nos commandes) :
    $$\Delta s = \begin{pmatrix} \Delta x \\ \Delta v_x \\ \Delta y \\ \Delta v_y \\ \Delta\theta \\ \Delta\omega \end{pmatrix} \quad \text{et} \quad u = \begin{pmatrix} \Delta f \\ \Delta\phi \end{pmatrix}$$

    En extrayant les coefficients de nos équations différentielles précédentes, on sépare la dynamique interne (Matrice $A$, $6 \times 6$) de l'impact des commandes (Matrice $B$, $6 \times 2$).

    **La matrice de dynamique $A$ :**
    On traduit simplement le fait que la dérivée d'une position est sa vitesse (les $1$), et on place notre seul terme de couplage interne (l'influence de $\theta$ sur l'accélération horizontale $\ddot{x}$) :
    $$A = \begin{pmatrix} 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & -g & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$

    **La matrice de commande $B$ :**
    Elle map nos deux entrées ($\Delta f$ et $\Delta\phi$) sur les accélérations correspondantes. On retrouve bien le couplage de $\Delta\phi$ sur $\ddot{x}$ et le couple de rappel angulaire sur $\ddot{\theta}$ :
    $$ B = \begin{pmatrix} 0 & 0 \\ 0 & -g \\ 0 & 0 \\ 1/M & 0 \\ 0 & 0 \\ 0 & -Mg \cdot l/(2J) \end{pmatrix}$$

    **Note :**
    Si on remplace avec nos valeurs numériques ($M=1$, $g=1$, $\ell=2$), le moment d'inertie du cylindre vaut $J = \frac{M\ell^2}{12} = \frac{1}{3}$.
    Le coefficient $B_{5,1}$ (accélération angulaire) devient donc $-\frac{1 \cdot 1 \cdot 2}{2 \cdot (1/3)} = -3$. C'est physiquement cohérent.
    """)
    return


@app.cell
def _(J, M, g, l, np):
    # Matrices A et B du système linéarisé complet (6x6, 6x2)
    A_full = np.array([
        [0, 1, 0, 0, 0,  0],
        [0, 0, 0, 0, -g, 0],
        [0, 0, 0, 1, 0,  0],
        [0, 0, 0, 0, 0,  0],
        [0, 0, 0, 0, 0,  1],
        [0, 0, 0, 0, 0,  0],
    ], dtype=float)

    B_full = np.array([
        [0,      0],
        [0,      -g],
        [0,       0],
        [1/M,     0],
        [0,       0],
        [0, -M*g*l/(2*J)],
    ], dtype=float)

    print("A ="); print(A_full)
    print("\nB ="); print(B_full)
    return A_full, B_full


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pour déterminer la stabilité, il faut trouver les valeurs propres de $A$, c'est-à-dire les racines du polynôme caractéristique $\det(A - \lambda I) = 0$.

    On calcule $A - \lambda I$ :

    $$A - \lambda I = \begin{pmatrix} -\lambda & 1 & 0 & 0 & 0 & 0 \\ 0 & -\lambda & 0 & 0 & -1 & 0 \\ 0 & 0 & -\lambda & 1 & 0 & 0 \\ 0 & 0 & 0 & -\lambda & 0 & 0 \\ 0 & 0 & 0 & 0 & -\lambda & 1 \\ 0 & 0 & 0 & 0 & 0 & -\lambda \end{pmatrix}$$

    On remarque tout de suite que cette matrice est **triangulaire supérieure** (tous les termes sous la diagonale sont nuls). Et on sait que le déterminant d'une matrice triangulaire, c'est juste le produit des éléments diagonaux :

    $$\det(A - \lambda I) = (-\lambda) \times (-\lambda) \times (-\lambda) \times (-\lambda) \times (-\lambda) \times (-\lambda) = (-\lambda)^6 = \lambda^6$$

    Donc le polynôme caractéristique est $\lambda^6 = 0$, ce qui donne une **unique racine** $\lambda = 0$ de **multiplicité 6**.

    **Donc :**

    Un système linéaire $\dot{x} = Ax$ est asymptotiquement stable si et seulement si **toutes** les valeurs propres de $A$ ont une partie réelle strictement négative ($\text{Re}(\lambda_i) < 0$ pour tout $i$).

    Ici, $\text{Re}(\lambda_i) = 0$ pour toutes les valeurs propres. Le système **n'est pas asymptotiquement stable**.

    Physiquement, c'est assez intuitif : sans aucun contrôle ($\Delta f = 0$, $\Delta\phi = 0$), le booster est en chute libre. Une petite perturbation de vitesse entraîne un déplacement qui croît linéairement... le système dérive sans jamais revenir.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Imagine qu'on perturbe légèrement le booster autour de son point d'équilibre. Sans contrôleur pour corriger le tir, voici ce que nos équations linéarisées prédisent du comportement "naturel" du système :

    **1. Perturbation de la vitesse horizontale ($\Delta\dot{x}$)** :


    À l'équilibre parfait, on sait que $\Delta\theta = 0$ et $\Delta\phi = 0$. Notre équation de la dynamique latérale $\Delta\ddot{x} = -g(\Delta\theta + \Delta\phi)$ se réduit donc à :
    $$\Delta\ddot{x} = 0 \implies \Delta\dot{x}(t) = \text{constante} = \Delta\dot{x}(0)$$
    Ce qui nous donne, en intégrant pour la position :
    $$\Delta x(t) = \Delta x(0) + \Delta\dot{x}(0) \cdot t$$
    *Bilan physique :* Si le lanceur subit une petite pichenette latérale (un coup de vent par exemple), il va se mettre à dériver horizontalement à vitesse constante, indéfiniment. Il ne reviendra jamais de lui-même à sa position d'origine, car la matrice $A$ ne contient aucune force de rappel sur $x$.

    **2. Perturbation de la vitesse verticale ($\Delta\dot{y}$)** :
    Même punition sur l'axe vertical.

    **3. Perturbation de l'inclinaison ($\Delta\theta$)** :


    C'est la perturbation la plus critique. Si le booster s'incline légèrement ($\Delta\theta \neq 0$), alors la gravité commence à tirer le centre de masse hors de l'axe :
    $$\Delta\ddot{x} = -g\Delta\theta$$
    Le lanceur va donc commencer à accélérer horizontalement dans le sens de son inclinaison. Le système est instable en boucle ouverte. C'est exactement pour ça qu'on va devoir concevoir une loi de commande robuste !
    """)
    return


@app.cell
def _(A_full, la):
    eigenvalues_A = la.eigvals(A_full)
    print("Valeurs propres de A:", eigenvalues_A)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Toutes les valeurs propres sont nulles (ou à partie réelle nulle)

    Le système n'est PAS asymptotiquement stable : il est marginalement stable

    C'est logique, c'est un intégrateur pur sans contrôle, le booster dérive
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On utilise le **critère de Kalman** : le système $(A, B)$ est commandable si et seulement si

    $$\text{rang}\,[B \;,\; AB \;,\; A^2B \;,\; \cdots \;,\; A^{n-1}B] = n$$

    avec $n = 6$ (dimension de l'état).

    Si la matrice de commandabilité est de rang plein, alors on peut amener le système de n'importe quel état initial à n'importe quel état final en temps fini.

    En pratique, on calcule numériquement :
    """)
    return


@app.cell
def _(A_full, B_full, la, np):
    def kalman_matrix(A, B):
        n = A.shape[0]
        cols = [np.linalg.matrix_power(A, k) @ B for k in range(n)]
        return np.hstack(cols)

    C_full = kalman_matrix(A_full, B_full)
    rank_full = la.matrix_rank(C_full)
    print(f"Rang de la matrice de commandabilité: {rank_full}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le rang vaut 6 = $n$ donc le système est commandable. On peut donc concevoir un retour d'état $u = -K\Delta s$ qui place les pôles de la boucle fermée où on veut.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On fixe $f = Mg$ et on ne s'intéresse qu'aux variables latérales $(\Delta x, \Delta v_x, \Delta\theta, \Delta\omega)$ :

    Les équations linéarisées deviennent :
    - $\dot{\Delta x} = \Delta v_x$
    - $\dot{\Delta v_x} = -g\Delta\theta - g\Delta\phi = -\Delta\theta - \Delta\phi$
    - $\dot{\Delta\theta} = \Delta\omega$
    - $\dot{\Delta\omega} = -3\Delta\phi$

    En forme matricielle :
    $$X_{lat} = \begin{bmatrix} \Delta x \\ \Delta\dot{x} \\ \Delta\theta \\ \Delta\dot{\theta} \end{bmatrix}, \qquad U_{lat} = \Delta\phi$$

    En extrayant les lignes/colonnes correspondantes du système complet, les équations linéarisées deviennent :

    $$\Delta\ddot{x} = -g(\Delta\theta + \Delta\phi)$$
    $$\Delta\ddot{\theta} = -\frac{Mg\ell}{2J}\Delta\phi$$

    #### Nouvelles matrices $A$ et $B$

    $$\dot{X}_{lat} = A_{lat} X_{lat} + B_{lat} U_{lat}$$

    $$A_{lat} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & -g & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \qquad B_{lat} = \begin{pmatrix} 0 \\ -g \\ 0 \\ -\dfrac{Mg\ell}{2J} \end{pmatrix}$$
    """)
    return


@app.cell
def _(J, M, g, l, np):
    A_lat = np.array([
        [0, 1, 0, 0],
        [0, 0, -g, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ])

    B_lat = np.array([
        [0],
        [-g],
        [0],
        [-M*g*l/ (2*J)],
    ])

    # Matrice de contrôlabilité :
    C_lat = np.hstack([np.linalg.matrix_power(A_lat, i) @ B_lat for i in range(4)])

    print("Matrice de contrôlabilité :")
    print(C_lat)
    print(f"\nRang : {np.linalg.matrix_rank(C_lat)}")
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Résultat

    $$\boxed{\text{rank}(\mathcal{C}_{lat}) = 4 = n}$$

    **Le système latéral réduit est contrôlable.**

    Avec une seule entrée $\Delta\phi$, on peut tout contrôler car les effets se propagent en cascade :

    $$\Delta\phi \longrightarrow \Delta\ddot{\theta} \longrightarrow \Delta\theta \longrightarrow \Delta\ddot{x} \longrightarrow \Delta x$$

    Incliner le moteur fait pivoter le booster, ce qui crée une force horizontale, ce qui déplace $x$. Un seul actionneur suffit à atteindre les 4 états.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Avec $\Delta\phi = 0$ (pas de contrôle), les équations se simplifient :

    1. $\dot{\Delta\omega} = -3 \times 0 = 0$ → $\Delta\omega(t) = \Delta\omega(0) = 0$ (pas de couple = pas d'accélération angulaire)
    2. $\dot{\Delta\theta} = \Delta\omega = 0$ → $\Delta\theta(t) = \Delta\theta(0) = \pi/4$ (l'angle ne bouge pas)
    3. $\dot{\Delta v_x} = -\Delta\theta = -\pi/4$ → $\Delta v_x(t) = -(\pi/4) \cdot t$ (accélération horizontale constante)
    4. $\dot{\Delta x} = \Delta v_x$ → $\Delta x(t) = -(\pi/4) \cdot t^2/2$ (dérive quadratique)
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, sci):
    def sim_linear_lat(A, B, x0, K_ctrl, t_span, t_eval):
        def rhs(t, x):
            u = -K_ctrl @ x
            return (A @ x + B @ u).flatten()
        r = sci.solve_ivp(rhs, t_span, x0, t_eval=t_eval, rtol=1e-10, atol=1e-10)
        return r.t, r.y

    t_eval = np.linspace(0, 20, 1000)
    x0_ff = [0.0, 0.0, np.pi/4, 0.0]  
    K_zero = np.zeros((1, 4))

    t_ff, y_ff = sim_linear_lat(A_lat, B_lat, x0_ff, K_zero, [0, 20], t_eval)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(t_ff, y_ff[0]); axes[0].set_title(r"$\Delta x(t)$"); axes[0].grid(True)
    axes[0].set_xlabel("t (s)")
    axes[1].plot(t_ff, y_ff[2]); axes[1].set_title(r"$\Delta	heta(t)$"); axes[1].grid(True)
    axes[1].set_xlabel("t (s)")
    plt.tight_layout()
    plt.show()
    return (sim_linear_lat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    C'est assez logique quand on y pense : le booster est penché à 45°, la composante horizontale de la gravité le pousse de côté, mais personne ne corrige l'angle. Du coup l'angle reste figé et la position dérive de plus en plus vite.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On a:
    $K = [0, 0, k_\theta, k_{\dot\theta}]$ donc :

    $$\Delta\phi(t) = -k_\theta \Delta\theta(t) - k_{\dot\theta} \Delta\dot{\theta}(t)$$

    On n'agit que sur $\theta$ et $\dot\theta$ (on ignore $x$ pour l'instant). En substituant dans la dynamique angulaire :

    $$\Delta\ddot\theta = -\frac{Mg\ell}{2J}\Delta\phi = \frac{Mg\ell}{2J}\left(k_\theta \Delta\theta + k_{\dot\theta}\Delta\dot\theta\right)$$

    Posons $\alpha = \frac{Mg\ell}{2J} = 3$ avec nos constantes. L'équation devient :

    $$\Delta\ddot\theta - \alpha k_{\dot\theta}\,\Delta\dot\theta - \alpha k_\theta\,\Delta\theta = 0$$

    C'est un *oscillateur du second ordre*. On identifie avec la forme standard $\ddot q + 2\zeta\omega_n \dot q + \omega_n^2 q = 0$ :

    $$\omega_n^2 = -\alpha k_\theta \implies k_\theta < 0$$
    $$2\zeta\omega_n = -\alpha k_{\dot\theta} \implies k_{\dot\theta} < 0$$

    Pour converger en ~20s, on veut $\omega_n \approx 0.3$ rad/s et $\zeta \approx 1$ (critiquement amorti) :

    $$k_\theta = -\frac{\omega_n^2}{\alpha} = -\frac{0.09}{3} = -0.03$$
    $$k_{\dot\theta} = -\frac{2\zeta\omega_n}{\alpha} = -\frac{0.6}{3} = -0.2$$


    en effet:

    L'équation de $\Delta\theta$ en boucle fermée est :

    $$\Delta\ddot\theta + 2\zeta\omega_n,\Delta\dot\theta + \omega_n^2,\Delta\theta = 0$$

    La solution générale (pour $\zeta = 1$, cas critique) est :

    $$\Delta\theta(t) = (A + Bt)e^{-\omega_n t}$$

    Le terme $e^{-\omega_n t}$ contrôle la vitesse de convergence.

    La constante de temps du système est $\tau = \dfrac{1}{\omega_n}$. On considère que le système a convergé après environ $5\tau$ (règle empirique : à $5\tau$, on est à $e^{-5} \approx 0.7%$ de la valeur initiale) :

    $$t_{\text{convergence}} \approx 5\tau = \frac{5}{\omega_n}$$

    On veut converger en $\sim 20$ s :

    $$\frac{5}{\omega_n} = 20 \implies \omega_n = \frac{5}{20} = 0.25 \approx 0.3 \text{ rad/s}$$

    $\zeta = 1$ implique un retour le plus rapide sans dépasser 0
    """)
    return


@app.cell
def _(A_lat, J, M, g, l, np, plt, sci):
    def simulate_manually_tunned():

        alpha = M * g * l / (2 * J)    # = 3.0
        B = np.array([0, -g, 0, -alpha])   # vecteur colonne (4,)

        X0     = np.array([0.0, 0.0, np.pi/4, 0.0])
        t_span = [0, 40]
        t_eval = np.linspace(0, 40, 2000)

        # Gains à tester (k_theta, k_dtheta, label, couleur)
        # Choix guidé par la forme standard : ωₙ² = α|k_θ|, 2ζωₙ = α|k_θ̇|
        # Cible : ωₙ ≈ 0.3 rad/s, ζ ≈ 1 (amorti critique) → convergence ~20s
        # Voir l'analyse ci*dessous
        gains = [
            (-0.03, -0.20, "iter 1 — ωₙ=0.30, ζ=1.0",     "royalblue"),
            (-0.05, -0.30, "iter 2 — ωₙ=0.39, ζ=1.0",     "darkorange"),
            (-0.08, -0.35, "iter 3 — ωₙ=0.49, ζ=0.71",    "seagreen"),
            (-0.05, -0.25, "iter 4 — ωₙ=0.39, ζ=0.96",    "crimson"),
            (-0.03, -0.1, "iter 4 — ωₙ=0.3, ζ=0.5",    "yellow"),
        ]

        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        for k_th, k_dth, label, color in gains:
            K = np.array([0, 0, k_th, k_dth])
        
            def closed_loop(t, X, K=K):
                delta_phi = -K @ X
                return A_lat @ X + B * delta_phi

            sol = sci.solve_ivp(closed_loop, t_span, X0,
                            dense_output=True, rtol=1e-10, atol=1e-10)
            X_t   = sol.sol(t_eval)
            x_t   = X_t[0]
            th_t  = X_t[2]
            dth_t = X_t[3]
            phi_t = -(K[2] * th_t + K[3] * dth_t)
            axes[0].plot(t_eval, np.degrees(th_t),  label=label, color=color)
            axes[1].plot(t_eval, np.degrees(phi_t), label=label, color=color)
            axes[2].plot(t_eval, x_t,               label=label, color=color)

        for ax in axes[:2]:
            ax.axhline( 90, color="grey", ls=":", lw=1)
            ax.axhline(-90, color="grey", ls=":", lw=1, label="±90° (limite)")
        titles  = [r"$\Delta\theta(t)$ (degrés)",
                   r"$\Delta\phi(t)$  (degrés)",
                   r"$\Delta x(t)$    (m)"]
        ylabels = ["degrés", "degrés", "m"]

        for ax, title, ylabel in zip(axes, titles, ylabels):
            ax.axhline(0, color="black", ls="--", lw=0.8)
            ax.set_title(title)
            ax.set_xlabel("temps (s)")
            ax.set_ylabel(ylabel)
            ax.legend(fontsize=7)
            ax.grid(True)

        plt.suptitle("Contrôleur manuel — itérations sur les gains", fontsize=12)
        plt.tight_layout()
        return plt.show()

    simulate_manually_tunned()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On utilise `place_poles` pour placer les 4 pôles de $A_{lat} - B_{lat}K_{pp}$. Contrairement au contrôleur manuel, cette fois on veut aussi $\Delta x \to 0$, donc les 4 pôles doivent être dans le demi-plan gauche.

    Pour le placement de pôles, on a le choix entre des pôles réels ou complexes conjugués. Les deux sont valides, mais le comportement est différent :
    - **Pôles réels** ($\lambda = -\sigma$) : la réponse est une décroissance exponentielle pure $e^{-\sigma t}$, sans oscillation. C'est "doux" mais parfois lent.
    - **Pôles complexes** ($\lambda = -\sigma \pm j\omega_d$) : la réponse est une exponentielle amortie multipliée par une sinusoïde : $e^{-\sigma t}\cos(\omega_d t + \varphi)$. Le système oscille un peu autour de l'équilibre avant de se stabiliser.
    La partie réelle $-\sigma$ contrôle la **vitesse de convergence** (constante de temps $\tau = 1/\sigma$), et la partie imaginaire $\omega_d$ contrôle la **fréquence d'oscillation**.
    L'avantage des pôles complexes, c'est qu'on peut avoir une convergence plus rapide pour un effort de commande comparable.


    **Contrainte importante :** les pôles complexes doivent toujours venir par **paires conjuguées** ($\lambda$ et $\bar{\lambda}$), sinon le gain $K$ ne serait pas réel et on aurait une commande $\phi$ complexe, ce qui n'a pas de sens physique.
    On essaie ici :
    $$\lambda_{1,2} = -0.5 \pm 0.1j, \qquad \lambda_{3,4} = -0.3 \pm 0.1j$$
    d'abord, puis on ajuste.
    """)
    return


@app.cell
def _(A_lat, B_lat, la, np, plt, sim_linear_lat):
    from scipy.signal import place_poles

    desired_poles = np.array([-0.5+0.1j, -0.5-0.1j, -0.3+0.1j, -0.3-0.1j])
    _result_pp = place_poles(A_lat, B_lat, desired_poles)
    K_pp = _result_pp.gain_matrix
    print("K_pp =", K_pp)
    print("Pôles obtenus:", la.eigvals(A_lat - B_lat @ K_pp))
    X0     = np.array([0.0, 0.0, np.pi/4, 0.0])
    _t_eval = np.linspace(0, 60, 3000)
    _t_pp, _y_pp = sim_linear_lat(A_lat, B_lat, X0, K_pp, [0, 60], _t_eval)
    _phi_pp = -(K_pp @ _y_pp).flatten()

    _fig, _axes = plt.subplots(1, 3, figsize=(15, 4))
    _axes[0].plot(_t_pp, _y_pp[2]); _axes[0].set_title(r"$\Delta\theta(t)$"); _axes[0].grid(True)
    _axes[0].axhline(0, color='k', ls='--', lw=0.5)
    _axes[1].plot(_t_pp, _y_pp[0]); _axes[1].set_title(r"$\Delta x(t)$"); _axes[1].grid(True)
    _axes[1].axhline(0, color='k', ls='--', lw=0.5)
    _axes[2].plot(_t_pp, _phi_pp); _axes[2].set_title(r"$\Delta\phi(t)$"); _axes[2].grid(True)
    _axes[2].axhline(np.pi/2, color='r', ls='--')
    _axes[2].axhline(-np.pi/2, color='r', ls='--')
    plt.suptitle("Pole Placement Controller")
    plt.tight_layout(); plt.show()

    print(f"|theta| < pi/2 ? {np.all(np.abs(_y_pp[2]) < np.pi/2)}")
    print(f"|phi| < pi/2 ? {np.all(np.abs(_phi_pp) < np.pi/2)}")
    print(f"Asymptotiquement stable ? {np.all(np.real(la.eigvals(A_lat - B_lat @ K_pp)) < 0)}")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Au lieu de choisir les pôles à la main, on formule un problème d'optimisation. On minimise le coût :
    $$J = \int_0^\infty \left(\Delta s^T Q \Delta s + \Delta\phi^T R \Delta\phi\right) dt$$

    L'idée c'est :
    - **$Q$ grand** → on pénalise les écarts d'état, le système converge vite
    - **$R$ grand** → on pénalise l'effort de commande, $\phi$ reste petit
    - C'est un compromis entre performance et effort

    On résout l'**équation algébrique de Riccati** :
    $$A^T P + PA - PBR^{-1}B^TP + Q = 0$$

    Et le gain optimal est $K_{oc} = R^{-1}B^TP$..

    On commence avec $Q = \text{diag}(1, 1, 10, 1)$ et $R = 100$, puis on ajuste.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


if __name__ == "__main__":
    app.run()
