import numpy as np

labels=[]
rel_path = './../data/shen_268_parcellation_networklabels.csv'
labels.append(np.loadtxt(rel_path, delimiter=','))

#def network 1
network1=[]
network2=[]
network3=[]
network4=[]
network5=[]
network6=[]
network7=[]
network8=[]


for i in range (0,len(labels[0])):
    if labels[0][i][1]==1:
        network1.append(labels[0][i][0])
    elif labels[0][i][1]==2:
        network2.append(labels[0][i][0])
    elif labels[0][i][1]==3:
        network3.append(labels[0][i][0])
    elif labels[0][i][1]==4:
        network4.append(labels[0][i][0])
    elif labels[0][i][1]==5:
        network5.append(labels[0][i][0])
    elif labels[0][i][1]==6:
        network6.append(labels[0][i][0])
    elif labels[0][i][1]==7:
        network7.append(labels[0][i][0])
    elif labels[0][i][1]==8:
        network8.append(labels[0][i][0])

n_nodes=[len(network1),len(network2),len(network3),len(network4),len(network5),len(network6),len(network7),len(network8)]
