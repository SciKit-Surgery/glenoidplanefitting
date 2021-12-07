"""
Widgets for show the results of plane fitting.
"""
import vtk
from glenoidplanefitting.algorithms.models import make_plane_model, \
        make_friedman_model, make_vault_model

def renderer_common(bone):
    """
    Initialises a vtk renderer and adds the bone model
    """

    renderer = vtk.vtkRenderer() #pylint:disable=no-member

    bone.ambient = 1.0
    bone.diffuse = 1.0
    bone.specular = 1.0
    bone.actor.GetProperty().SetAmbient(1)
    bone.actor.GetProperty().SetDiffuse(1)
    bone.actor.GetProperty().SetSpecular(1)
    renderer.AddActor(bone.actor)

    return renderer

def render_window_common(renderer, window_name):
    """
    Creates and starts a render window and interactor.
    :param renderer: A vtk renderer to add to the render window
    :param window_name: A name for the window
    """

    render_window = vtk.vtkRenderWindow() #pylint:disable=no-member
    render_window.SetWindowName(window_name)
    render_window.AddRenderer(renderer)

    render_window_interactor = vtk.vtkRenderWindowInteractor() #pylint:disable=no-member
    render_window_interactor.SetRenderWindow(render_window)
    render_window_interactor.Start()

    render_window.Finalize()
    del render_window_interactor, render_window

def add_vtk_source(renderer, source):
    """
    simplifies adding a vtk geometry source to a renderer
    :params renderer: a vtk renderer to add to
    :params source: a vtk geometry source
    """
    mapper = vtk.vtkPolyDataMapper() #pylint:disable=no-member
    mapper.SetInputConnection(source.GetOutputPort())
    actor = vtk.vtkActor() #pylint:disable=no-member
    actor.SetMapper(mapper)
    renderer.AddActor(actor)

def vis_planes(bone, planes):
    """
    Visualisation for plane fitting methods
    :param bone: The model surface model
    :param planes: a list of planes, as returned by the
        plane fitting methods in algorithms.plane_fitting

    """
    renderer = renderer_common(bone)
    for plane in planes:
        plane_source = make_plane_model(plane[1], plane[2])
        add_vtk_source(renderer, plane_source)

    render_window_common(renderer, "Fitted Planes")

def vis_fried(bone, cross1, cross2, glenoid1, result):
    """
    Visualise the lines resulting from the friedman
    method.
    :params cross1, cross2: The end points of the line crossing the glenoid
    :params glenoid1, result: The end points of the line defining the glenoid
        version
    """
    renderer = renderer_common(bone)

    glenoid_line = make_friedman_model(cross1,cross2)
    add_vtk_source(renderer, glenoid_line)

    friedman_line = make_friedman_model(glenoid1,result)
    add_vtk_source(renderer, friedman_line)

    render_window_common(renderer, "Friedman Lines")


def vis_vault(bone, cross1, cross2, glenoid1, result):
    """
    Visualise the lines resulting from the vault
    method.
    :params cross1, cross2: The end points of the line crossing the glenoid
    :params glenoid1, result: The end points of the line defining the glenoid
        version
    """
    renderer = renderer_common(bone)

    glenoid_line = make_vault_model(cross1,cross2)
    add_vtk_source(renderer, glenoid_line)

    vault_line = make_vault_model(glenoid1, result)
    add_vtk_source(renderer, vault_line)

    render_window_common(renderer, "Vault Lines")
