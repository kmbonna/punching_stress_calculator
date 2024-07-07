# Punching Stress Calculator

This program was designed to check whether a particular column is safe to be built in a house or would it cause **punching** on the roof. We are comparing the punching stress of the column with the allowable for the stress of the house roof.

The program takes inputs from the user of the dimensions of the columns and its position in the house and determines if its safe or not.

## Punching Stress:
$$ qp =  \frac{QU * \beta}{B_{o} * \text{depth}} $$ 

Allowable:
$$ max(0.316 \sqrt{\frac{f_{cu}}{\gamma_{c}}},1.6) $$

where $QU$ is the Ultimate Shear Force, $\beta$ is a coefficient for the position of the pole in the place, $B_{o}$ is the perimeter of the slab, and depth is the depth of the slab.

$ \beta = 1.15$ for interior column

$ \beta = 1.30$ for exterior column

$ \beta = 1.50$ for corner column


## QU equation:
for interior columns:
$$ QU = w_{u}(L_{1}*L_{2} - a_{1}*b_{1})$$

for exterior columns:
$$ QU = w_{u}(\frac{L_{1}*L_{2}}{2} - a_{1}*b_{1})$$

for corner columns:
$$ QU = w_{u}(\frac{L_{1}*L_{2}}{4} - a_{1}*b_{1})$$


where:
$$ w_{u} = 1.4(2.5T_{s} + F_{c} + wall load) + (1.6 * live load) $$
$$ a_{1} = a+depth $$
$$ b_{1} = b+depth $$


### $\beta_{o}$ equation:
$$ B_{o} = 2a_{1} + 2b_{1}$$

### depth equation:
$$ depth = T_{s} - 0.003$$

## Inputs to get from user:

 - $ a,b, T_{s}$: Dimensions of the column

 - $f_{cu}$: Compressive Strength

 - wall load
 - live load
 - $L_{1}, L_{2} $
 - $F_{c}$
 - Type of column: (interior, exterior, corner)
