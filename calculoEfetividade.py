import processarProjetos
from datetime import datetime, timedelta
from holidayList import *

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

    def setarNome(self):
        for i in range(len(processarProjetos.listaProjetos)):
            self.nome = processarProjetos.listaProjetos[i]

    def setarPrazos(self, dataFimIteracao):
        for



