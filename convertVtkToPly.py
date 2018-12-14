import os
import vtk
import argparse

def convertFile(filepath, outdir):
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    if os.path.isfile(filepath):
        basename = os.path.basename(filepath)
        print("Copying file:", basename)
        basename = os.path.splitext(basename)[0]
        outfile = os.path.join(outdir, basename+".ply")
        reader = vtk.vtkGenericDataObjectReader()
        reader.SetFileName(filepath)
        reader.Update()
        writer = vtk.vtkPLYWriter()
        writer.SetInputConnection(reader.GetOutputPort())
        writer.SetFileName(outfile)
        return writer.Write() == 1
    return False

def convertFiles(indir, outdir):
    files = os.listdir(indir)
    files = [ os.path.join(indir,f) for f in files if f.endswith('.vtk') ]
    ret = 0
    print("In:", indir)
    print("Out:", outdir)
    for f in files:
        ret += convertFile(f, outdir)
    print("Successfully converted %d out of %d files." % (ret, len(files)))

def run(args):
    convertFiles(args.indir, args.outdir)