

"""
This is an implentation of Friedman's method, see

Friedman RJ, Hawthorne KB and Genez BM.
The use of computerized tomography in the measurement
of glenoid version. J Bone and Joint Surg Am 1992; 74: 1032–7.

"""
import vtk
import numpy as np
import math


def createFriedmanLine(p1,p2):

    """
    Determines the second point needed to form the Friedman line
    :param p1: First point on glenoid line, anatomically defined as a point on the anterior margin of glenoid
    :param p2: Second point on glenoid line anatomically defined as a point on the posterior margin of glenoid
    
    :returns: The midpoint of the glenoid line, or the second point of for the Friedman line
    """

    midpoint_x = (p1[0] + p2[0])/2
    midpoint_y = (p1[1] + p2[1])/2
    pm = [midpoint_x, midpoint_y,p1[2]]

    return pm

def FriedmanVersion(p1,pm,p3):

    """
    Determines the glenoid version using the Friedman line
    :param p1: First point on glenoid line, anatomically defined as a point on the anterior margin of the glenoid
    :param pm: Second point on the Friedman line, anatomically defined as the midpoint of the glenoid fossa
    :param p3: First point on the Friedman line, anatomically defined as the medial tip of the scapula

    :returns: The glenoid version 

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
