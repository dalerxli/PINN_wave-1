# PINN: Physics-Informed Neural Network (for 2D wave equation)

This is an implementation of PINN(s): Physics-Informed Neural Network(s) to solve 2D wave equation. It considers a square domain with Dirichlet / Neumann boundary condition. One can choose which boundary condition, and initial condition within 

<br>
One can find the details of PINN in their [paper](https://www.sciencedirect.com/science/article/pii/S0021999118307125). Training is accelerated with [L-LAAF](https://royalsocietypublishing.org/doi/10.1098/rspa.2020.0334)



This repo considers 0<= x, y <= 5

### Reference:
[1] Raissi, M., Perdikaris, P., Karniadakis,  G.E.: Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations, Journal of Computational Physics, Vol. 378, pp. 686-707, 2019. ([paper](https://www.sciencedirect.com/science/article/pii/S0021999118307125))
<br>
[2] Jagtap, A.D., Kawaguchi K., Karniadakis, G.E.: Locally adaptive activation functions with slope recovery for deep and physics-informed neural networks, Proceedings of Royal Society A, pp.4762020033420200334, 2020. ([paper](https://royalsocietypublishing.org/doi/10.1098/rspa.2020.0334))

### Dependencies
Tested on the following environment. 
---------------------------- -------------------
Package                      Version
---------------------------- -------------------
Python                       3.8.10
---------------------------- -------------------
h5py                         3.6.0
keras                        2.8.0
Keras-Preprocessing          1.1.2
matplotlib                   3.5.1
numpy                        1.22.1
pandas                       1.4.0
pip                          22.0.3
scipy                        1.7.3
tensorboard                  2.8.0
tensorboard-data-server      0.6.1
tensorboard-plugin-wit       1.8.1
tensorflow                   2.8.0
tensorflow-io-gcs-filesystem 0.23.1
wheel                        0.37.1
wrapt                        1.13.3
zipp                         3.7.0
