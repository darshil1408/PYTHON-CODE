import numpy as np
def system_coeffs():
    num = 0.5 * np.poly([0.7, 0.9])   # numerator coefficients
    den = np.poly([0.6, 0.4])         # denominator coefficients
    return num, den
def analyze_stability(num, den):
    zeros = np.roots(num) if len(num) > 0 else np.array([])
    poles = np.roots(den)
    print("Numerator coeffs:", np.round(num, 6))
    print("Denominator coeffs:", np.round(den, 6))
    print("Zeros:", np.round(zeros, 6))
    print("Poles:", np.round(poles, 6))
    mags = np.abs(poles)
    print("Pole magnitude: ", np.round(mags, 6))
    if np.all(mags < 1):
        print("Stability: Stable (all poles inside unit circle)")
    elif np.any(np.isclose(mags, 1, atol=1e-8)):
        print("Stability: Marginal (pole on unit circle) — not BIBO stable")
    else:
        print("Stability: Unstable (some poles outside unit circle)")
if __name__ == "__main__":
    num, den = system_coeffs()
    print("H(z) = 0.5*(z-0.7)*(z-0.9) / ((z-0.6)*(z-0.4))")
    analyze_stability(num, den)