from datetime import datetime

class DateGenerator:
    def __init__(self) -> None:
        self.current_date = []

    def pick_date(self) -> None:
        #Capturando data atual
        date = datetime.today()
        year, month, day = date.year, date.month, date.day
        self.current_date = list(map(str, [day, month, year]))

    def date_convert(self) -> None:
        #Convertendo data para string
        month = self.current_date[1]
        m_e = { '1':'Janeiro', '2':'Fevereiro', '3':'Março',
                '4':'Abril', '5':'Maio', '6':'Junho',
                '7':'Julho', '8':'Agosto', '9':'Setembro',
                '10':'Outubro', '11':'Novembro', '12':'Dezembro',
                }
        #Capturando mês por extenso
        month = m_e[str(month)]
        self.current_date[1] = month

    def get_date(self) -> list:
        return self.current_date

if __name__ == '__main__':
    date = DateGenerator()
    date.pick_date()
    date.date_convert()
    print(date.get_date())