#Importando bibliotecas e metodos necessários
from DataManager import DataManager
from DateGenerator import Date
from StyleGenerator import Style

from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from pdf2image import convert_from_path


class CertificateGenerator():

    def __init__(self, img: str, file: str) -> None:
        super().__init__()
        self.img = img
        self.file = DataManager(file).get_data() #Recebendo por composição os dados do arquivo .csv já organizados
        self.texts = []

    def text_generator(self):

        data = self.file
        #Atribuindo dados tratados para as variáveis
        for item in data:
            nome = item["nome"]
            cpf = item["cpf"]
            curso = item["nome_curso"]
            coordenador = item["nome_coordenador"]
            data1 = item["data_inicio"]
            data2 = item["data_termino"]
            carga = item["carga_horaria"]
            
            #Gerando os textos - texto principal
            text = f"Certificamos que <b>{nome}</b>, CPF <b>{cpf}</b>, participou, como CURSISTA, do Projeto de extensão contínuo <b>{curso}</b>, coordenado por <b>{coordenador}</b>, selecionado através do EDITAL No 03/2020/PROEN/IFS - PROGRAMA INSTITUCIONAL DE PESQUISA MULTIDISCIPLINAR DE APOIO AO ENSINO, no período de <b>{data1}</b> a <b>{data2}</b>, com uma carga horária total de <b>{carga}h</b>."
            
            #Capturando data
            date = Date()
            date.pick_date()
            get_date = date.date_convert()
            year, month, day = get_date[0], get_date[1], get_date[2]

            #Gerando os textos - texto data e local
            set_line = f"Corrente - PI, {day} de {month} de {year}"

            line = ["______________________", "______________________"]
            
            #Gerando os textos - textos coordenação e direção

            nome_diretor = "Israel Lobato Rocha"
            footer1 = [f"<b>{coordenador}</b>", f"<b>{nome_diretor}</b>"]
            footer2 = ["Coordenador do Curso","Diretor Geral"]
            footer3 = ["IFPI - Campus Corrente", "IFPI - Campus Corrente"]

            #Salvando todos os textos
            self.texts.append([text, set_line, footer1, footer2, footer3, line])

    def save_as_img(self):
        
        for x in range(0, len(self.file)):
            path = f"Certificado\certificado{x+1}.pdf"
            imgs = convert_from_path(path, dpi=200)
            for img in imgs:
                img.save(f"CertificadosImagem\certificado{x+1}.png", "PNG")


    def save_as_pdf(self):
        
        #Criando os PDFs
        for x in range(0, len(self.file)):
            pdf = canvas.Canvas(f'Certificados/certificado{x+1}.pdf')
            #Selecionando a imagem de fundo
            pdf.drawImage(self.img, 0, 0, 29.7*cm, 21*cm)
            
            #Capturando estilos de paragrafo
            styles = Style()
            styles.create_style()
            get_styles = styles.get_styles()
            style, style2, style3 = get_styles[0], get_styles[1], get_styles[2]
            
            #Atribuindo ao texto principal um estilo de paragrafo
            text = Paragraph(self.texts[x][0], style)

            text.wrapOn(pdf, 650, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
            text.drawOn(pdf, 100, 210) #Determinando coordenadas do inicio do texto (x, y)
            
            #Atribuindo ao texto local-data um estilo de paragrafo
            set_line = Paragraph(self.texts[x][1], style)

            set_line.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
            set_line.drawOn(pdf, 300, 170) #Determinando coordenadas do inicio do texto (x, y)

            #Colocando linha
            line = self.texts[x][5]

            f_line = Paragraph(line[0], style)

            f_line.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
            f_line.drawOn(pdf, 180, 140) #Determinando coordenadas do inicio do texto (x, y)

            f_line = Paragraph(line[1], style)

            f_line.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
            f_line.drawOn(pdf, 515, 140) #Determinando coordenadas do inicio do texto (x, y)
            


            #Capturando texto coordenador - diretor
            text1 = self.texts[x][2]
            #Atribuindo ao texto coordenador um estilo de paragrafo
            footer1 = Paragraph(text1[0], style2)

            footer1.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
            footer1.drawOn(pdf, 170, 120) #Determinando coordenadas do inicio do texto (x, y)

            #Atribuindo ao texto diretor um estilo de paragrafo
            footer1 = Paragraph(text1[1], style2)

            footer1.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
            footer1.drawOn(pdf, 525, 120) #Determinando coordenadas do inicio do texto (x, y)
            
            #Capturando texto titulos
            text2 = self.texts[x][3]
            #Atribuindo ao texto titulo coordenador um estilo de paragrafo
            footer2 = Paragraph(text2[0], style3)

            footer2.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
            footer2.drawOn(pdf, 190, 100) #Determinando coordenadas do inicio do texto (x, y)
            
            #Atribuindo ao texto titulo diretor um estilo de paragrafo
            footer2 = Paragraph(text2[1], style3)

            footer2.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
            footer2.drawOn(pdf, 550, 100) #Determinando coordenadas do inicio do texto (x, y)

            #Capturando texto instituição
            text3 = self.texts[x][4]
            footer3 = Paragraph(text3[0], style3)

            footer3.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
            footer3.drawOn(pdf, 190, 80) #Determinando coordenadas do inicio do texto (x, y)

            footer3 = Paragraph(text3[1], style3)

            footer3.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
            footer3.drawOn(pdf, 525, 80) #Determinando coordenadas do inicio do texto (x, y)
            
            #Determinando a página do pdf como horizontal
            canvas.Canvas.setPageSize(pdf, (landscape(A4)))

            #Salvando PDF
            pdf.save()