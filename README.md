# PINN(s): Physics-Informed Neural Network(s)

This is an implementation of [PINN(s): Physics-Informed Neural Network(s)](https://doi.org/10.1016/j.jcp.2018.10.045) on TensorFlow 2. This code solve 2D wave equation under Dirichlet / Neumann boundary condition without training data (data to fit initial & boundary conditions need to be provided). PINN-derived solution is compared with FDM (Finite Difference Method) approximation to quantitatively show a good agreement. 

One can find and change the initial / boundary condition in <code>FDM.py</code> and <code>prp_dat.py</code>.

<br>
Training could be accelerated with GPU-utilized  is speeded up with [L-LAAF](https://doi.org/10.1098/rspa.2020.0334)

## Usage
Simply type
<br>
<code>
  python main.py
</code>
<br>
to run the code (this includes FDM simulation, PINN training, and inferece). Basic parameters (e.g., network architecture, batch size, initializer, etc.) are found in 
<br>
<code>
  params.py
</code>
<br>
and could be modified depending on the problem setup. 

## Dependencies
Tested on 
Simply type
<p>
<code>
  python 3.8.10
</code>
</p>
with the following:
packages
version

## Reference:
[1] Raissi, M., Perdikaris, P., Karniadakis, G.E.: Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations, Journal of Computational Physics, Vol. 378, pp. 686-707, 2019. 
<br>
[2] Jagtap, A.D., Kawaguchi, K., Karniadakis, GE.: Locally adaptive activation functions with slope recovery for deep and physics-informed neural networks, Proceedings of Royal Society A, pp. 4762020033420200334, 2020. 
