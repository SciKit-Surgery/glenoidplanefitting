

"""
This is an implentation of the vault method, see

Matsumura N et al.
Computed tomography measurement of glenoid vault version
as an alternative measuring method for glenoid version.
Journal of Orthopaedic Surgery and Research 2014, 9:17

"""
import vtk
import numpy as np
import math


def createVaultLine(p1,p2):

    """

    Determines the second point needed to form the Friedman line
    :param p1: First point on glenoid line, anatomically defined as a point on the anterior margin of glenoid
    :param p2: Second point on glenoid line anatomically defined as a point on the posterior margin of glenoid
    
    :returns: The midpoint of the glenoid line, or the second point of for the vault line
    
    """

    midpoint_x = (p1[0] + p2[0])/2
    midpoint_y = (p1[1] + p2[1])/2
    pm = [midpoint_x, midpoint_y,p1[2]]

    return pm

def VaultVersion(p1,pm,p3):

    """
    Determines the glenoid version using the glenoid vault as reference 
    :param p1: First point on glenoid line, anatomically defined as a point on the anterior margin of the glenoid
    :param pm: Second point on the vault line, anatomically defined as the midpoint of the glenoid fossa
    :param p3: First point on the vault line, anatomically defined as the tip of the glenoid vaultt

    :returns: The glenoid version (positive value indicates retroversion)

    """

    a = np.array(p1)
    b = np.array(pm)
    c = np.array(p3)

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    radians = np.arccos(cosine_angle)
    math = vtk.vtkMath
    version = (math.DegreesFromRadians(radians))-90
    

    return version
