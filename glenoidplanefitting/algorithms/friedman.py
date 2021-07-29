

"""
This is an implentation of Friedman's method, see

Friedman RJ, Hawthorne KB and Genez BM.
The use of computerized tomography in the measurement
of glenoid version. J Bone and Joint Surg Am 1992; 74: 1032–7.

"""
import vtk
import numpy as np
import math


def createFriedmanLine(p1,p2,p3):

    midpoint_x = (p1[0] + p2[0])/2
    midpoint_y = (p1[1] + p2[1])/2
    pm = [midpoint_x, midpoint_y,-94.83]

    return pm

def FriedmanAngle(p1,pm,p3):

    a = np.array(p1)
    b = np.array(pm)
    c = np.array(p3)

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    radians = np.arccos(cosine_angle)
    math = vtk.vtkMath
    angle = math.DegreesFromRadians(radians)
    

    return angle
