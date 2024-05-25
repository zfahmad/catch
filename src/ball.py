class Ball:
    def __init__(self, radius=1.0, mass=1.0, elasticity=1.0):
        self._radius = radius
        self._mass = mass
        self._elasticity = elasticity

    @property
    def radius(self):
        return self._radius

    @property
    def mass(self):
        return self._mass

    @property
    def elasticity(self):
        return self._elasticity
