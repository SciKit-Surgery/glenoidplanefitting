"""
This is an implentation of Friedman's method, see

Friedman RJ, Hawthorne KB and Genez BM.
`The use of computerized tomography in the measurement
of glenoid version. <https://pubmed.ncbi.nlm.nih.gov/1522089/>`_
J Bone and Joint Surg Am 1992; 74: 1032–7.

"""

import math
import numpy as np

def create_friedman_line(point0,point1):

    """
    Determines the second point needed to form the Friedman line

    :param point0: First point on glenoid line, anatomically defined as a
        point on the anterior margin of glenoid
    :param point1: Second point on glenoid line anatomically defined as a
        point on the posterior margin of glenoid

    :raises: Value Error if the z values of point0 and point1 are not equal

    :returns: The midpoint of the glenoid line, which is the second point of
        the Friedman line
    """

    if point0[2] != point1[2]:
        raise ValueError("For Friedman method points must have equal z values")

    midpoint_x = (point0[0] + point1[0])/2
    midpoint_y = (point0[1] + point1[1])/2
    midpoint = [midpoint_x, midpoint_y,point0[2]]
    return midpoint

def friedman_version(glenoid0,friedman1,friedman0):

    """
    Determines the glenoid version using the Friedman line

    :param glenoid0: First point on glenoid line, anatomically defined as a
        point on the anterior margin of the glenoid
    :param friedman1: Second point on the Friedman line, anatomically defined
        as the midpoint of the glenoid fossa
    :param friedman0: First point on the Friedman line, anatomically defined
        as the medial tip of the scapula

    :returns: The glenoid version (positive value indicates retroversion)

    """

    glenoid0_arr = np.array(glenoid0)
    friedman1_arr = np.array(friedman1)
    friedman0_arr = np.array(friedman0)

    glen_f1 = glenoid0_arr - friedman1_arr
    f0_f1 = friedman0_arr - friedman1_arr

    cosine_angle = np.dot(glen_f1, f0_f1) / (np.linalg.norm(glen_f1) *
            np.linalg.norm(f0_f1))
    radians = np.arccos(cosine_angle)
    version = (math.degrees(radians))-90

    return version
