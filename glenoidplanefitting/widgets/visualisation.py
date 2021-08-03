import vtk
from glenoidplanefitting.algorithms.models import make_plane_model

def renderer_common(bone):
    """
    Initialises a vtk renderer and adds the bone model
    """

    renderer = vtk.vtkRenderer()

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

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetWindowName(window_name)
    renderWindow.AddRenderer(renderer)

    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderWindowInteractor.Start()

    renderWindow.Finalize()
    del renderWindowInteractor, renderWindow

def vis_planes(bone, planes):
    """
    Visualisation for plane fitting methods
    :param bone: The model surface model
    :param planes: a list of planes, as returned by the 
        plane fitting methods in algorithms.plane_fitting

    """
   
    renderer = renderer_common(bone)
    for plane in planes:
        planeSource = make_plane_model(plane[1], plane[2])

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(planeSource.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        renderer.AddActor(actor)
    
    render_window_common(renderer, "Fitted Planes")
  
def vis_fried(bone, planes):
    pass

def vis_vault(bone, planes):
    pass
