import numpy as np
import pygimli as pg
from .kernel import SolveGravMagHolstein


class MagneticsModelling(pg.frameworks.MeshModelling):
    """Magnetics modelling operator using Holstein (2007)."""

    def __init__(self, mesh, points, cmp, igrf, foot=None):
        """Setup forward operator.

        Parameters
        ----------
        mesh : pygimli:mesh
            tetrahedral or hexahedral mesh
        points : list|array of (x, y, z)
            measuring points
        cmp : list of str
            component of: gx, gy, gz, TFA, Bx, By, Bz, Bxy, Bxz, Byy, Byz, Bzz
        igrf : list|array of size 3 or 7
            international geomagnetic reference field, either
            [D, I, H, X, Y, Z, F] - declination, inclination, horizontal field,
                                   X/Y/Z components, total field OR
            [X, Y, Z] - X/Y/Z components
        """
        # check if components do not contain g!
        super().__init__(mesh=mesh)
        self.createRefinedForwardMesh(refine=False, pRefine=False)
        self.mesh_ = mesh
        self.sensorPositions = points
        self.components = cmp
        self.igrf = igrf
        self.footprint = foot
        self.kernel = SolveGravMagHolstein(self.mesh_,
                                           pnts=self.sensorPositions,
                                           cmp=self.components, igrf=self.igrf,
                                           foot=self.footprint)
        self.J = pg.matrix.BlockMatrix()
        self.Ki = []
        self.Ji = []
        for iC in range(self.kernel.shape[1]):
            self.Ki.append(np.squeeze(self.kernel[:, iC, :]))
            self.Ji.append(pg.matrix.NumpyMatrix(self.Ki[-1]))
            self.J.addMatrix(self.Ji[-1], iC*self.kernel.shape[0], 0)

        self.J.recalcMatrixSize()
        self.setJacobian(self.J)

    # better move the latter to
    # self.createKernel

    # def setMesh(self, mesh):
        # self.createKernel(mesh)

    def response(self, model):
        """Compute forward response."""
        return self.J.dot(model)

    def createJacobian(self, model):
        """Do nothing as this is a linear problem."""
        pass
