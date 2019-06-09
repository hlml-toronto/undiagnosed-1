#import a bunch of stuff
from numpy import *
import vcf
import glob
import os
def simplify_patient():
    #get a list of patient data file names
    os.chdir(".\\patientdata")
    filenames = os.listdir(".")
    os.chdir("..")

    #get path to all the patient data files
    patientfiles = glob.glob(".\\patientdata\\*")

    #loops over all the patient variant data files
    for genetype in range(len(patientfiles)):
        #set the current patient variant file type
        patientdatafile = patientfiles[genetype]

        #create lists to hold positions, ch
        variant_positions = []
        variant_chromosomes=[]
        variant_filter = []

        #open the vcf file in vcf reader
        vcf_reader = vcf.Reader(open(patientdatafile,'r'))

        #go through the whole file and record the variant positions, chromosomes and filter in different lists
        while True:
            try:
                record = next(vcf_reader)
                variant_positions.append(record.POS)
                variant_chromosomes.append(record.CHROM)
                variant_filter.append(record.FILTER)
            except:
                break

        #sav the simplified data in different files
        f1=open(".\\simplifiedpatient\\varpos_"+filenames[genetype],"w")
        f2=open(".\\simplifiedpatient\\varchr_"+filenames[genetype],"w")
        f3=open(".\\simplifiedpatient\\varfil_"+filenames[genetype],"w")

        for i in range(len(variant_positions)):
            f1.write(str(variant_positions[i])+"\n")
            if variant_chromosomes[i] == "X":
                f2.write("23\n")
            elif variant_chromosomes[i] == "Y":
                f2.write("24\n")
            else:
                f2.write(str(variant_chromosomes[i])+"\n")
                
            if str(variant_filter[i]) == "[]":
                f3.write("0\n")
            else:
                f3.write("1\n")
        f1.close()
        f2.close()
        f3.close()

        print("File " + str(genetype) + "complete")


def simplify_ref():
    from gtfparse import read_gtf
    #read in the data
    refdatafile = "./ref/gencode.v18.annotation.gtf"
    df = read_gtf(refdatafile)

    #open a file for chromosome #
    f1=open(".\\simplifiedref\\genchr","w")
    #open a file for start pos
    f2=open(".\\simplifiedref\\gensta","w")
    #open a file for end pos
    f3=open(".\\simplifiedref\\genend","w")
    #open a file for gene name
    f4=open(".\\simplifiedref\\gennam","w")

    for i in range(len(df.start)):
        if i%100000 == 0:
            print(i/len(df.start))
        #write to chromosome file
        if str(df.seqname[i])[3] == 'M':
            f1.write("25\n")
        elif str(df.seqname[i])[3:] == 'MT':
            f1.write("26\n")
        elif str(df.seqname[i])[3] == 'X':
            f1.write("23\n")
        elif str(df.seqname[i])[3] == 'Y':
            f1.write("24\n")
        else:
            f1.write(str(df.seqname[i])[3]+"\n")
        #write to start position file
        f2.write(str(df.start[i])+"\n")
        #end file
        f3.write(str(df.end[i])+"\n")
        #gene name
        f4.write(str(df.gene_name[i])+"\n")

    f1.close()
    f2.close()
    f3.close()
    f4.close()

simplify_patient()
#simplify_ref()


