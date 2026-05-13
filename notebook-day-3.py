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


@app.cell
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


@app.cell
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our state is $s = (x, v_x, y, v_y,\theta, \omega)$ and the system is governed by
    $\dot{s} = F(s, f, \phi)$ with
    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    The equilibria are characterized by $F(s, f, \phi) = 0$. We obtain directly that
    $v_x = v_y = 0$ and $\omega = 0$. We also extract the two equations

    $$
    \begin{bmatrix}
    -(f / M) \sin (\theta + \phi) \\
    +(f / M) \cos(\theta +\phi)
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    $$
    which holds if when $|\theta| < \pi/2$ and $|\phi| < \pi/2$ and only if
    $\theta = \phi = 0$ and $f = M g$. The final equation is then satisfied if and only if
    $\omega = 0$. Finally, we obtain the equilibria as:
    $$
    \begin{bmatrix}
    x \\
    v_x \\
    y \\
    v_y \\
    \theta \\
    \omega \\
    f \\
    \phi
    \end{bmatrix}
    =
    \begin{bmatrix}
    ? \\
    0 \\
    ? \\
    0 \\
    0 \\
    0 \\
    M g \\
    0
    \end{bmatrix}
    $$
    where $?$ stands for "any possible value".
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $\Delta \theta = \theta$, $\Delta \phi = \phi$ and $\Delta f = f - M g$. Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and that for small values of $\alpha$, $\sin \alpha \approx \alpha$ and $\cos \alpha \approx 1$, we obtain:

    \begin{align*}
    M (d/dt)^2 \Delta x &= - Mg (\Delta \theta + \Delta \phi)  \\
    M (d/dt)^2 \Delta y &= \Delta f \\
    J (d/dt)^2 \Delta \theta &= - (Mg \ell /2) \Delta \phi \\
    \end{align*}
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
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note: remember that $J = (1/12) M \ell^2$.

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 1 \\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix}
    \;\;\;
    B =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & -M g \ell/(2J)\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & - 6 g / \ell\\
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(g, np):
    A = np.zeros((6, 6))
    A[0, 1] = 1.0
    A[1, 4] = -g
    A[2, 3] = 1.0
    A[4, -1] = 1.0
    A
    return (A,)


@app.cell(hide_code=True)
def _(M, g, l, np):
    B = np.zeros((6, 2))
    B[ 1, 1]  = -g 
    B[ 3, 0]  = 1/M
    B[-1, 1] = -6 * g / l
    B
    return (B,)


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
    ### 🔓 Solution

    No, since $0$ is the only eigenvalue of $A$ and $0$ doesn't have a negative real part.
    """)
    return


@app.cell(hide_code=True)
def _(A, la):
    eigenvalues, eigenvectors = la.eig(A)
    print(f"Eigenvalues of A: {eigenvalues}")
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
    ### 🔓 Solution

    The controllability matrix of the system is:
    """)
    return


@app.cell(hide_code=True)
def _(A, B, np):
    # Controllability
    cs = np.column_stack
    mp = np.linalg.matrix_power
    KC = cs([mp(A, k) @ B for k in range(6)])
    KC
    return (KC,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and its rank is
    """)
    return


@app.cell(hide_code=True)
def _(KC, np):
    int(np.linalg.matrix_rank(KC))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    which is equal to the state dimension, so the answer is yes, it's controllable.
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
    ### 🔓 Solution
    """)
    return


@app.cell
def _(g, l, np):
    A_lat = np.array([
        [0, 1, 0, 0], 
        [0, 0, -g, 0], 
        [0, 0, 0, 1], 
        [0, 0, 0, 0]], dtype=np.float64)
    B_lat = np.array([[0, -g, 0, - 6 * g / l]]).T

    print("A_lat:")
    print(A_lat)
    print("B_lat:")
    print(B_lat)
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(A_lat, B_lat, np):
    # Controllability
    _cs = np.column_stack
    _mp = np.linalg.matrix_power
    KC_lat = _cs([_mp(A_lat, k) @ B_lat for k in range(6)])
    KC_lat
    return (KC_lat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This reduced system of dimension 4 is controllable since the rank of its controllability matrix is 4:
    """)
    return


@app.cell(hide_code=True)
def _(KC_lat, np):
    np.linalg.matrix_rank(KC_lat)
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
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(g, l, np):
    def make_fun_lat(phi):
        def fun_lat(t, state):
            x, dx, theta, dtheta = state
            phi_ = phi(t, state)
            d2x = -g * (theta + phi_)
            d2theta = - 6 * g / l * phi_
            return np.array([dx, d2x, dtheta, d2theta])

        return fun_lat

    return (make_fun_lat,)


@app.cell(hide_code=True)
def _(make_fun_lat, mo, np, plt, sci):
    def lin_sim_1():
        def phi(t, state):
            return 0.0

        f_lat = make_fun_lat(phi)
        t_span = [0, 10]
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]
        r = sci.solve_ivp(
            fun=f_lat, y0=state_0, t_span=t_span, dense_output=True
        )
        t = np.linspace(t_span[0], t_span[1], 1000)
        sol_t = r.sol(t)
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(t, sol_t[0], label=r"$x(t)$")
        ax1.grid(True)
        ax1.legend()
        ax2.plot(t, sol_t[2], label=r"$\theta(t)$")
        ax2.grid(True)
        ax2.set_xlabel(r"time $t$")
        ax2.legend()
        return mo.center(fig)


    lin_sim_1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Since the reactor pushes (with a constant force) in the axis of the booster ($\phi=0$) and the initial title velocity $\omega = \dot{\theta}$ is zero, it's sensible that the title $\theta$ stays constant. That explains the second graph.
    - On the other hand, the constant projected force on the $x$-axis drives a constant acceleration which is towards the left since the initial tilt is positive. That explain the first graph.
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We try first a controller that corrects using only $\Delta \theta$ since it it's the simples think we can think of (a controller based only on the derivative would not achieve $\Delta \theta(t) \to 0$ since it would only knows $\Delta \theta(t)$ up to a constant). When $\Delta \theta > 0$, we want the reactor to be oriented on the right ($\Delta \phi > 0$) to compensate for this trend.

    Hence it makes sens to start for something simple such as
    $\Delta \phi =  \Delta \theta$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & 0
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    and

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    Let's make a simulation out of this!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k1():

        K = np.array([0.0, 0.0, -1.0, 0.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Unfortunately that doesn't work, we have introduced an oscillatory dynamics.

    To correct that, we may introduce some additionial "friction" that prevents our compensation to kick in too fast and end up the control
    $\Delta \phi = \Delta \theta + \beta (d \Delta \theta /dt)$, for some $\beta > 0$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & -\beta
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    Experimentally (see below), anything between $\beta = 0.1$ and $\beta = 5.0$ seems to satisfy the specification. The closed-loop dynamics is slower need $0.1$ and faster near $5.0$.

    In any case, there is a permament drift which is induced on $\Delta x$, which does not converge to $0$. This is corroborated by a double eigenvalue at $0$, which proves that our closed-loop dynamics is **not** asymptotically stable.
    """)
    return


