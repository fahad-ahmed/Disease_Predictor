import os

from Sources.MachineLearningAlgorithm import MachineLearningAlgorithm
from Sources.Process_CTD_chem_gene import Process_CTD_chem_gene


def main():
    pass
    #print("Hello World!")

if __name__ == "__main__":
    main()

dataprocessingObject = Process_CTD_chem_gene()
file_exists = os.path.exists('../Dataset/ProcessedData/CTD_chemicals_diseases_Processed.csv')
if (file_exists == False):
    dataprocessingObject.DownloadProcessedDataset()

#dataprocessingObject.PreprocessRawData()

# file_exists = os.path.exists('../Dataset/RawData/ctdbase_chemical_gene_interaction/CTD_chemicals_diseases.csv')
# if (file_exists == False):
#     dataprocessingObject.DownloadRawDataset()
#


MachineLearningAlgorithmObject = MachineLearningAlgorithm()
MachineLearningAlgorithmObject.KNeighborsClassifier()
MachineLearningAlgorithmObject.GaussianNB()

#MachineLearningAlgorithmObject.ApplyLinearLassoModel()



#dataprocessingObject.ProcessDataset()
#dataprocessingObject.SaveProcessedCSVFile()