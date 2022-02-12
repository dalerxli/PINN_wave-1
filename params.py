"""
********************************************************************************
all your params
********************************************************************************
"""

# network structure
f_in  = 3
f_out = 1
width = 2 ** 8   # 2 ** 6 = 64, 2 ** 8 = 256
depth = 5 

# training setting
n_epch = int(1e4)
n_btch = 2 ** 12   # 2 ** 6 = 64, 2 ** 8 = 256
c_tol  = 1e-8

# initializers
w_init = "Glorot"
b_init = "zeros"

# optimization
act = "tanh"
lr  = 5e-4
opt = "Adam"
f_scl = "minmax"   # "minmax" or "mean"
laaf = True

# system params
c = 1.

# weights
w_ini = 1.
w_bnd = 1.
w_pde = 1.

# boundary condition 
BC = "Neu"   # "Dir" for Dirichlet, "Neu" for Neumann

# rarely changed params
f_mntr = 10
r_seed = 1234

def params():
    return \
                f_in, f_out, width, depth, \
                w_init, b_init, act, \
                lr, opt, \
                f_scl, laaf, c, \
                w_ini, w_bnd, w_pde, BC, \
                f_mntr, r_seed, \
                n_epch, n_btch, c_tol, \

