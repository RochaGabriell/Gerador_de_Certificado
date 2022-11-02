import csv

class DataManager():
    def __init__(self, file: str) -> None:
        self.file = file

    def _cpf_format(self, cpf: str) -> str:
        if "." not in cpf and "-" not in cpf:
            slice_one = cpf[:3]
            slice_two = cpf[3:6]
            slice_three = cpf[6:9]
            slice_four = cpf[9:]
            return f"{slice_one}.{slice_two}.{slice_three}-{slice_four}"
        else:
            return cpf

    def get_data(self) -> list[dict]:
        data_list = []
        #abrindo arquivo
        with open(self.file, "r+") as arch:
            #lendo arquivo
            reader = csv.reader(arch)
            for data in reader:

                cpf = self._cpf_format(data[6]) # Tratar o cpf

                #dicionarizando cada linha do arquivo
                mydict = {"nome": data[0],
                          "nome_curso": data[1],
                          "nome_coordenador": data[2],
                          "data_inicio": data[3],
                          "data_termino": data[4],
                          "carga_horaria": data[5],
                          "cpf": cpf}

                data_list.append(mydict)
        return data_list