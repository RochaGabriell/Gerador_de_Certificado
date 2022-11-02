from datetime import date

class Date:

    def __init__(self) -> None:

        self.date = []

    def pick_date(self) -> None:
        #Capturando data atual
        actual_date = date.today()
        #Listando ano, mês e dia atuais
        self.date = [actual_date.year, actual_date.month, actual_date.day]
    
    def date_convert(self) -> tuple:

        month = self.date[1]

        m_e = { '1':'Janeiro', 
                '2':'Fevereiro', 
                '3':'Março',
                '4':'Abril', 
                '5':'Maio', 
                '6':'Junho',
                '7':'Julho', 
                '8':'Agosto', 
                '9':'Setembro',
                '10':'Outubro', 
                '11':'Novembro', 
                '12':'Dezembro',
                }
        #Capturando mês por extenso
        month = m_e[str(month)]
        #Retornando tupla com o ano, mês por extenso e dia
        return self.date[0], month, self.date[2]