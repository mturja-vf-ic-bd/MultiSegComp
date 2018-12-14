# find center of mass in vtk
import vtk
import sys

def centerCOM(polydata):
    # Get Center of Mass
    centerFilter = vtk.vtkCenterOfMass()
    centerFilter.SetInputData(polydata)
    centerFilter.SetUseScalarsAsWeights(False)
    centerFilter.Update()
    center = centerFilter.GetCenter()
    print(center)

    # Change Center to (0, 0, 0)
    transform = vtk.vtkTransform()
    transform.Translate(-center[0], -center[1], -center[2])
    transformFilter = vtk.vtkTransformPolyDataFilter()
    transformFilter.SetInputData(polydata)
    transformFilter.SetTransform(transform)
    transformFilter.Update()
    centeredPolydata = transformFilter.GetOutput()
    return centeredPolydata

if __name__ == "__main__":
    filepath = sys.argv[1]
    output = sys.argv[2]
    reader = vtk.vtkGenericDataObjectReader()
    reader.SetFileName(filepath)
    reader.Update()
    polydata = reader.GetOutput()
    centeredPolydata = centerCOM(polydata)

    # write file
    writer = vtk.vtkPLYWriter()
    writer.SetInputData(centeredPolydata)
    writer.SetFileName(output)
    writer.Write()

