# encoding: utf-8
"""
Mesh generation and modification.

.. note::

    Although we discriminate here between grids (structured meshes) and meshes
    (unstructured), both objects are treated the same internally.
"""

from ..core import createMesh1D, createMesh1DBlock, createMesh2D, createMesh3D
from .grid import appendTetrahedronBoundary, appendTriangleBoundary, createGrid

from .mesh import (createMesh, createParaMesh, createParaMesh2DGrid,
                   extrudeMesh, 
                   merge2Meshes, refineQuad2Tri, refineHex2Tet,
                   mergeMeshes, readGmsh, readHydrus2dMesh,
                   readHydrus3dMesh, readTetgen, readTriangle,
                   convertHDF5Mesh, readHDF5Mesh, readFenicsHDF5Mesh,
                   exportHDF5Mesh, exportFenicsHDF5Mesh,
                   readSTL, exportSTL,
                   )

from .polytools import createParaDomain2D  # keep for backward compatibility
from .polytools import (createCircle, createLine, createParaMeshPLC,
                        createPolygon, createRectangle, createWorld, 
                        mergePLC, mergePLC3D,
                        createCylinder, createCube,
                        readPLC, exportPLC, writePLC, syscallTetgen)
from .quality import (quality)

from .mapping import (nodeDataToCellData,
                      cellDataToNodeData,
                      nodeDataToBoundaryData,
                      cellDataToBoundaryData,
                      fillEmptyToCellArray,
                      tapeMeasureToCoordinates,
                      interpolate,
                      interpolateAlongCurve
                      )

#  This is neither functional nor good practice  #  why?
#  __all__ = [name for name in dir() if '_' not in name]

__all__ = ['appendTriangleBoundary',
           'appendTetrahedronBoundary',
           'createMesh',
           'readGmsh',
           'readTriangle',
           'readTetgen',
           'readHydrus2dMesh',
           'readHydrus3dMesh',
           'readHDF5Mesh',
           'readFenicsHDF5Mesh',
           'readSTL',
           'refineQuad2Tri',
           'mergeMeshes',
           'merge2Meshes',
           'createParaMesh',
           'createParaMesh2DGrid',
           'createPolygon',
           'createRectangle',
           'createWorld',
           'createCircle',
           'createLine',
           'createParaMeshPLC',
           'convertHDF5Mesh',
           'exportHDF5Mesh',
           'exportFenicsHDF5Mesh',
           'mergePLC',
           'readPLC',
           'writePLC',
           'exportPLC',
           'createParaDomain2D',  # keep for backward compatibility
           'quality'
           ]
