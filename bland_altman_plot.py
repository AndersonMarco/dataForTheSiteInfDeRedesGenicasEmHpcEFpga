import matplotlib.pyplot as plt
import numpy as np
import sys
import csv

def openCSVDataFromFileToANumpyMatrix(fileStr):
    fp=open(fileStr, 'r')
    data=list(csv.reader(fp))
    all_data = [np.zeros(len(data)-1) for i in range(len(data[0]))]
    for i in range(1,len(data)):
        for j in range(len(data[0])):
            all_data[j][i-1]=data[i][j]


    return all_data

def bland_altman_plot(data1, data2, *args, **kwargs):
    data1     = np.asarray(data1)
    data2     = np.asarray(data2)
    mean      = np.mean([data1, data2], axis=0)
    diff      = data1 - data2              # Difference between data1 and data2
    md        = np.mean(diff)                   # Mean of the difference
    sd        = np.std(diff, axis=0)            # Standard deviation of the difference

    plt.scatter(mean, diff, *args, **kwargs)
    plt.axhline(md,           color='gray', linestyle='--')
    plt.axhline(md + 1.96*sd, color='gray', linestyle='--')
    plt.axhline(md - 1.96*sd, color='gray', linestyle='--')


data=openCSVDataFromFileToANumpyMatrix(sys.argv[1])





labelsForThePlots=["Implementação CUDA rodando na Titan XP", "Implementação OpenCL rodando na R9 Nano","Implementação OpenCL rodando na Titan XP","Implementação para FPGA", "Implementação OpenCL rodando nos núcleos x86 do AMD A10"]
for i in range(5):
    for j in range(i+1,5):

        #plt.text(0.5, -0.1, labelsForThePlots[i]+"\nX\n"+labelsForThePlots[j], horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        plt.title(labelsForThePlots[i]+" versus\n"+labelsForThePlots[j],  fontsize=14)
        #ax.set_xlabel(labelsForThePlots[i]+"\nX\n"+labelsForThePlots[j], fontsize=14)
        bland_altman_plot(data[i], data[j])
        plt.savefig("Impl"+str(i)+str(j)+".svg")
        plt.close()

