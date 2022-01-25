# coding=utf-8

"""glenoid-plane-fitting tests"""
import math
import pytest
from glenoidplanefitting.ui.glenoidplanefitting_demo import run_demo

def test_fit_plane_demo():
    """
    Tests plane fitting demo for different methods and outputs
    """
    #version is set based on the name of the output so,
    #out_temp will result in no version being returned
    model_name = 'glenoid.vtp'
    output_name = 'out_temp.vtp'

    version = run_demo (model_file_name = model_name,
                        planes = 'landmark_points.fcsv',
                        fried_points="",
                        vault_points="",
                        corr_fried="",
                        output = output_name,
                        visualise = False)
    assert version is None

    #This next one should result in version based on the planes method
    output_name = 'planes.vtp'
    version = run_demo (model_file_name = model_name,
                        planes = 'landmark_points.fcsv',
                        fried_points="",
                        vault_points="",
                        corr_fried="",
                        output = output_name,
                        visualise = False)

    assert math.isclose(version, 7.35087724)

    #This next one should result in version based on the friedman method
    output_name = 'friedman.vtp'
    version = run_demo (model_file_name = model_name,
                        planes = '',
                        fried_points='landmark_friedman.fcsv',
                        vault_points="",
                        corr_fried="",
                        output = output_name,
                        visualise = False)

    assert math.isclose(version, 7.742736667)

    #This next one should result in version based on the vault method
    #the vault method uses the same landmark design
    output_name = 'vault.vtp'
    version = run_demo (model_file_name = model_name,
                        planes = '',
                        fried_points="",
                        vault_points='landmark_vault.fcsv',
                        corr_fried="",
                        output = output_name,
                        visualise = False)

    assert math.isclose(version, 15.34696463)

    #Corrected friedman method?
    output_name = 'friedman.vtp'
    with pytest.raises(NotImplementedError):
        version = run_demo (model_file_name = model_name,
                            planes = '',
                            fried_points='',
                            vault_points="",
                            corr_fried='landmark_friedman.fcsv',
                            output = output_name,
                            visualise = False)

    assert math.isclose(version, 7.742736667)
