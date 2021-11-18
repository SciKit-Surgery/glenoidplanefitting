# coding=utf-8

"""glenoid-plane-fitting tests"""

from glenoidplanefitting.ui.glenoidplanefitting_demo import run_demo

def test_fit_plane_demo():

    model_name = 'glenoid.vtp'
    output_name = 'out_temp.vtp'

    run_demo (model_file_name = model_name, 
              planes = 'landmark_points.fcsv',
              fried_points="", 
              vault_points="", 
              corr_fried="", 
              output = output_name,
              visualise = False)
