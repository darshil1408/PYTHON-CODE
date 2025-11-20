import numpy as np
def z_transform_unit_step():
    num = [1, 0]   
    den = [1, -1]  
    roc = "|z| > 1"
    return num, den, roc
def analyze_stability(num, den):
    zeros = np.roots(num) if any(num) else np.array([])
    poles = np.roots(den)
    print("Zeros:", zeros)
    print("Poles:", poles)
    # BIBO stable if all poles are inside the unit circle
    inside = np.abs(poles) < 1
    if np.all(inside):
        print("Stability: Stable (all poles inside unit circle)")
    else:
        if np.any(np.isclose(np.abs(poles), 1)):
            print("Stability: Marginal / not BIBO stable (pole on unit circle)")
        else:
            print("Stability: Unstable (some poles outside unit circle)")
if __name__ == "__main__":
    num, den, roc = z_transform_unit_step()
    print("Z-transform: X(z) = z / (z - 1)")
    print("Region of Convergence:", roc)
    analyze_stability(num, den)
   