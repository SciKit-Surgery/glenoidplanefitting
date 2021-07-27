import vtk
from glenoidplanefitting.algorithms.models import make_plane_model

def vis_widget(bone, planes):
    
    renderer = vtk.vtkRenderer()
    for plane in planes:
        planeSource = make_plane_model(plane[1], plane[2])

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(planeSource.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        renderer.AddActor(actor)
    
    bone.ambient = 1.0
    bone.diffuse = 1.0
    bone.specular = 1.0
    bone.actor.GetProperty().SetAmbient(1)
    bone.actor.GetProperty().SetDiffuse(1)
    bone.actor.GetProperty().SetSpecular(1)
    renderer.AddActor(bone.actor)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetWindowName("Arrow")
    renderWindow.AddRenderer(renderer)

    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderWindowInteractor.Start()

    renderWindow.Finalize()
    del renderWindowInteractor, renderWindow