@app.cell(hide_code=True)
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k2():

        K = np.array([0.0, 0.0, -1.0, -0.1])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k2()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k3():

        K = np.array([0.0, 0.0, -1.0, -5.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k3()
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We decide to try to cluster all our eigenvalue near a single real (negative) value
    $s$. If we want a convergence at 5% in 20 seconds at most, we know that $|\lambda|$
    should be at least $3 / 20 = 0.15$.

    Experimentally however this is a bit slow to converge (see below), the setup is better if we pick a faster dynamics, to have our eigenvalues clustered around $-0.5$ for example.

    There is actually quite a range of locations that work, but around $-0.1$, we start compensating too fast and to violate the constraint on the maximal value of $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_3():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-0.15 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_3()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Kpp = scipy.signal.place_poles(
        A=A_lat,
        B=B_lat,
        poles=-0.5 * np.array([1.0, 1.01, 1.02, 1.03]),
    ).gain_matrix.squeeze()


    def lin_sim_32():
        K = Kpp
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_32()
    return (Kpp,)


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_33():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-1.0 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_33()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
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
    The basic optimal control design, with

    $$
    Q = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix},
    $$

    and

    $$
    R = \begin{bmatrix}
    1
    \end{bmatrix},
    $$
    almost makes the job, except that it is a bit too fast and that results initially in large values of the angle $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_4():
        Q = np.eye(4,4)
        print("Q:", Q)
        R = np.eye(1) #10*l**2 * np.eye(1)
        print("R:", R)
        Pi = scipy.linalg.solve_continuous_are(
            a=A_lat, 
            b=B_lat, 
            q=Q, 
            r=R
        )
        Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_4()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A second design with the same $Q$ but $R$ increased by $100$ (to reduce the activation of the input at the price of some convergence speed) performs adequately!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Q = np.eye(4,4)
    print("Q:", Q)
    _R = 100 * np.eye(1)
    print("R:", _R)
    Pi = scipy.linalg.solve_continuous_are(
        a=A_lat, 
        b=B_lat, 
        q=Q, 
        r=_R
    )
    Koc = (np.linalg.inv(_R) @ B_lat.T @ Pi).squeeze()

    def lin_sim_42():
        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_42()
    return (Koc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(Kpp, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Kpp.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(Koc, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Koc.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exact Linearization

    Let
    $$
    R(\alpha) =
    \begin{bmatrix} +\cos \alpha & -\sin \alpha \\ +\sin \alpha & -\cos \alpha
    \end{bmatrix}
    $$

    Consider an auxiliary system which is meant to compute the force $(f_x, f_y)$ applied to the booster.

    The inputs of the auxiliary system are

    $$
    v = (v_1, v_2) \in \mathbb{R}^2,
    $$

    its dynamics

    $$
    \ddot{z} = v_1 \qquad \text{ where } \qquad z \in \mathbb{R}
    $$

    and its output $(f_x, f_y) \in \mathbb{R}^2$ is given by

    \[
    \begin{bmatrix}
    f_x \\
    f_y
    \end{bmatrix} = R\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix}
    z - M\ell\dot{\theta}^2 / 6 \\
    {M\ell v_2}/{6z}
    \end{bmatrix}
    \]

    ⚠️ Note that the second component $f_y$ of the reactor force is undefined whenever $z=0$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Geometrical Interpretation


    Consider the output $h$ of the original system

    $$
    h :=
    \begin{bmatrix}
    x - (\ell/6) \sin \theta \\
    y + (\ell/6) \cos \theta
    \end{bmatrix} \in \mathbb{R}^2
    $$

    Provide a geometrical interpretation of $h$ (for example, make a drawing).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notre **centre de gravité** (CoM) se trouve aux coordonnées $(x,y)$.

    Si l'on définit $\theta$ comme l'angle mesuré dans le sens anti-horaire par rapport à la verticale, le vecteur unitaire pointant vers le **haut de la fusée** (le côté opposé à la tuyère) est $(-\sin\theta, \cos\theta)$.

    Si l'on remonte le long de cet axe sur une distance de $\ell/6$ (où $\ell$ est la longueur totale du système) depuis le centre de gravité, on obtient l'équation suivante :

    $$h = \begin{pmatrix}x\\y\end{pmatrix} + \frac{\ell}{6}\begin{pmatrix}-\sin\theta\\\cos\theta\end{pmatrix} = \begin{pmatrix}x - (\ell/6)\sin\theta\\ y + (\ell/6)\cos\theta\end{pmatrix}$$

    ## Interprétation Visuelle

    Le point $h$ correspond au point situé exactement à **un tiers (1/3) du sommet du booster** (soit une distance de $\ell/6$ au-dessus du centre de gravité en direction du sommet).
    """)
    return


@app.cell
def _(mo):
    mo.image(src="Inter.jpeg")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 First and Second-Order Derivatives

    Compute $\dot{h}$ as a function of $\dot{x}$, $\dot{y}$, $\theta$ and $\dot{\theta}$ (and constants) and then $\ddot{h}$ as a function of $\theta$ and $z$ (and constants) when the auxiliary system is plugged in the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Par la règle de dérivation en chaîne :

    $$\dot{h}_x = \dot{x} - \frac{\ell}{6}\cos\theta\cdot\dot\theta = v_x - \frac{\ell}{6}\omega\cos\theta$$

    $$\dot{h}_y = \dot{y} - \frac{\ell}{6}(-\sin\theta)\cdot\dot\theta = v_y - \frac{\ell}{6}\omega\sin\theta$$

    En notation matricielle :

    $$\dot{h} = \begin{bmatrix} v_x \\ v_y \end{bmatrix} - \frac{\ell}{6}\omega \begin{bmatrix} \cos\theta \\ \sin\theta \end{bmatrix}$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On dérive $\dot{h}$ :

    $$\ddot{h}_x = \ddot{x} - \frac{\ell}{6}\frac{d}{dt}\!\left(\cos\theta\,\dot\theta\right)$$

    En effet $\dfrac{d}{dt}(\cos\theta\,\dot\theta) = -\sin\theta\,\dot\theta^2 + \cos\theta\,\ddot\theta$, donc :

    $$\ddot{h}_x = \ddot{x} + \frac{\ell}{6}\sin\theta\,\dot\theta^2 - \frac{\ell}{6}\cos\theta\,\ddot\theta$$

    $$\ddot{h}_y = \ddot{y} - \frac{\ell}{6}\frac{d}{dt}\!\left(\sin\theta\,\dot\theta\right)$$

    Or $\dfrac{d}{dt}(\sin\theta\,\dot\theta) = \cos\theta\,\dot\theta^2 + \sin\theta\,\ddot\theta$, donc :
    $$\ddot{h}_y = \ddot{y} - \frac{\ell}{6}\cos\theta\,\dot\theta^2 - \frac{\ell}{6}\sin\theta\,\ddot\theta$$

    La dynamique de translation donne $M\ddot{x} = f_x$, $M\ddot{y} = f_y - Mg$, et le système auxiliaire fournit :

    $$\begin{pmatrix}f_x\\f_y\end{pmatrix} = R\!\left(\theta-\frac{\pi}{2}\right)\begin{pmatrix}z - \dfrac{M\ell\dot\theta^2}{6}\\[4pt]\dfrac{M\ell v_2}{6z}\end{pmatrix}$$

    En développant $R(\theta - \pi/2) = \begin{pmatrix}\sin\theta & \cos\theta \\ -\cos\theta & \sin\theta\end{pmatrix}$, on obtient :

    $$f_x = \sin\theta\!\left(z - \frac{M\ell\dot\theta^2}{6}\right) + \cos\theta\!\left(\frac{M\ell v_2}{6z}\right)$$

    $$f_y = -\cos\theta\!\left(z - \frac{M\ell\dot\theta^2}{6}\right) + \sin\theta\!\left(\frac{M\ell v_2}{6z}\right)$$

    D'où les accélérations de translation :
    $$\ddot{x} = \frac{z}{M}\sin\theta - \frac{\ell}{6}\dot\theta^2\sin\theta + \frac{\ell v_2}{6z}\cos\theta$$

    $$\ddot{y} = -\frac{z}{M}\cos\theta + \frac{\ell}{6}\dot\theta^2\cos\theta + \frac{\ell v_2}{6z}\sin\theta - g$$

    Le couple vaut $J\ddot\theta = (\ell/2)\cdot f\sin\phi$

    on : $f\sin\phi = \tfrac{M\ell\,v_2}{6z}$

    En substituant : $\tfrac{M\ell^2}{12}\,\ddot\theta = \tfrac{M\ell^2}{12}\cdot\tfrac{v_2}{z}$, et comme $J = M\ell^2/12$, tout se simplifie :

    $$\ddot\theta = \frac{v_2}{z}$$

    On remplace $\ddot{x}$ et $\ddot\theta$ dans $\ddot{h}_x$ :

    $$\ddot{h}_x = \left(\frac{z}{M}\sin\theta - \frac{\ell}{6}\dot\theta^2\sin\theta + \frac{\ell v_2}{6z}\cos\theta\right) + \frac{\ell}{6}\sin\theta\,\dot\theta^2 - \frac{\ell}{6}\cos\theta\cdot\frac{v_2}{z}$$

    Il reste :
    $$\boxed{\ddot{h}_x = \frac{z}{M}\sin\theta}$$

    On remplace $\ddot{y}$ et $\ddot\theta$ dans $\ddot{h}_y$ :

    $$\ddot{h}_y = \left(-\frac{z}{M}\cos\theta + \frac{\ell}{6}\dot\theta^2\cos\theta + \frac{\ell v_2}{6z}\sin\theta - g\right) - \frac{\ell}{6}\cos\theta\,\dot\theta^2 - \frac{\ell}{6}\sin\theta\cdot\frac{v_2}{z}$$

    Il reste :
    $$\boxed{\ddot{h}_y = -\frac{z}{M}\cos\theta - g}$$

    $$\boxed{\ddot{h} = \frac{z}{M}\begin{pmatrix}\sin\theta \\ -\cos\theta\end{pmatrix} - \begin{pmatrix}0 \\ g\end{pmatrix}}$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Third and Fourth-Order Derivatives

    Compute the third derivative $h^{(3)}$ of $h$ as a function of $\theta$ and $z$ (and constants) and then the fourth derivative $h^{(4)}$ of $h$ with respect to time as a function of $\theta$, $\dot{\theta}$, $z$, $\dot{z}$, $v$ (and constants) when the auxiliary system is on.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La troisième dérivée

    On repart du résultat établi :
    $$\ddot{h} = \frac{z}{M}\begin{pmatrix}\sin\theta \\ -\cos\theta\end{pmatrix} - \begin{pmatrix}0 \\ g\end{pmatrix}$$

    On dérive composante par composante. La constante $g$ disparaît, et on applique la règle du produit à $\frac{z}{M}\sin\theta$ et $\frac{z}{M}(-\cos\theta)$.

    **Composante $h^{(3)}_x$ :** on dérive $\frac{z}{M}\sin\theta$,

    $$h^{(3)}_x = \frac{\dot{z}}{M}\sin\theta + \frac{z}{M}\cos\theta\,\dot\theta$$

    **Composante $h^{(3)}_y$ :** on dérive $-\frac{z}{M}\cos\theta$,

    $$h^{(3)}_y = -\frac{\dot{z}}{M}\cos\theta + \frac{z}{M}\sin\theta\,\dot\theta$$

    Donc :

    $$\boxed{h^{(3)} = \frac{\dot{z}}{M}\begin{pmatrix}\sin\theta \\ -\cos\theta\end{pmatrix} + \frac{z\dot\theta}{M}\begin{pmatrix}\cos\theta \\ \sin\theta\end{pmatrix}}$$

    La quatrième dérivée

    On dérive $h^{(3)}$ composante par composante. On a quatre termes à différentier via la règle du produit.

    **Composante $h^{(4)}_x$ :** on dérive $\frac{\dot{z}}{M}\sin\theta + \frac{z\dot\theta}{M}\cos\theta$,

    $$h^{(4)}_x = \frac{\ddot{z}}{M}\sin\theta + \frac{\dot{z}}{M}\cos\theta\,\dot\theta + \frac{d}{dt}\!\left(\frac{z\dot\theta}{M}\cos\theta\right)$$

    Or $\dfrac{d}{dt}(z\dot\theta\cos\theta) = \dot{z}\dot\theta\cos\theta + z\ddot\theta\cos\theta - z\dot\theta\sin\theta\,\dot\theta$, donc :

    $$h^{(4)}_x = \frac{\ddot{z}}{M}\sin\theta + \frac{\dot{z}\dot\theta}{M}\cos\theta + \frac{\dot{z}\dot\theta}{M}\cos\theta + \frac{z\ddot\theta}{M}\cos\theta - \frac{z\dot\theta^2}{M}\sin\theta$$

    $$h^{(4)}_x = \frac{\ddot{z}}{M}\sin\theta + \frac{2\dot{z}\dot\theta}{M}\cos\theta + \frac{z\ddot\theta}{M}\cos\theta - \frac{z\dot\theta^2}{M}\sin\theta$$

    **Composante $h^{(4)}_y$ :** on dérive $-\frac{\dot{z}}{M}\cos\theta + \frac{z\dot\theta}{M}\sin\theta$,

    $$h^{(4)}_y = -\frac{\ddot{z}}{M}\cos\theta + \frac{\dot{z}}{M}\sin\theta\,\dot\theta + \frac{d}{dt}\!\left(\frac{z\dot\theta}{M}\sin\theta\right)$$

    Or $\dfrac{d}{dt}(z\dot\theta\sin\theta) = \dot{z}\dot\theta\sin\theta + z\ddot\theta\sin\theta + z\dot\theta\cos\theta\,\dot\theta$, donc :

    $$h^{(4)}_y = -\frac{\ddot{z}}{M}\cos\theta + \frac{\dot{z}\dot\theta}{M}\sin\theta + \frac{\dot{z}\dot\theta}{M}\sin\theta + \frac{z\ddot\theta}{M}\sin\theta + \frac{z\dot\theta^2}{M}\cos\theta$$

    $$h^{(4)}_y = -\frac{\ddot{z}}{M}\cos\theta + \frac{2\dot{z}\dot\theta}{M}\sin\theta + \frac{z\ddot\theta}{M}\sin\theta + \frac{z\dot\theta^2}{M}\cos\theta$$


    Le système auxiliaire donne $\ddot{z} = v_1$ et $\ddot\theta = v_2/z$. On substitue :

    **Dans $h^{(4)}_x$ :**

    $$h^{(4)}_x = \frac{v_1}{M}\sin\theta + \frac{2\dot{z}\dot\theta}{M}\cos\theta + \frac{z}{M}\cdot\frac{v_2}{z}\cos\theta - \frac{z\dot\theta^2}{M}\sin\theta$$

    Le troisième terme se simplifie $\frac{z}{M}\cdot\frac{v_2}{z} = \frac{v_2}{M}$, donc :

    $$h^{(4)}_x = \frac{v_1}{M}\sin\theta + \frac{2\dot{z}\dot\theta}{M}\cos\theta + \frac{v_2}{M}\cos\theta - \frac{z\dot\theta^2}{M}\sin\theta$$

    **Dans $h^{(4)}_y$ :**

    $$h^{(4)}_y = -\frac{v_1}{M}\cos\theta + \frac{2\dot{z}\dot\theta}{M}\sin\theta + \frac{z}{M}\cdot\frac{v_2}{z}\sin\theta + \frac{z\dot\theta^2}{M}\cos\theta$$

    De même $\frac{z}{M}\cdot\frac{v_2}{z} = \frac{v_2}{M}$, donc :

    $$h^{(4)}_y = -\frac{v_1}{M}\cos\theta + \frac{2\dot{z}\dot\theta}{M}\sin\theta + \frac{v_2}{M}\sin\theta + \frac{z\dot\theta^2}{M}\cos\theta$$


    On regroupe par vecteurs directeurs :

    $$\boxed{h^{(4)} = \frac{v_1}{M}\begin{pmatrix}\sin\theta\\-\cos\theta\end{pmatrix} + \frac{v_2 + 2\dot{z}\dot\theta}{M}\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix} + \frac{z\dot\theta^2}{M}\begin{pmatrix}-\sin\theta\\\cos\theta\end{pmatrix}}$$

    Les trois vecteurs directeurs qui apparaissent ont une belle interprétation géométrique :

    - $(\sin\theta,\,-\cos\theta)^T$ : direction **axiale** du booster (de la base vers le nez)
    - $(\cos\theta,\,\sin\theta)^T$ : direction **latérale** (perpendiculaire au corps)
    - $(-\sin\theta,\,\cos\theta)^T$ : direction axiale **opposée**, liée à l'effet centripète $z\dot\theta^2$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Exact Linearization

    Show that with yet another auxiliary system with input $u=(u_1, u_2)$ and output $v$ fed into the previous one, we can achieve the dynamics

    $$
    h^{(4)} = u
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On cherche un système auxiliaire supplémentaire avec entrée $u = (u_1, u_2)$ et sortie $v = (v_1, v_2)$, tel qu'une fois branché, on obtienne $h^{(4)} = u$.

    On repart du résultat établi :

    $$h^{(4)} = \frac{v_1}{M}\begin{pmatrix}\sin\theta\\-\cos\theta\end{pmatrix} + \frac{v_2 + 2\dot{z}\dot\theta}{M}\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix} + \frac{z\dot\theta^2}{M}\begin{pmatrix}-\sin\theta\\\cos\theta\end{pmatrix}$$

    **Mise sous forme matricielle**

    On réécrit $h^{(4)}$ comme un produit matrice-vecteur. En regroupant les termes en $v_1$ et $v_2$ d'un côté, et les termes connus de l'autre :

    $$h^{(4)} = \frac{1}{M}\underbrace{\begin{pmatrix}\sin\theta & \cos\theta \\ -\cos\theta & \sin\theta\end{pmatrix}}_{=:\,P(\theta)}\begin{pmatrix}v_1 \\ v_2\end{pmatrix} + \frac{1}{M}\begin{pmatrix}-z\dot\theta^2\sin\theta + 2\dot{z}\dot\theta\cos\theta \\ z\dot\theta^2\cos\theta + 2\dot{z}\dot\theta\sin\theta\end{pmatrix}$$

    que l'on écrit de façon compacte :

    $$h^{(4)} = \frac{1}{M}P(\theta)\,v + \frac{1}{M}\begin{pmatrix}-z\dot\theta^2\sin\theta + 2\dot{z}\dot\theta\cos\theta \\ z\dot\theta^2\cos\theta + 2\dot{z}\dot\theta\sin\theta\end{pmatrix}$$

    **Inversibilité de $P(\theta)$**

    On calcule le déterminant de $P(\theta)$ :

    $$\det P(\theta) = \sin\theta\cdot\sin\theta - \cos\theta\cdot(-\cos\theta) = \sin^2\theta + \cos^2\theta = 1$$

    La matrice $P(\theta)$ est donc **inversible pour tout $\theta$**, et son inverse est :

    $$P(\theta)^{-1} = \begin{pmatrix}\sin\theta & -\cos\theta \\ \cos\theta & \sin\theta\end{pmatrix}$$

    On vérifie : $P(\theta)^{-1}P(\theta) = \begin{pmatrix}\sin^2\theta+\cos^2\theta & 0 \\ 0 & \sin^2\theta+\cos^2\theta\end{pmatrix} = I$. ✓

    **Définition du système auxiliaire supplémentaire**

    On veut $h^{(4)} = u$. Il suffit donc de choisir $v$ tel que :

    $$\frac{1}{M}P(\theta)\,v + \frac{1}{M}\begin{pmatrix}-z\dot\theta^2\sin\theta + 2\dot{z}\dot\theta\cos\theta \\ z\dot\theta^2\cos\theta + 2\dot{z}\dot\theta\sin\theta\end{pmatrix} = u$$

    On résout en $v$ en appliquant $M\,P(\theta)^{-1}$ des deux côtés :

    $$\boxed{v = M\,P(\theta)^{-1}\left[u - \frac{1}{M}\begin{pmatrix}-z\dot\theta^2\sin\theta + 2\dot{z}\dot\theta\cos\theta \\ z\dot\theta^2\cos\theta + 2\dot{z}\dot\theta\sin\theta\end{pmatrix}\right]}$$

    En développant explicitement avec $P(\theta)^{-1} = \begin{pmatrix}\sin\theta & -\cos\theta \\ \cos\theta & \sin\theta\end{pmatrix}$ :

    $$v_1 = M(u_1\sin\theta - u_2\cos\theta) - (-z\dot\theta^2\sin\theta + 2\dot{z}\dot\theta\cos\theta)\sin\theta + (z\dot\theta^2\cos\theta + 2\dot{z}\dot\theta\sin\theta)\cos\theta$$

    $$v_2 = M(u_1\cos\theta + u_2\sin\theta) - (-z\dot\theta^2\sin\theta + 2\dot{z}\dot\theta\cos\theta)\cos\theta - (z\dot\theta^2\cos\theta + 2\dot{z}\dot\theta\sin\theta)\sin\theta$$

    En simplifiant les termes en $z\dot\theta^2$ et $\dot{z}\dot\theta$ (en utilisant $\sin^2\theta+\cos^2\theta=1$) :

    $$\boxed{v_1 = M(u_1\sin\theta - u_2\cos\theta) + z\dot\theta^2}$$

    $$\boxed{v_2 = M(u_1\cos\theta + u_2\sin\theta) - 2\dot{z}\dot\theta}$$

    **Vérification**

    On substitue $v_1$ et $v_2$ dans l'expression de $h^{(4)}$ :

    $$h^{(4)} = \frac{1}{M}P(\theta)\begin{pmatrix}M(u_1\sin\theta - u_2\cos\theta)+z\dot\theta^2 \\ M(u_1\cos\theta+u_2\sin\theta)-2\dot{z}\dot\theta\end{pmatrix} + \frac{1}{M}\begin{pmatrix}-z\dot\theta^2\sin\theta+2\dot{z}\dot\theta\cos\theta\\z\dot\theta^2\cos\theta+2\dot{z}\dot\theta\sin\theta\end{pmatrix}$$

    Le terme $M\,P(\theta)\,u'$ (avec $u' = P(\theta)^{-1}u$) redonne $Mu/M = u$, et tous les termes nonlinéaires se compensent exactement. On obtient bien :

    $$\boxed{h^{(4)} = u}$$

    **Conclusion**

    La cascade des deux systèmes auxiliaires réalise une **linéarisation exacte par bouclage** : la dynamique entrée-sortie de $h$ est exactement celle de **quatre intégrateurs découplés**,

    $$h^{(4)} = u,$$

    indépendamment de $\theta$, $\dot\theta$, $z$, $\dot{z}$. Toute la nonlinéarité du booster est compensée algébriquement par le choix de $v$, et il ne reste plus qu'un système linéaire simple à commander.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 State to Derivatives of the Output

    Implement a function `Tr` of `x, dx, y, dy, theta, dtheta, z, dz` that returns `h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Étant donné l'état $(x, v_x, y, v_y, \theta, \omega, z, \dot{z})$, la transformation $\text{Tr}$ retourne $(h, \dot{h}, \ddot{h}, h^{(3)})$ :

    $$h_x = x - \frac{\ell}{6}\sin\theta, \qquad h_y = y + \frac{\ell}{6}\cos\theta$$

    $$\dot{h}_x = v_x - \frac{\ell\omega}{6}\cos\theta, \qquad \dot{h}_y = v_y - \frac{\ell\omega}{6}\sin\theta$$

    $$\ddot{h}_x = \frac{z\sin\theta}{M}, \qquad \ddot{h}_y = \frac{-z\cos\theta}{M} - g$$

    $$h^{(3)}_x = \frac{\dot{z}\sin\theta + z\omega\cos\theta}{M}, \qquad h^{(3)}_y = \frac{-\dot{z}\cos\theta + z\omega\sin\theta}{M}$$
    """)
    return


@app.cell
def _(M, g, l, np):
    def Tr(x, dx, y, dy, theta, dtheta, z, dz):
        c = np.cos(theta)
        s = np.sin(theta)
        h_x  = x - (l/6) * s
        h_y  = y + (l/6) * c
        dh_x = dx - (l/6) * c * dtheta
        dh_y = dy - (l/6) * s * dtheta
        d2h_x =  (z/M) * s
        d2h_y = -(z/M) * c - g
        d3h_x =  (dz/M) * s + (z/M) * c * dtheta
        d3h_y = -(dz/M) * c + (z/M) * s * dtheta

        return h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y

    return (Tr,)


@app.cell
def _(Tr):
    #Vérification 
    Tr(0,0,0,0,0,0,0,0)
    return


@app.cell
def _(Tr):
    Tr(1.0, 2.0, 3.0, 4.0, 0.1, 0.2, -0.3, -0.4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Inversion


    Assume for the sake of simplicity that $z<0$ at all times. Show that given the values of $h$, $\dot{h}$, $\ddot{h}$ and $h^{(3)}$, one can uniquely compute the booster state (the values of $x$, $\dot{x}$, $y$, $\dot{y}$, $\theta$, $\dot{\theta}$) and auxiliary system state (the values of $z$ and $\dot{z}$).

    Implement the corresponding function `T_inv`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On dispose de $h_x, h_y, \dot h_x, \dot h_y, \ddot h_x, \ddot h_y, h^{(3)}_x, h^{(3)}_y$ et on veut retrouver $x, \dot x, y, \dot y, \theta, \dot\theta, z, \dot z$.

    Étape 1 — extraire $\theta$ et $z$ depuis $\ddot{h}$

    On a :
    $$\ddot{h}_x = \frac{z}{M}\sin\theta, \qquad \ddot{h}_y = -\frac{z}{M}\cos\theta - g$$

    On isole d'abord $\frac{z}{M}\cos\theta$ :
    $$\frac{z}{M}\cos\theta = -(\ddot{h}_y + g)$$

    On a donc le vecteur $\frac{z}{M}(\sin\theta, -\cos\theta)^T = (\ddot h_x,\, \ddot h_y + g)^T$, dont la norme donne $|z|/M$ :

    $$\frac{|z|}{M} = \sqrt{\ddot{h}_x^2 + (\ddot{h}_y + g)^2}$$

    Comme on suppose $z < 0$, on a $|z| = -z$, donc :

    $$\boxed{z = -M\sqrt{\ddot{h}_x^2 + (\ddot{h}_y + g)^2}}$$

    Puis l'angle $\theta$ s'obtient par :
    $$\frac{z}{M}\sin\theta = \ddot{h}_x, \qquad \frac{z}{M}\cos\theta = -(\ddot{h}_y+g)$$

    Comme $z < 0$, on a $\frac{z}{M} < 0$, donc :
    $$\sin\theta = \frac{\ddot{h}_x}{z/M} = \frac{M\ddot{h}_x}{z}, \qquad \cos\theta = \frac{-(\ddot{h}_y+g)}{z/M} = \frac{-M(\ddot{h}_y+g)}{z}$$

    $$\boxed{\theta = \mathrm{atan2}\!\left(\frac{M\ddot{h}_x}{z},\, \frac{-M(\ddot{h}_y+g)}{z}\right) = \mathrm{atan2}(-\ddot{h}_x,\, \ddot{h}_y+g)}$$

    où la simplification du facteur $M/z$ (négatif) retourne le quadrant correct via `atan2`.

    Étape 2 — extraire $\dot\theta$ et $\dot z$ depuis $h^{(3)}$

    On a :
    $$h^{(3)} = \frac{\dot{z}}{M}\begin{pmatrix}\sin\theta\\-\cos\theta\end{pmatrix} + \frac{z\dot\theta}{M}\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix}$$

    C'est un système $2\times 2$ en $(\dot z, \dot\theta)$. En projetant sur les deux vecteurs directeurs orthogonaux $(\sin\theta, -\cos\theta)^T$ et $(\cos\theta, \sin\theta)^T$ :

    **Projection sur $(\sin\theta, -\cos\theta)^T$ :**
    $$h^{(3)}_x\sin\theta - h^{(3)}_y\cos\theta = \frac{\dot{z}}{M}\underbrace{(\sin^2\theta+\cos^2\theta)}_{=1} + \frac{z\dot\theta}{M}\underbrace{(\cos\theta\sin\theta - \sin\theta\cos\theta)}_{=0}$$

    $$\boxed{\dot{z} = M\left(h^{(3)}_x\sin\theta - h^{(3)}_y\cos\theta\right)}$$

    **Projection sur $(\cos\theta, \sin\theta)^T$ :**
    $$h^{(3)}_x\cos\theta + h^{(3)}_y\sin\theta = \frac{\dot{z}}{M}\underbrace{(\sin\theta\cos\theta - \cos\theta\sin\theta)}_{=0} + \frac{z\dot\theta}{M}\underbrace{(\cos^2\theta+\sin^2\theta)}_{=1}$$

    $$\boxed{\dot\theta = \frac{M}{z}\left(h^{(3)}_x\cos\theta + h^{(3)}_y\sin\theta\right)}$$

    Étape 3 — extraire $x, y$ depuis $h$

    Directement depuis la définition de $h$ :

    $$\boxed{x = h_x + \frac{\ell}{6}\sin\theta, \qquad y = h_y - \frac{\ell}{6}\cos\theta}$$

    Étape 4 — extraire $\dot x, \dot y$ depuis $\dot h$

    Depuis $\dot h = (\dot x - \frac{\ell}{6}\cos\theta\,\dot\theta,\; \dot y - \frac{\ell}{6}\sin\theta\,\dot\theta)^T$ :

    $$\boxed{\dot x = \dot h_x + \frac{\ell}{6}\cos\theta\,\dot\theta, \qquad \dot y = \dot h_y + \frac{\ell}{6}\sin\theta\,\dot\theta}$$
    """)
    return


@app.cell
def _(M, g, l, np):
    def T_inv(h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y):
        # Step 1 — z and theta from d2h
        z = -M * np.sqrt(d2h_x**2 + (d2h_y + g)**2)   # z < 0 by assumption

        theta = np.arctan2(-d2h_x, d2h_y + g)
        c = np.cos(theta)
        s = np.sin(theta)

        # Step 2 — dz and dtheta from d3h (projection onto orthogonal basis)
        dz     = M * (d3h_x * s - d3h_y * c)
        dtheta = (M / z) * (d3h_x * c + d3h_y * s)

        # Step 3 — x, y from h
        x = h_x + (l/6) * s
        y = h_y - (l/6) * c

        # Step 4 — dx, dy from dh
        dx = dh_x + (l/6) * c * dtheta
        dy = dh_y + (l/6) * s * dtheta

        return x, dx, y, dy, theta, dtheta, z, dz

    return (T_inv,)


@app.cell
def _(T_inv, Tr):
    T_inv(*Tr(1.0, 2.0, 3.0, 4.0, 0.1, 0.2, -0.3, -0.4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Admissible Path Computation

    Implement a function

    ```python
    def compute(
        x_0,
        dx_0,
        y_0,
        dy_0,
        theta_0,
        dtheta_0,
        z_0,
        dz_0,
        x_tf,
        dx_tf,
        y_tf,
        dy_tf,
        theta_tf,
        dtheta_tf,
        z_tf,
        dz_tf,
        tf,
    ):
        ...

    ```

    that returns a function `fun` such that `fun(t)` is a value of `x, dx, y, dy, theta, dtheta, z, dz, f, phi` at time `t` that match the initial and final values provided as arguments to `compute`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On veut faire atterrir le booster. On connaît son état de départ (position, vitesse, angle…) et son état d'arrivée (posé, droit, immobile).

    La difficulté, c'est que le booster est un système physique non linéaire — ses équations de mouvement sont compliquées, avec des $\sin$, des $\cos$, des couplages entre la rotation et la translation. Planifier une trajectoire directement dans l'espace physique $(x, y, \theta)$ est un cauchemar.

    On a montré qu'il existe un point particulier du booster, situé à $\ell/6$ au-dessus du centre de masse, dont la position $(h_x, h_y)$ obéit à une dynamique très simple :

    $$h^{(4)}(t) = u(t)$$

    La fonction `Tr` calcule, à partir de l'état physique du booster, les valeurs de $h$ et ses trois premières dérivées :

    $$\text{Tr}(x, \dot x, y, \dot y, \theta, \omega, z, \dot z) \;\longmapsto\; \big(h_x,\, h_y,\, \dot h_x,\, \dot h_y,\, \ddot h_x,\, \ddot h_y,\, h^{(3)}_x,\, h^{(3)}_y\big)$$

    On obtient donc **8 valeurs à $t=0$** et **8 valeurs à $t=t_f$**, soit **16 conditions aux limites** au total (8 par composante de $h$).

    Pour que la trajectoire soit physiquement réalisable (vitesse, accélération ...), il faut imposer $h$, $\dot h$, $\ddot h$ et $h^{(3)}$ aux deux extrémités.

    On cherche une fonction $h_x(t)$ qui :
    - vaut $h_{x,0}$ à $t=0$
    - a la même dérivée première, deuxième et troisième qu'à l'état initial
    - vaut $h_{x,f}$ à $t=t_f$
    - a la même dérivée première, deuxième et troisième qu'à l'état final

    C'est **8 conditions**. Un polynôme de degré 7 a exactement **8 coefficients libres** :

    $$h_x(t) = c_0 + c_1 t + c_2 t^2 + c_3 t^3 + c_4 t^4 + c_5 t^5 + c_6 t^6 + c_7 t^7$$

    8 inconnues, 8 équations → système linéaire, solution unique.


    Au lieu de travailler avec le temps $t \in [0, t_f]$, on normalise : $s = t/t_f \in [0, 1]$.

    Pour des raisons numériques. Si $t_f = 10$ secondes, les puissances $t^7 = 10^7 = 10\,000\,000$ deviennent énormes. Avec $s \in [0,1]$, toutes les puissances restent entre 0 et 1.

    La conversion des dérivées est immédiate :

    $$\frac{d}{dt} = \frac{1}{t_f}\frac{d}{ds}, \quad \frac{d^2}{dt^2} = \frac{1}{t_f^2}\frac{d^2}{ds^2}, \quad \frac{d^3}{dt^3} = \frac{1}{t_f^3}\frac{d^3}{ds^3}$$


    On resoud Le système linéaire :

    Les 4 conditions à $s = 0$ donnent directement les premiers coefficients :

    $$p(0) = c_0 \implies c_0 = b_0[0]$$
    $$p'(0) = c_1 \implies c_1 = b_0[1]$$
    $$p''(0) = 2c_2 \implies c_2 = b_0[2]/2$$
    $$p'''(0) = 6c_3 \implies c_3 = b_0[3]/6$$

    Les 4 conditions à $s = 1$ donnent un système $4 \times 4$ en $(c_4, c_5, c_6, c_7)$ :

    $$\begin{pmatrix} 1 & 1 & 1 & 1 \\ 4 & 5 & 6 & 7 \\ 12 & 20 & 30 & 42 \\ 24 & 60 & 120 & 210 \end{pmatrix} \begin{pmatrix} c_4 \\ c_5 \\ c_6 \\ c_7 \end{pmatrix} = \begin{pmatrix} b_1[0] - (c_0+c_1+c_2+c_3) \\ b_1[1] - (c_1+2c_2+3c_3) \\ b_1[2] - (2c_2+6c_3) \\ b_1[3] - 6c_3 \end{pmatrix}$$

    Les colonnes de la matrice viennent des dérivées de $s^4, s^5, s^6, s^7$ évaluées en $s=1$ :

    | Polynôme | $p(1)$ | $p'(1)$ | $p''(1)$ | $p'''(1)$ |
    |---|---|---|---|---|
    | $s^4$ | 1 | 4 | 12 | 24 |
    | $s^5$ | 1 | 5 | 20 | 60 |
    | $s^6$ | 1 | 6 | 30 | 120 |
    | $s^7$ | 1 | 7 | 42 | 210 |

    Cette matrice est toujours inversible (c'est une matrice de type Vandermonde des dérivées), donc `np.linalg.solve` donne une solution unique.


    On Évaluer le polynôme et ses dérivées avec `np.polyder`

    On a planifié le chemin de $h(t)$ dans l'espace plat. Maintenant, à chaque instant $t$, on connaît $(h, \dot h, \ddot h, h^{(3)})$. La fonction `T_inv` invertit la transformation `Tr` pour retrouver l'état physique $(x, \dot x, y, \dot y, \theta, \omega, z, \dot z)$.

    On a le chemin, mais on veut savoir **quelle poussée** et **quel angle de gicleur** produisent ce chemin.

    On a montré que :

    $$h^{(4)} = \frac{v_1}{M}\mathbf{n} + \frac{v_2}{M}\mathbf{t} + \text{termes non linéaires}$$

    où $\mathbf{n} = (\sin\theta, -\cos\theta)$ et $\mathbf{t} = (\cos\theta, \sin\theta)$.

    On les soustrait de $h^{(4)}$ (que l'on connaît depuis le polynôme), puis on projette sur $(\mathbf{n}, \mathbf{t})$ pour isoler $v_1$ et $v_2$ :

    $$\text{rhs} = h^{(4)} - \text{termes non linéaires}$$

    $$v_1 = M\,(\text{rhs}\cdot\mathbf{n}) = M\,(\text{rhs}_x \sin\theta - \text{rhs}_y \cos\theta)$$

    $$v_2 = M\,(\text{rhs}\cdot\mathbf{t}) = M\,(\text{rhs}_x \cos\theta + \text{rhs}_y \sin\theta)$$

    Puis il faut récupérer $(f_x, f_y)$ depuis le premier système auxiliaire

    Le premier système auxiliaire définit les composantes de force :

    $$\begin{pmatrix}f_x \\ f_y\end{pmatrix} = R(\theta - \pi/2)\begin{pmatrix}z - \frac{M\ell\omega^2}{6} \\ \frac{M\ell v_2}{6z}\end{pmatrix} = \begin{pmatrix}\sin\theta & \cos\theta \\ -\cos\theta & \sin\theta\end{pmatrix}\begin{pmatrix}f_1^{\text{body}} \\ f_2^{\text{body}}\end{pmatrix}$$


    Puis la rotation donne $(f_x, f_y)$ dans le repère monde.

    La norme de $(f_x, f_y)$ donne la poussée totale :

    $$f = \sqrt{f_x^2 + f_y^2}$$

    L'angle de gicleur $\phi$ est l'angle entre la force et l'axe du booster :

    $$\phi = \arctan2(-f_x, f_y) + \phi$$
    """)
    return


@app.cell
def _(M, T_inv, Tr, l, np):
    def compute(
        x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0,
        x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf,
        tf,
    ):

        h_0  = Tr(x_0,  dx_0,  y_0,  dy_0,  theta_0,  dtheta_0,  z_0,  dz_0)
        h_tf = Tr(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf)

        (hx0,  hy0,
         dhx0,  dhy0,
         d2hx0,  d2hy0,
         d3hx0,  d3hy0)  = h_0

        (hxf,  hyf,
         dhxf,  dhyf,
         d2hxf,  d2hyf,
         d3hxf,  d3hyf) = h_tf

        # 2. degree-7 polynomial fit (one per component)
        # We work on the normalised time s = t/tf ∈ [0,1] to keep the Vandermonde
        # matrix well-conditioned, then convert derivatives accordingly.
        #
        # If p(s) is the normalised poly, then:
        #   d/dt   = (1/tf)   d/ds
        #   d2/dt2 = (1/tf^2) d2/ds2
        #   d3/dt3 = (1/tf^3) d3/ds3

        def fit_poly7(a0, da0, d2a0, d3a0, af, daf, d2af, d3af, tf):
            """
            Return coefficients c of degree-7 polynomial p(s) = sum c[k] s^k
            satisfying the 8 boundary conditions at s=0 and s=1.
            Derivatives are w.r.t. original time t (converted internally).
            """
            # convert to s-derivatives
            b0 = [a0,
                  da0   * tf,
                  d2a0  * tf**2,
                  d3a0  * tf**3]
            b1 = [af,
                  daf   * tf,
                  d2af  * tf**2,
                  d3af  * tf**3]

            # Vandermonde-style matrix for p(0), p'(0), p''(0), p'''(0)
            # p(s)   = c0 + c1 s + c2 s^2 + ... + c7 s^7
            # at s=0: only the lowest-order terms survive
            # at s=1: sum of all coefficients and their derivatives

            # Conditions at s=0:
            #   p(0)   = c0
            #   p'(0)  = c1
            #   p''(0) = 2 c2
            #   p'''(0)= 6 c3
            # => c0,c1,c2,c3 determined immediately
            c0 = b0[0]
            c1 = b0[1]
            c2 = b0[2] / 2
            c3 = b0[3] / 6

            # Conditions at s=1 give 4 equations in (c4,c5,c6,c7):
            # p(1)   = c0+c1+c2+c3 + c4+c5+c6+c7                  = b1[0]
            # p'(1)  = c1+2c2+3c3  + 4c4+5c5+6c6+7c7              = b1[1]
            # p''(1) = 2c2+6c3     + 12c4+20c5+30c6+42c7           = b1[2]
            # p'''(1)= 6c3         + 24c4+60c5+120c6+210c7         = b1[3]

            known0 = c0 + c1 + c2 + c3
            known1 = c1 + 2*c2 + 3*c3
            known2 = 2*c2 + 6*c3
            known3 = 6*c3

            rhs = np.array([
                b1[0] - known0,
                b1[1] - known1,
                b1[2] - known2,
                b1[3] - known3,
            ])

            A = np.array([
                [1,   1,   1,   1  ],
                [4,   5,   6,   7  ],
                [12,  20,  30,  42 ],
                [24,  60,  120, 210],
            ])

            c4567 = np.linalg.solve(A, rhs)
            return np.array([c0, c1, c2, c3, *c4567])

        cx = fit_poly7(hx0,  dhx0,  d2hx0,  d3hx0,
                       hxf,  dhxf,  d2hxf,  d3hxf,  tf)

        cy = fit_poly7(hy0,  dhy0,  d2hy0,  d3hy0,
                       hyf,  dhyf,  d2hyf,  d3hyf,  tf)

        # 3. polynomial evaluation helpers
        def poly_derivs(c, s, tf):
            """
            Given normalised coefficients c and s = t/tf,
            return p, p', p'', p''', p'''' w.r.t. original time t.
            """
            # build derivative coefficient arrays w.r.t. s
            c1 = np.polyder(c[::-1])[::-1]   # d/ds,   degree 6
            c2 = np.polyder(c1[::-1])[::-1]  # d2/ds2, degree 5
            c3 = np.polyder(c2[::-1])[::-1]  # d3/ds3, degree 4
            c4 = np.polyder(c3[::-1])[::-1]  # d4/ds4, degree 3

            p   = np.polyval(c[::-1],  s)
            dp  = np.polyval(c1[::-1], s) / tf
            d2p = np.polyval(c2[::-1], s) / tf**2
            d3p = np.polyval(c3[::-1], s) / tf**3
            d4p = np.polyval(c4[::-1], s) / tf**4

            return p, dp, d2p, d3p, d4p

        # 4. trajectory function
        def fun(t):
            s = t / tf

            hx,  dhx,  d2hx,  d3hx,  d4hx  = poly_derivs(cx, s, tf)
            hy,  dhy,  d2hy,  d3hy,  d4hy  = poly_derivs(cy, s, tf)

            # recover full state
            x, dx, y, dy, theta, dtheta, z, dz = T_inv(
                hx, hy, dhx, dhy, d2hx, d2hy, d3hx, d3hy
            )

            # recover v from d4h = P(theta) v/M + nonlinear terms  (see h^(4) formula)
            # => v = M P^{-1} (d4h - nonlinear)
            # P(theta)^{-1} = [[sin, -cos],[cos, sin]]
            c_t, s_t = np.cos(theta), np.sin(theta)

            nl_x = (2*dz*dtheta/M)*c_t - (z*dtheta**2/M)*s_t
            nl_y = (2*dz*dtheta/M)*s_t + (z*dtheta**2/M)*c_t

            rhs_x = d4hx - nl_x
            rhs_y = d4hy - nl_y

            # P^{-1} = [[s_t, -c_t],[c_t, s_t]]
            v1 = M * ( s_t * rhs_x - c_t * rhs_y)
            v2 = M * ( c_t * rhs_x + s_t * rhs_y)

            # recover (fx, fy) from the first auxiliary system
            # [fx, fy] = R(theta-pi/2) @ [z - Ml dtheta^2/6, Ml v2/(6z)]
            f1_body = z - (M*l/6)*dtheta**2
            f2_body = (M*l*v2) / (6*z)

            fx =  s_t * f1_body + c_t * f2_body
            fy = -c_t * f1_body + s_t * f2_body

            # total thrust magnitude and gimbal angle
            f   = np.sqrt(fx**2 + fy**2)
            phi = np.arctan2(-fx, +fy) - theta   # angle of thrust w.r.t. -y body axis

            return x, dx, y, dy, theta, dtheta, z, dz, f, phi

        return fun

    return (compute,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Graphical Validation

    Test your `compute` function with

    - `(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0) = (5.0, 0.0, 20.0, -1.0, -np.pi/8, 0.0, -M*g, 0.0`),
    - `(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf) = (0.0, 0.0, 2/3*l, 0.0,     0.0, 0.0, -M*g, 0.0`),
    - `tf = 10.0`.

    Make the graph of the relevant variables as a function of time, then make an animation out of the same result. Comment and iterate if necessary!
    """)
    return


@app.cell
def _(M, compute, g, l, np):
    tf = 10
    fun = compute(5.0, 0.0, 20.0, -1.0, -np.pi/8, 0.0, -M*g, 0.0, 0.0, 0.0, 2/3*l, 0.0, 0.0, 0.0, -M*g, 0.0, tf)
    return fun, tf


@app.cell
def _(booster_anim, fun, mo, tf, world):
    def _anim():
        t_span = [0.0, tf]
        x = lambda t: fun(t)[0]
        y = lambda t: fun(t)[2]
        theta = lambda t : fun(t)[4]
        f = lambda t: fun(t)[-2]
        phi = lambda t: fun(t)[-1]
        return mo.Html(
            world(
                [-20, 20, -5, 20], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell
def _(M, compute, g, l, np, plt, tf):
    import matplotlib.gridspec as gridspec
    from matplotlib.patches import FancyArrowPatch
    import matplotlib.patheffects as pe

    IC = dict(x_0=5.0,   dx_0=0.0,  y_0=20.0,  dy_0=-1.0,
              theta_0=-np.pi/8, dtheta_0=0.0, z_0=-M*g, dz_0=0.0)
    FC = dict(x_tf=0.0,  dx_tf=0.0, y_tf=2/3*l, dy_tf=0.0,
              theta_tf=0.0, dtheta_tf=0.0, z_tf=-M*g, dz_tf=0.0)

    traj = compute(**IC, **FC, tf=tf)

    t_vals = np.linspace(0, tf, 600)
    R = np.array([traj(t) for t in t_vals])
    x_t, dx_t, y_t, dy_t   = R[:,0], R[:,1], R[:,2], R[:,3]
    theta_t, omega_t        = R[:,4], R[:,5]
    z_t, dz_t_arr          = R[:,6], R[:,7]
    f_t, phi_t             = R[:,8], R[:,9]

    fx_t = M * np.array([np.gradient(np.gradient(R[:,0], t_vals), t_vals)[i]
                          for i in range(len(t_vals))])  # d2x/dt2 * M
    fy_t = M * (np.gradient(np.gradient(R[:,2], t_vals), t_vals)
                + g * np.ones(len(t_vals)))

    phi_fixed = np.arctan2(-fx_t, fy_t) - theta_t

    fig2, ax2 = plt.subplots(figsize=(7, 11))
    fig2.patch.set_facecolor('#0f0f1a')
    ax2.set_facecolor('#161629')

    # Ground
    ax2.axhline(0, color='#444', lw=1.5)
    ax2.fill_between([-1, 7], -0.3, 0, color='#2d2d2d', zorder=1)

    # CoM path
    sc = ax2.scatter(x_t, y_t, c=t_vals, cmap='plasma', s=8, zorder=3, alpha=0.9)
    cbar = plt.colorbar(sc, ax=ax2, fraction=0.03, pad=0.02)
    cbar.set_label('t [s]', color='white', fontsize=9)
    cbar.ax.yaxis.set_tick_params(color='white', labelcolor='white')

    # h path
    h_x = x_t - (l/6)*np.sin(theta_t)
    h_y = y_t + (l/6)*np.cos(theta_t)
    ax2.plot(h_x, h_y, color='#00d4ff', lw=1.2, ls='--', alpha=0.5,
             label=r'$h(t)$ — flat output path', zorder=2)

    # Booster snapshots at a few instants
    snap_times = np.linspace(0, tf, 9)
    for ts in snap_times:
        rs = traj(ts)
        xs, _, ys = rs[0], rs[1], rs[2]
        ths = rs[4]
        # booster body: line from bottom to top
        half = l / 2
        bx0, by0 = xs + half*np.sin(ths),  ys - half*np.cos(ths)   # bottom (nozzle)
        bx1, by1 = xs - half*np.sin(ths),  ys + half*np.cos(ths)   # top
        alpha_snap = 0.3 + 0.5*(ts/tf)
        ax2.plot([bx0, bx1], [by0, by1], color='#51cf66',
                 lw=3, alpha=alpha_snap, solid_capstyle='round', zorder=4)
        # CoM dot
        ax2.plot(xs, ys, 'o', color='white', ms=4, zorder=5, alpha=alpha_snap)
        # h dot
        hxs = xs - (l/6)*np.sin(ths)
        hys = ys + (l/6)*np.cos(ths)
        ax2.plot(hxs, hys, 's', color='#00d4ff', ms=3, zorder=5, alpha=alpha_snap)

    # Start / End markers
    ax2.plot(IC['x_0'], IC['y_0'], 'o', color='#ffd43b', ms=12,
             zorder=6, label=f"Start ({IC['x_0']}, {IC['y_0']})")
    ax2.plot(FC['x_tf'], FC['y_tf'], '*', color='#ff6b6b', ms=14,
             zorder=6, label=f"Target ({FC['x_tf']}, {FC['y_tf']:.3f})")

    ax2.set_xlim(-1.5, 7)
    ax2.set_ylim(-0.5, 22)
    ax2.set_xlabel('x [m]', color='white', fontsize=11)
    ax2.set_ylabel('y [m]', color='white', fontsize=11)
    ax2.set_title('Booster Trajectory',
                  color='white', fontsize=12, fontweight='bold')
    ax2.tick_params(colors='#aaa', labelsize=9)
    for sp in ax2.spines.values(): sp.set_edgecolor('#333')
    ax2.legend(facecolor='#222', labelcolor='white', edgecolor='#444',
               fontsize=9, loc='upper right')
    ax2.set_aspect('equal', adjustable='datalim')
    plt.tight_layout()
    plt.show()

    return f_t, phi_fixed, sp, t_vals


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le chemin du centre de masse (colorié par le temps) montre une courbe douce du point de départ $(5, 20)$ vers la cible $(0, 1.33)$. En pointillés, on voit le chemin de la **sortie plate** $h(t)$  ce petit point situé à $\ell/6$ au-dessus du centre de masse, dont on a planifié le mouvement par le polynôme. Les deux chemins sont proches mais distincts, car $h$ et le CoM sont décalés d'une distance $\ell/6$ dans la direction de l'axe du booster.

    Les "bâtons" verts représentent le booster à différents instants. On voit clairement la rotation : le booster se couche vers $t \approx 2.5$ s, puis se redresse progressivement. À l'atterrissage, il est vertical exactement comme demandé.
    """)
    return


