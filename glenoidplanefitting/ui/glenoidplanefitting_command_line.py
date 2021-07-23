# coding=utf-8

"""Command line processing"""


import argparse
from glenoidplanefitting import __version__
from glenoidplanefitting.ui.glenoidplanefitting_demo import run_demo


def main(args=None):
    """Entry point for glenoidplanefitting application"""

    parser = argparse.ArgumentParser(description='glenoidplanefitting')

    ## ADD POSITIONAL ARGUMENTS
    parser.add_argument("model",
                        type=str,
                        help="Filename for vtk surface model")

    
    # ADD OPTIONAL ARGUMENTS
    parser.add_argument("-i", "--points",
                        required=False,
                        type=str,
                        default="",
                        help="Landmark points file"
                        )

    # ADD OPTIONAL ARGUMENTS
    parser.add_argument("-o", "--output",
                        required=False,
                        type=str,
                        default="",
                        help="Write the fitted sphere to file"
                        )



    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='glenoidplanefitting version ' + friendly_version_string)

    args = parser.parse_args(args)

    run_demo(args.model, args.points, args.output)
