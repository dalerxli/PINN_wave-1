# PINN: Physics-Informed Neural Network (for 2D wave equation)

This is an implementation of [PINN(s): Physics-Informed Neural Network(s)](https://www.sciencedirect.com/science/article/pii/S0021999118307125) to solve 2D wave equation. It considers a square domain with Dirichlet / Neumann boundary condition, and is capable to simulate the wave propagation without any training data (data on initial & boundary conditions need to be provided). This code also investigates PINN-derived solution vs FDM (Finit Difference Method) approximation, and quantitatively compares their agreement. Training is speeded up with [L-LAAF](https://royalsocietypublishing.org/doi/10.1098/rspa.2020.0334), and could be further accelerated with GPU-utilized training. 

### Usage
Simply type 
<br>
<code>python main.py</code>
<br>
to run the code (this includes FDM simulation, PINN training, and inference). Basic parameters (e.g., network architecture, weight initializer, batch size, etc.) could be found in 
<br>
<code>params.py</code>
<br>
file and modified on your preferred setting. 

### Dependencies
Tested on 
<br>
<code>Python 3.8.10</code>
<br>
and the following environment. 

| Package | Version |
| :---: | :---: |
| keras | 2.8.0 |
| matplotlib|                    3.5.1| 
| numpy|                         1.22.1| 
| scipy|                         1.7.3| 
| tensorflow|                    2.8.0| 

### Reference:
[1] Raissi, M., Perdikaris, P., Karniadakis,  G.E.: Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations, Journal of Computational Physics, Vol. 378, pp. 686-707, 2019. ([paper](https://www.sciencedirect.com/science/article/pii/S0021999118307125))
<br>
[2] Jagtap, A.D., Kawaguchi K., Karniadakis, G.E.: Locally adaptive activation functions with slope recovery for deep and physics-informed neural networks, Proceedings of Royal Society A, pp. 4762020033420200334, 2020. ([paper](https://royalsocietypublishing.org/doi/10.1098/rspa.2020.0334))
