# coding=utf-8

"""glenoid-plane-fitting tests"""

from glenoidplanefitting.ui.glenoidplanefitting_demo import run_demo

def test_fit_plane_demo():

    model_name = 'glenoid.vtp'
    output_name = 'out_temp.vtp'

   run_demo (model_name, output_name)
