from numpy import *
import glob

#paths to the data
refpath = ".\\simplifiedref\\"
patientpath = ".\\simplifiedpatient\\"

#load the reference data into numpy array
refchrom = loadtxt(refpath+"genchr",dtype=int)
refstarts = loadtxt(refpath+"gensta",dtype=int)
refends = loadtxt(refpath+"genend",dtype=int)
refname = loadtxt(refpath+"gennam",dtype=str)

#get the variant file names
varchrfiles = glob.glob(patientpath+"\\varchr*")
varfilfiles = glob.glob(patientpath+"\\varfil*")
varposfiles = glob.glob(patientpath+"\\varpos*")

vargene = []
varnum = []

##for genetype in range(len(varchrfiles)):
##
##    #pick and load variant files
##    varchrfile = varchrfiles[genetype]
##    varposfile = varposfiles[genetype]
##    varfilfile = varfilfiles[genetype]
##
##    varchr = loadtxt(varchrfile,dtype=int)
##    varpos = loadtxt(varposfile,dtype=int)
##    varfil = loadtxt(varfilfile,dtype=int)
##
##    #get a list of gene names that have variants
##    #for each variant, loop through the start and ends to 
##    #loop through all variants
##    for i in range(len(varpos)):
##        variant_position = varpos[i]
##        print(genetype,i,"./",len(varchr))
##        #loop through all genes
##        for j in range(len(refstarts)):
##            #if the variant position and chromosome lies within that gene positions and chromosome
##            if variant_position > refstarts[j] and variant_position < refends[j] and varchr[i] == refchrom[j]:
##                #then add that gene to the list
##                vargene.append(refname[j])

#pick and load variant files
varchrfile = varchrfiles[2]
varposfile = varposfiles[2]
varfilfile = varfilfiles[2]

varchr = loadtxt(varchrfile,dtype=int)
varpos = loadtxt(varposfile,dtype=int)
varfil = loadtxt(varfilfile,dtype=int)

#get a list of gene names that have variants
#for each variant, loop through the start and ends to 
#loop through all variants
for i in range(len(varpos)):
    variant_position = varpos[i]
    print(i,"./",len(varchr))
    #loop through all genes
    for j in range(len(refstarts)):
        #if the variant position and chromosome lies within that gene positions and chromosome
        if variant_position > refstarts[j] and variant_position < refends[j] and varchr[i] == refchrom[j]:
            #then add that gene to the list
            vargene.append(refname[j])
            
savetxt("vargene2.txt",vargene)
            
    
    