@app.cell
def _(M, f_t, g, np, phi_fixed, plt, sp, t_vals):
    fig3, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4))
    fig3.patch.set_facecolor('#0f0f1a')
    for ax in (a1, a2):
        ax.set_facecolor('#161629')
        ax.tick_params(colors='#888', labelsize=8)
        for _sp in ax.spines.values(): sp.set_edgecolor('#333')

    a1.plot(t_vals, f_t, color='#ff922b', lw=2.2)
    a1.axhline(M*g, color='white', ls='--', lw=1, alpha=0.5, label=f'Mg = {M*g}')
    a1.set_title(r'Thrust $f(t)$', color='white', fontsize=11)
    a1.set_xlabel('t [s]', color='#888'); a1.set_ylabel('N', color='#888')
    a1.legend(facecolor='#222', labelcolor='white', edgecolor='#444', fontsize=9)

    a2.plot(t_vals, np.degrees(phi_fixed), color='#cc5de8', lw=2.2, label=r'$\phi$ (fixed)')
    a2.axhline( 90, color='red',   ls='--', lw=1, alpha=0.5, label='±90° limit')
    a2.axhline(-90, color='red',   ls='--', lw=1, alpha=0.5)
    a2.axhline(  0, color='white', ls=':',  lw=0.6, alpha=0.3)
    a2.set_title(r'Gimbal angle $\phi(t)$ [°]', color='white', fontsize=11)
    a2.set_xlabel('t [s]', color='#888'); a2.set_ylabel('degrees', color='#888')
    a2.legend(facecolor='#222', labelcolor='white', edgecolor='#444', fontsize=9)

    fig3.suptitle('Control Inputs', color='white', fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(fun, np, plt, tf):
    x_init     = 5 
    y_init     = 20
    theta_init =-np.pi/8



    def _():
        # 1. Data Generation
        t_eval = np.linspace(0, tf, 500)
        results = np.array([fun(t) for t in t_eval])

        # Extracting the 10 variables (Transpose to get columns)
        x, dx, y, dy, theta, dtheta, z, dz, f, phi = results.T

        # 2. Static Graphs of Relevant Variables
        fig, axs = plt.subplots(3, 2, figsize=(12, 12))
        plt.subplots_adjust(hspace=0.4, wspace=0.3)

        # Trajectory components
        axs[0, 0].plot(t_eval, x, label='$x(t)$', color='blue')
        axs[0, 0].plot(t_eval, y, label='$y(t)$', color='green')
        axs[0, 0].set_title("Positions vs Time")
        axs[0, 0].legend()
        axs[0, 0].grid(True)

        # Velocities
        axs[0, 1].plot(t_eval, dx, label='$\dot{x}$', linestyle='--')
        axs[0, 1].plot(t_eval, dy, label='$\dot{y}$', linestyle='--')
        axs[0, 1].set_title("Velocities vs Time")
        axs[0, 1].legend()
        axs[0, 1].grid(True)

        # Orientation (Theta)
        axs[1, 0].plot(t_eval, np.degrees(theta), color='purple')
        axs[1, 0].set_title("Angle $\\theta$ (degrees) vs Time")
        axs[1, 0].set_ylabel("Degrees")
        axs[1, 0].grid(True)

        # Command Angle (Phi)
        axs[1, 1].plot(t_eval, np.degrees(phi), color='orange')
        axs[1, 1].set_title("Control Angle $\\phi$ (degrees) vs Time")
        axs[1, 1].grid(True)

        # Force/Thrust (f)
        axs[2, 0].plot(t_eval, f, color='brown')
        axs[2, 0].set_title("Thrust Force $f$ vs Time")
        axs[2, 0].grid(True)

        # Phase Space (X-Z trajectory)
        axs[2, 1].plot(x, y)
        axs[2, 1].set_title("Vertical Profile (Y-X Plane)")
        axs[2, 1].set_xlabel("y")
        axs[2, 1].set_ylabel("x")
        axs[2, 1].grid(True)
        return plt.show()


    _()
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ce notebook a construit, de zéro, une trajectoire d'atterrissage complète pour un booster réutilisable. On est partis des équations de la physique, on a trouvé une transformation algébrique (la sortie plate $h$) qui simplifie radicalement le problème, et on a planifié dans cet espace simplifié.

    Le résultat : une trajectoire calculée en une fraction de seconde, valide pour des grandes inclinaisons, avec des conditions aux limites respectées à l'erreur numérique près.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusion du notebook

    Ce projet nous a emmenés d'une feuille blanche jusqu'à un système de contrôle complet pour un booster en atterrissage.

    On a commencé par modéliser physiquement le système : forces, couples, centre de masse, moment d'inertie. On a simulé le comportement non linéaire libre. Puis on a linéarisé autour de l'équilibre pour concevoir des contrôleurs classiques.

    On a transformé un système non linéaire couplé en deux intégrateurs quadruples indépendants. Cette transformation est exacte pas une approximation. Elle a rendu la planification de trajectoire triviale

    Le résultat sur les graphes parle de lui-même : une trajectoire fluide, physiquement cohérente, avec des conditions aux limites respectées.

    C'est ça, la puissance de la théorie du contrôle moderne.
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
