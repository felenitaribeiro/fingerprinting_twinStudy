import numpy as np
from scipy.stats import pearsonr


# Correlation matrix among the subjects
def corr(list_of_individuals_matrix, corr_matrix):
    for i in range(0, len(list_of_individuals_matrix)):
        corr_row = []
        for m in range(0, len(list_of_individuals_matrix)):
            corr_row.append(pearsonr(list_of_individuals_matrix[i].reshape(-1),
                                     list_of_individuals_matrix[m].reshape(
                                         -1))[0])
        corr_matrix[i] = corr_row
    # Null results of the diagonal when a databaseXitself
    np.fill_diagonal(corr_matrix, -1)


# Accuracy for individual prediction function
def accuracy(corr_matrices, list_subject_ID, list_subject_ID_2):
    ind_accuracies = []
    for i in range(0, len(corr_matrices)):
        acc = 0
        # print(i)
        for j in range(0, len(corr_matrices[0])):
            if list_subject_ID[np.argmax(corr_matrices[i][j])] == list_subject_ID_2[j]:
                acc = acc + 1.
                # print(acc)
        accuracy = (acc / len(corr_matrices[0])) * 100.
        ind_accuracies.append(accuracy)
    return ind_accuracies


# Accuracy for twin prediction function
# Monozygotic twin identifications
def accuracy_t_MZ(corr_matrices, list_subject_ID, list_of_twin):
    acc = 0
    identified_pair = []
    for i in range(0, len(corr_matrices)):
        identified_pair.append([int(list_subject_ID[i]), int(
            list_subject_ID[np.argmax(corr_matrices[i])])])
        if identified_pair[i] == list_of_twin[i]:
            acc = acc + 1.
    accuracy_t = (acc / len(corr_matrices)) * 100.
    return accuracy_t



# Dizygotic twin identification
def accuracy_t_DZ(corr_matrices, list_subject_ID, list_of_twin):
    acc = 0
    identified_pair = []
    for i in range(0, len(corr_matrices)):
        identified_pair.append([int(list_subject_ID[i + 246]), int(
            list_subject_ID[np.argmax(corr_matrices[i])])])
        if identified_pair[i] == list_of_twin[i]:
            acc = acc + 1.
    # print len(identified_pair)
    accuracy_t = (acc / len(corr_matrices)) * 100.
    return accuracy_t


# Network matrices
def network(network_name, list_of_individuals_matrix,
            list_of_individuals_network):
    network_name = np.asarray(network_name, dtype='int')
    for i in range(len(network_name)):
        network_name[i] = network_name[i] - 1
    list_of_individuals_matrix = np.asarray(list_of_individuals_matrix)
    for m in range(0, len(list_of_individuals_matrix)):
        rows = list_of_individuals_matrix[m][network_name, :]
        columns = rows[:, network_name]
        list_of_individuals_network.append(columns)

