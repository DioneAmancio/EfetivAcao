import processarProjetos
import getIssues
from datetime import datetime, timedelta
from DatasEPrazos import *

EfetividadeProjetos = []

class projeto:
    def __init__(self, nome, prazoSubmissaoRDP, dataSubmissaoRDP, eficienciaSubmissaoRDP, eficaciaSubmissaoRDP,
                 prazoRevisaoRDP, dataRevisaoRDP, eficienciaRevisaoRDP, eficaciaRevisaoRDP, prazoRAG, dataRAG,
                 eficienciaRAG, eficaciaRAG, prazoSubmissaoBHP, dataSubmissaoBHP, eficienciaSubmissaoBHP, eficaciaSubmissaoBHP):

        self.nome = nome
        self.prazoSubmissaoRDP = prazoSubmissaoRDP
        self.dataSubmissaoRDP = dataSubmissaoRDP
        self.eficienciaSubmissaoRDP = eficienciaSubmissaoRDP
        self.eficaciaSubmissaoRDP = eficaciaSubmissaoRDP
        self.prazoRevisaoRDP = prazoRevisaoRDP
        self.dataRevisaoRDP = dataRevisaoRDP
        self.eficienciaRevisaoRDP = eficienciaRevisaoRDP
        self.eficaciaRevisaoRDP = eficaciaRevisaoRDP
        self.prazoRAG = prazoRAG
        self.dataRAG = dataRAG
        self.eficienciaRAG = eficienciaRAG
        self.eficaciaRAG = eficaciaRAG
        self.prazoSubmissaoBHP = prazoSubmissaoBHP
        self.dataSubmissaoBHP = dataSubmissaoBHP
        self.eficienciaSubmissaoBHP = eficienciaSubmissaoBHP
        self.eficaciaSubmissaoBHP = eficaciaSubmissaoBHP

    def setarNome(self, i):
            self.nome = processarProjetos.listaProjetos[i]

    def setarPrazos (self, dataFimIteracao):
        #Calculando data para a submissão do RDP
        self.prazoSubmissaoRDP = calcularPrazos(dataFimIteracao, 7)

        #Calculando data para a revisão do RDP
        self.prazoRevisaoRDP = calcularPrazos(self.prazoSubmissaoRDP, 5)

        # Calculando data para a realizar RAG
        self.prazoRAG = calcularPrazos(self.prazoRevisaoRDP, 5)

        # Calculando data para a submissão da BHP
        self.prazoSubmissaoBHP = calcularPrazos(self.prazoRAG, 5)

    def setarDataSubmissaoRDP :
        IdIssue = getIssues.buscarIssueRDP()





