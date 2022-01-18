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
    parser.add_argument("-p", "--planes",
                        required=False,
                        type=str,
                        default="",
                        help="Landmark points file"
                        )

    parser.add_argument("-f", "--fried_points",
                        required=False,
                        type=str,
                        default="",
                        help="Landmark points file (freidman)"
                        )

    parser.add_argument("-t", "--vault_points",
                        required=False,
                        type=str,
                        default="",
                        help="Landmark points file (vault)"
                        )

    parser.add_argument("-cf", "--corr_fried",
                        required=False,
                        type=str,
                        default="",
                        help="Landmark points file (corrected friedman)"
                        )

    parser.add_argument("-o", "--output",
                        required=False,
                        type=str,
                        default="",
                        help="Write the fitted plane or lines to a file"
                        )

    parser.add_argument("-v", "--visualise",
                        required=False,
                        default=False,
                        action='store_true',
                        help="Visualise the results"
                        )

    parser.add_argument("-c", "--config",
                        required=False,
                        type=str,
                        default=None,
                        help="A configuration file"
                        )


    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='glenoidplanefitting version ' + friendly_version_string)

    args = parser.parse_args(args)

    run_demo(args.model, args.planes, args.fried_points,
             args.vault_points,args.corr_fried, args.output,
             args.visualise, args.config)
