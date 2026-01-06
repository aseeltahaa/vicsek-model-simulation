# Vicsek Model Simulation – Active Matter
![Vicsek Model Animation](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzJrNG50NG9vc3pmM2gwMW11bzY3NmkxMmJqYzltamtiZ2RicnJ0eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3h3tVn3DL9NUPrSJnV/giphy.gif)

## Overview

**Active matter** refers to systems of individual agents that consume energy to self-propel, creating organized motion and complex patterns, known as **collective behavior**, far from equilibrium. Examples include bacterial colonies, bird flocks, and fish schools.

The **Vicsek Model** is a classic mathematical model in statistical physics and active matter studies, introduced by Tamas Vicsek in 1995. It simulates **self-propelled particles in 2D** to demonstrate how simple local interactions lead to global alignment (emergent order).

This project implements the Vicsek Model in Python and allows for **simulation, visualization, and parameter analysis**.

---

## How the Model Works

Imagine a group of birds flying in a 2D box:

1. Each bird has a **position** and a **direction**. All birds move at the same **constant speed**.
2. Each bird observes its **neighbors within a radius `r`** and aligns with the **average direction** of those neighbors.
3. Random **noise η** is added to simulate imperfect alignment.
4. The process repeats at discrete **time steps**, leading to emergent flocking behavior over time.

---

## Key Components

- **Particles:**  
  - Position: \(x_i(t)\)  
  - Velocity: \(\vec{v}_i(t) = v_0 (\cos \theta_i, \sin \theta_i)\)  
    where \(v_0\) is constant speed and \(\theta_i\) is particle direction.  

- **Time Step:** Discrete steps \(t, t+\Delta t, t+2\Delta t, …\)  

- **Neighborhood:** Only particles within radius `r` influence each other.  

- **Noise:** Random directional perturbation η, simulating imperfect alignment.

---

## Update Rules

At each time step:

1. **Update direction**:

\[
\theta_i(t+\Delta t) = \langle \theta_j(t) \rangle_{j \in N_i} + \eta \xi_i
\]

Where:  
- \(\langle \theta_j(t) \rangle\) = average direction of neighbors  
- \(\xi_i \in [-1/2, 1/2]\) = random number  
- η = noise amplitude  

2. **Update position**:

\[
x_i(t+\Delta t) = x_i(t) + v_0 \cdot (\cos \theta_i(t+\Delta t), \sin \theta_i(t+\Delta t)) \cdot \Delta t
\]

3. **Periodic boundaries:** Particles leaving the box re-enter from the opposite side.

---

## Measuring Global Order

The system’s alignment is quantified with the **order parameter φ**:

\[
\phi = \frac{1}{N} \left| \sum_{i=1}^{N} \frac{\vec{v}_i}{v_0} \right|
\]

- φ ≈ 1 → highly aligned (ordered flocking)  
- φ ≈ 0 → random directions (disordered motion)

By varying:

- **Noise η**  
- **Particle density ρ = N / L²**  
- **Particle speed v₀**  

we can observe **phase transitions** from disorder to order.

---

## Features

- **Simulate** the Vicsek model in Python.  
- **Visualize** particle motion with real-time animation.  
- **Track** the order parameter φ over time.  
- **Sweep parameters** (η, R, v₀) to study their effect on collective motion.  

---

## References

T. Vicsek et al., Phys. Rev. Lett., 1995.
Ginelli, F., The Physics of the Vicsek Model, SUPA, ICSMB and Department of Physics, King’s College, University of Aberdeen, Aberdeen AB24 3UE, United Kingdom, March 22, 2016.
Active Matter and Collective Motion literature
cd vicsek-model
