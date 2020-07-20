import numpydoc as np
import os


def split_file(path, pointsnum):
    " Load a file and split it into pieces of length pointsnum. Output will be in a new folder inside the file dir. Folder name same as file name. "
    with open(str(path)) as f:
        linenum=sum(1 for line in f) # Count lines in file

    f.close()

    bare_path, namestring = os.path.split(path) # This function returns two things

    #create list of file names
    names=[]
    for i in range(0, linenum/pointsnum):  # Range from 0 to (Number of new files)
        string= bare_path + '\\' + os.path.splitext(namestring)[0] + '\\' + os.path.splitext(namestring)[0] + '-' + str(i).zfill(4) + '.txt' # Directory/Filename/Filename-00i.txt 
        names.append(string) # Append the path to the list of paths 

    if not os.path.exists(string):
            os.makedirs(os.path.split(names[0])[0]) # /Filename/ Subfolder does not exist and needs to be created, generally. Remove filename from path before making dir
            
            
    f = open(str(path), 'r') # Open the file being split into pieces

    g= open(names[0],'w') # Open the first partial file for writing

    k=0 # Number of the current element in names[]
    i=0

    for line in f: # Iterate over lines in ffolder
        if i%pointsnum == 0 and i>0: # i%pointsnum is 0 only when i is n*pointsnum. 
            g.close() # Close current file as pointsnum worth of pts has been written
            k=k+1 # Increase the names[] element counter
            if k >= len(names): # if k happens to exceed len of names, stop the loop
                break
            g = open(names[k],'w') # If all is good, proceed to open names[k] for writing
            g.write(line)
            i=i+1
        else:
            g.write(line) # If pointsnum has not been reached yet for this particular file, write
            i=i+1

            
    g.close()
    f.close()



def chop_files(path, points):
    " Loads files from a directory and copies 'points' worth of each file into a new sub dir called 'Chopped' "
    filenames = sorted(os.listdir(path)) # List filenames
    newdir = path + '\\' + 'Chopped' # Path for new sub dir
    
    if not os.path.exists(newdir): # If new dir does not exist
        os.makedirs(newdir) # create newdir
        
    for i in range(1, len(filenames)):  # for each file
        Data_Temp = np.loadtxt(str(path) + '\\' + filenames[i]) # Load file
        New = open(newdir + '\\' + filenames[i],'w')  # Open new file in subdir
        for j in range(0, points): # Write 'points' worth of points
            string = str(Data_Temp[j,0]) + '\t' + str(Data_Temp[j,1]) + '\n'
            New.write(string)
        New.close()

    
def reduce_files(path, factor, lines_to_skip):
    " Reduce input files by factor. Ie. factor = 10 -> every tenth pt in output. "
    " Files are loaded from a dir, and output is in a subdir called Reduced "
    " Third arg is lines to skip at beginning of each file"
    " Before execution the folder should contain only the files to reduce "
    " For use on single column data! "


    filenames = sorted(os.listdir(path))
    
    newdir = path + '\\' + 'Reduced'
    
    if not os.path.exists(newdir):
        os.makedirs(newdir)

    for i in range(0,len(filenames)):
        with open(path + '\\' + os.path.split(filenames[i])[1],'r') as f:
            linenum=sum(1 for line in f)
        f.close()
        f=open(path + '\\' + os.path.split(filenames[i])[1],'r')
        g=open(newdir + '\\' + os.path.split(filenames[i])[1] ,'w')
        j=0
        for line in f:
            if j%factor == 0:
                g.write(line)
                j=j+1
            else:
                j=j+1
        g.close()
        f.close()


def get_filepaths(lib_path, eol, make):
    "Load a text file with paths to measurement files"
    "eol is either '\t' or '\n' depending on the library format"
    "If make = 1, fft folderpaths are made into actual filepaths"
    
    f=open(lib_path,'r')
    paths=[]
    for line in f:
        filepath=str()
        for i in line:
            if i != eol:
                filepath=filepath+i
            else:
                break
        paths.append(filepath)
    if make==1: #creates filepaths if fft folderpaths were given
        for i in range(0, len(paths)):
            paths[i]=paths[i]+ '\\Speed vs time\\'
            paths[i]=paths[i]+os.listdir(paths[i])[0]
    f.close()
    return paths
        
def get_filepaths_8192(lib_path, eol, make):
    "Load a text file with paths to measurement files"
    "eol is either '\t' or '\n' depending on the library format"
    "If make = 1, fft folderpaths are made into actual filepaths"
    
    f=open(lib_path,'r')
    paths=[]
    for line in f:
        filepath=str()
        for i in line:
            if i != eol:
                filepath=filepath+i
            else:
                break
        paths.append(filepath)
    if make==1: #creates filepaths if fft folderpaths were given
        for i in range(0, len(paths)):
            paths[i]=paths[i]+ '\\Speed vs time-8192\\'
            paths[i]=paths[i]+os.listdir(paths[i])[0]
    f.close()
    return paths
