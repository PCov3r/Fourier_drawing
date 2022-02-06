from cmath import *


# Compute complex Fourier serie coefficient from points affixes
# z : list of points
# Ncoeff : order of the Fourier serie
# Tau: Period of the transformation
def computeCoeff(z, Ncoeff, Tau= 2*pi):
    N = len(z)
    h = Ncoeff // 2
    # Dict that contains the coeff
    coeff = {}

    for n in range(-h, h + 1):
        # Compute each coefficient
        cn = 0
        for k in range(N):
            cn += z[k] * exp(-1j * n * (k / N) * Tau)
        cn = cn/N
        # Add c[n] to dict
        coeff[n] = complex(cn)
    return coeff
