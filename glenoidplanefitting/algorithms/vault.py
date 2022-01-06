

"""
This is an implentation of the vault method, see

Matsumura N et al.
`Computed tomography measurement of glenoid vault version
as an alternative measuring method for glenoid version.
<https://doi.org/10.1186/1749-799x-9-17>`_
Journal of Orthopaedic Surgery and Research 2014, 9:17

"""
import math
import numpy as np


def create_vault_line(anterior_point,posterior_point):
    """
    Determines the second point needed to form the Friedman line
    :param anterior_point: First point on glenoid line, anatomically defined
        as a point on the anterior margin of glenoid
    :param posterior_point: Second point on glenoid line anatomically defined
        as a point on the posterior margin of glenoid
    :returns: The midpoint of the glenoid line, or the second point of
        for the vault line
    """

    midpoint_x = (anterior_point[0] + posterior_point[0])/2
    midpoint_y = (anterior_point[1] + posterior_point[1])/2
    midpoint = [midpoint_x, midpoint_y,anterior_point[2]]

    return midpoint

def vault_version(anterior_point,midpoint,vaultpoint):
    """
    Determines the glenoid version using the glenoid vault as reference
    :param anterior_point: First point on glenoid line, anatomically defined
        as a point on the anterior margin of the glenoid
    :param midpoint: Second point on the vault line, anatomically defined as
        the midpoint of the glenoid fossa
    :param vaultpoint: First point on the vault line, anatomically defined as
        the tip of the glenoid vault

    :returns: The glenoid version (positive value indicates retroversion)
    """

    ant_p_arr = np.array(anterior_point)
    mid_p_arr = np.array(midpoint)
    vlt_p_arr = np.array(vaultpoint)

    ant_mid = ant_p_arr - mid_p_arr
    vlt_mid = vlt_p_arr - mid_p_arr

    cosine_angle = np.dot(ant_mid, vlt_mid) / (np.linalg.norm(ant_mid) *
                                               np.linalg.norm(vlt_mid))
    radians = np.arccos(cosine_angle)
    version = math.degrees(radians) - 90

    return version
