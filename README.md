# PINN(s): Physics-Informed Neural Network(s)

This is an implementation of [PINN(s)](https://doi.org/10.1016/j.jcp.2018.10.045) on TensorFlow 2. This code solve 2D wave equation under Dirichlet / Neumann boundary condition without training data (data to fit initial & boundary conditions need to be provided). PINN-derived solution is compared with FDM (Finite Difference Method) approximation to quantitatively show a good agreement. While training could be accelerated with GPU-utilized learning, this code also implements [L-LAAF](https://doi.org/10.1098/rspa.2020.0334) for further speed-up. 

## Usage
Simply type
<br>
<code>
  python main.py
</code>
<br>
to run the code (this includes FDM simulation, PINN training, inferece, and comparison). Basic parameters (e.g., network architecture, batch size, initializer, etc.) are found in 
<br>
<code>
  params.py
</code>
<br>
and could be modified depending on the problem setup. 

## Dependencies
Tested on 
<br>
<code>
  python 3.8.10
</code>
with the following:

|Package                      |Version|
| :---: | :---: |
|numpy                        |1.22.1|
|scipy                        |1.7.3|
|tensorflow                   |2.8.0|

## Reference:
[1] Raissi, M., Perdikaris, P., Karniadakis, G.E.: Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations, Journal of Computational Physics, Vol. 378, pp. 686-707, 2019. 
<br>
[2] Jagtap, A.D., Kawaguchi, K., Karniadakis, GE.: Locally adaptive activation functions with slope recovery for deep and physics-informed neural networks, Proceedings of Royal Society A, pp. 4762020033420200334, 2020. 
