import csv

class DataManager():

    def __init__(self, file: str) -> None:
        super().__init__()
        self.file = file
    def get_data(self):
        data_list = []
        #abrindo arquivo
        with open(self.file, "r+") as arch:
            #lendo arquivo
            reader = csv.reader(arch)
            for data in reader:
                #dicionarizando cada linha do arquivo
                mydict = {"nome": data[0],
                          "nome_curso": data[1],
                          "nome_coordenador": data[2],
                          "data_inicio": data[3],
                          "data_termino": data[4],
                          "carga_horaria": data[5],
                          "cpf": data[6]}

                data_list.append(mydict)

        return data_list