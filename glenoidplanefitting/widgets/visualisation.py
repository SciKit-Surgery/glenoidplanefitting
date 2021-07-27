import vtk

def vis_widget():
    arrowSource = vtk.vtkArrowSource()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(arrowSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetWindowName("Arrow")
    renderWindow.AddRenderer(renderer)

    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderWindowInteractor.Start()

    renderWindow.Finalize()
    del renderWindowInteractor, renderWindow
