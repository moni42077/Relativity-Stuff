import sympy as sp


class Field:
    def __init__(self, metric=None):
        self.t, self.r, self.theta, self.phi, self.M = sp.symbols("t r theta phi M")

        if metric is None:
            self.g = self.schwarzschildMetric()
        self.christoffel = self.christoffelCalc()
        self.riemann = self.riemannCalc()
        self.ricci = self.ricciCalc()

    def schwarzschildMetric(self):
        """Uncharged Non-rotating black hole"""
        g_tt = -(1 - 2 * self.M / self.r)
        g_rr = 1 / (1 - 2 * self.M / self.r)
        g_theta_theta = self.r**2
        g_phi_phi = (self.r * sp.sin(self.theta)) ** 2

        return sp.Matrix(
            [
                [g_tt, 0, 0, 0],
                [0, g_rr, 0, 0],
                [0, 0, g_theta_theta, 0],
                [0, 0, 0, g_phi_phi],
            ]
        )

    def kerrMetric(self, j):
        """Uncharged Rotating black hole (boyer lindquist coord)"""
        a = j / self.M
        sigma = self.r**2 + a**2 * sp.cos(self.theta) ** 2
        delta = self.r**2 - 2 * self.M * self.r + a**2
        g_tt = -(1 - 2 * self.M * self.r / sigma)
        g_rr = sigma / delta
        g_theta_theta = (
            self.r**2 + a**2 + 2 * self.M * self.r * a**2 / sigma
        ) * sp.sin(self.theta) ** 2
        g_phi_phi = 4 * self.M * self.r * sp.sin(self.theta) ** 2 / sigma

        return sp.Matrix(
            [
                [g_tt, 0, 0, 0],
                [0, g_rr, 0, 0],
                [0, 0, g_theta_theta, 0],
                [0, 0, 0, g_phi_phi],
            ]
        )

    def reissnerNordstromMetric(self):
        """Charged Non-rotating black hole"""
        return 0

    def kerrNewmanMetric(self, j, q):
        """Charged Rotating black hole"""
        return 0

    def christoffelCalc(self):
        """Г^λ_μv = 1/2 * d^{λσ} * (d_μ * g_vσ+ d_v * g_σμ - d_σ * g_μv)
        from Sean Carroll's Spacetime and Geometry"""
        coords = [self.t, self.r, self.theta, self.phi]
        christoffel = sp.MutableDenseNDimArray.zeros(
            4, 4, 4
        )  # same as np.zeros((4,4,4))
        g_inv = self.g.inv()

        for lam in range(4):
            for mu in range(4):
                for nu in range(4):
                    sum_term = 0
                    for o in range(4):
                        sum_term += (
                            g_inv[lam, o]
                            * (
                                sp.diff(self.g[nu, o], coords[mu])
                                + sp.diff(self.g[o, mu], coords[nu])
                                - sp.diff(self.g[mu, nu], coords[o])
                            )
                            / 2
                        )
                    christoffel[lam, mu, nu] = sp.simplify(sum_term)

        return christoffel

    def showChristoffel(self):
        map_symb = {0: "t", 1: "r", 2: "θ", 3: "φ"}

        for lam in range(4):
            for mu in range(4):
                for nu in range(4):
                    if self.christoffel[lam, mu, nu] != 0:
                        print(
                            f"Γ^{map_symb[lam]}_{map_symb[mu]}{map_symb[nu]} = ",
                            self.christoffel[lam, mu, nu],
                        )

    def riemannCalc(self):
        """R^ρ_σμv = d_μ * Г^ρ_vσ - d_v * Г^ρ_μσ +  Г^ρ_μλ * Г^λ_vσ - Г^ρ_vλ * Г^λ_μσ
        from Sean Carroll's Spacetime and Geometry"""
        coords = [self.t, self.r, self.theta, self.phi]
        riemann = sp.MutableDenseNDimArray.zeros(4, 4, 4, 4)

        for rho in range(4):
            for o in range(4):
                for mu in range(4):
                    for nu in range(4):
                        sum_term = 0
                        for lam in range(4):
                            sum_term += (
                                self.christoffel[rho, mu, lam]
                                * self.christoffel[lam, nu, o]
                                - self.christoffel[rho, nu, lam]
                                * self.christoffel[lam, mu, o]
                            )
                        riemann[rho, o, mu, nu] = sp.simplify(
                            sp.diff(self.christoffel[rho, nu, o], coords[mu])
                            - sp.diff(self.christoffel[rho, mu, o], coords[nu])
                            + sum_term
                        )

        return riemann

    def showRiemann(self):
        map_symb = {0: "t", 1: "r", 2: "θ", 3: "φ"}

        for rho in range(4):
            for o in range(4):
                for mu in range(4):
                    for nu in range(4):
                        if self.riemann[rho, o, mu, nu] != 0:
                            print(
                                f"R^{map_symb[rho]}_{map_symb[o]}{map_symb[mu]}{map_symb[nu]} = ",
                                self.riemann[rho, o, mu, nu],
                            )

    def ricciCalc(self):
        """R_μv = R^λ_μλv"""
        ricci = sp.MutableDenseNDimArray.zeros(4, 4)

        for mu in range(4):
            for nu in range(4):
                ricci[mu, nu] = sum(
                    [self.riemann[lam, mu, lam, nu] for lam in range(4)]
                )
        return ricci

    def showRicci(self):
        map_symb = {0: "t", 1: "r", 2: "θ", 3: "φ"}

        for mu in range(4):
            for nu in range(4):
                if self.ricci[mu, nu] != 0:
                    print(f"R_{map_symb[mu]}{map_symb[nu]} = ", self.ricci[mu, nu])
