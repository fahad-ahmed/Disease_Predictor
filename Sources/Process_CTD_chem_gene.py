import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
import gdown

class Process_CTD_chem_gene:
    df = pd.DataFrame()

    def DownloadRawDataset(self):
        print("Start: Downloading Raw Dataset")
        url = 'https://drive.google.com/uc?id=1zZhsUTPHjgXcor3d-lg59Ul7kVK6sqE3'
        output = '../Dataset/RawData/ctdbase_chemical_gene_interaction/CTD_chemicals_diseases.csv'
        gdown.download(url, output, quiet=False)
        print("Start: Download Completed")

    def DownloadProcessedDataset(self):
        print("Start: Downloading ProcessedDataset")
        url = 'https://drive.google.com/uc?id=1ESmif_fyoPHd2FeGTgFtD-XG2TioArhJ'
        output = '../Dataset/ProcessedData/CTD_chemicals_diseases_Processed.csv'
        gdown.download(url, output, quiet=False)
        print("Start: Download Completed")


    def LoadDataFromCSVFile(self):
        print("Start: LoadDataFromFile")
        self.df = pd.read_csv("../Dataset/RawData/ctdbase_chemical_gene_interaction/CTD_chemicals_diseases.csv", nrows=1000000)
        print("end: LoadDataFromFile")

    def ProcessDataset(self):
        print("Start: ProcessDataset")

        self.df.pop('ChemicalName')
        self.df.pop('CasRN')
        self.df.pop('DiseaseName')
        #self.df.pop('DiseaseID')
        self.df.pop('DirectEvidence')
        self.df.pop('OmimIDs')
        self.df.pop('PubMedIDs')

        enc = OrdinalEncoder()
        self.df = self.df.astype({"InferenceGeneSymbol": str})
        enc.fit(self.df[["InferenceGeneSymbol"]])
        self.df[["InferenceGeneSymbol"]] = enc.transform(self.df[["InferenceGeneSymbol"]])

        self.df = self.df.astype({"DiseaseID": str})
        enc.fit(self.df[["DiseaseID"]])
        self.df[["DiseaseID"]] = enc.transform(self.df[["DiseaseID"]])

        self.df = self.df.astype({"ChemicalID": str})
        enc.fit(self.df[["ChemicalID"]])
        self.df[["ChemicalID"]] = enc.transform(self.df[["ChemicalID"]])

        self.df = self.df.apply(pd.to_numeric, errors='coerce')
        self.df = self.df.dropna()

        print("end: ProcessDataset")

    def SaveProcessedCSVFile(self):
        print("Start: SaveProcessedFile")
        self.df.to_csv('../Dataset/ProcessedData/CTD_chemicals_diseases_Processed.csv', index=False)
        print("end: SaveProcessedFile")

    def GetClusteringOutput(self):
        print('Hello Harry')

    def LoadProcessedFile(self):
        print("Start: LoadProcessedFile")
        self.df = pd.read_excel('../Dataset/ProcessedData/CTD_chemicals_diseases_Processed.xlsx')
        print("end: LoadProcessedFile")


    def PreprocessRawData(self):
        print("Start: PreprocessRawData")
        self.LoadDataFromCSVFile()
        self.ProcessDataset()
        self.SaveProcessedCSVFile()
        print("end: PreprocessRawData")
