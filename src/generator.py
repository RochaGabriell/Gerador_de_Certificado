#Importando bibliotecas e metodos necessários
from src.dataManager import DataManager
from src.styleGenerator import Style
from src.dateGenerator import DateGenerator

from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import Paragraph
from reportlab.lib  import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY  
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
from pdf2image import convert_from_path
import os

class CertificateGenerator:
    def __init__(self, img: str, file: str) -> None:
        self.img = img
        self.file = DataManager(file).get_data() #Recebendo por composição os dados do arquivo .csv já organizados
        self.folder_name = []
        self.texts = []

    def folder_generater(self, cont: int, nome: str) -> None:
        new_folder = f"archive/{cont+1}_{'_'.join((nome.split())[0:2])}"
        os.mkdir(new_folder)
        self.folder_name.append(new_folder)

    def text_generator(self) -> None:
        data = self.file
        #Atribuindo dados tratados para as variáveis
        for cont, item in enumerate(data):
            # Gerar pasta do respectivo aluno
            self.folder_generater(cont, item['nome'])

            #Gerando os textos - texto principal
            text = f"Certificamos que <b>{item['nome']}</b>, CPF <b>{item['cpf']}</b>, participou, como CURSISTA, do Projeto de extensão contínuo <b>{item['nome_curso']}</b>, coordenado por <b>{item['nome_coordenador']}</b>, selecionado através do <b>EDITAL Nº 03/2020/PROEN/IFS - PROGRAMA INSTITUCIONAL DE PESQUISA MULTIDISCIPLINAR DE APOIO AO ENSINO</b>, no período de <b>{item['data_inicio']}</b> a <b>{item['data_termino']}</b>, com uma carga horária total de {item['carga_horaria']} horas."

            #Capturando data
            date = DateGenerator()
            date.pick_date()
            date.date_convert()
            date_line = date.get_date()
            #Gerando os textos - texto data e local
            set_line = f"Corrente - PI, {date_line[0]} de {date_line[1]} de {date_line[2]}"

            #Gerando os textos - textos coordenação e direção
            nome_diretor = "Israel Lobato Rocha"
            nome_coordenador = "Felipe Gonçalves dos Santos"
            footer0 = ["_"*30]
            footer1 = [f"<b>{nome_coordenador}</b>", f"<b>{nome_diretor}</b>"]
            footer2 = ["Coordenador do Curso","Diretor Geral"]
            footer3 = ["IFPI - Campus Corrente", "IFPI - Campus Corrente"]

            #Salvando todos os textos
            self.texts.append([text, set_line, footer1, footer2, footer3, footer0])

    def save_as_img(self) -> None:
        cont_p = len(self.texts)
        for cont in range(cont_p):
            img = convert_from_path(f"{self.folder_name[cont]}/certificado{cont+1}.pdf", dpi=200)
            for imgs in img:
                imgs.save(f"{self.folder_name[cont]}/certificado{cont+1}.png", "PNG")

    def save_as_pdf(self) -> None:
        #Criando os PDFs
        for cont in range(len(self.file)):
            pdf = canvas.Canvas(f'{self.folder_name[cont]}/certificado{cont+1}.pdf')

            #Selecionando a imagem de fundo
            pdf.drawImage(self.img, 0, 0, 29.7*cm, 21*cm)
            # pdfmetrics.registerFont(TTFont("Roboto-Medium", "fonts/Roboto/Roboto-Medium.ttf"))
            # pdfmetrics.registerFont(TTFont("Roboto-Black", "fonts/Roboto/Roboto-Black.ttf"))

            # Posicionar todos os elementos
            self.file_coordinates(pdf, cont)

            #Determinando a página do pdf como horizontal
            canvas.Canvas.setPageSize(pdf, (landscape(A4)))

            #Salvando o PDF
            pdf.save()

    def file_coordinates(self, pdf, cont: int) -> None:
        #Capturando estilos de paragrafo
        styles = Style()
        styles.create_style()
        get_styles = styles.get_styles()
        style, style2, style3 = get_styles[0], get_styles[1], get_styles[2]

        #Atribuindo ao texto principal um estilo de paragrafo
        text = Paragraph(self.texts[cont][0], style)

        text.wrapOn(pdf, 660, 310) #Determinando pontos de quebra de texto (na direita e esquerda)
        text.drawOn(pdf, 90, 210) #Determinando coordenadas do inicio do texto (x, y)
        
        #Atribuindo ao texto local-data um estilo de paragrafo
        set_line = Paragraph(self.texts[cont][1], style)

        set_line.wrapOn(pdf, 305, 260) #Determinando pontos de quebra de texto (na direita e esquerda)
        set_line.drawOn(pdf, 315, 170) #Determinando coordenadas do inicio do texto (x, y)

        #Capturando texto coordenador - diretor
        text1 = self.texts[cont][2]
        #Atribuindo ao texto coordenador um estilo de paragrafo
        footer1 = Paragraph(text1[0], style2)

        footer1.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
        footer1.drawOn(pdf, 170, 115) #Determinando coordenadas do inicio do texto (x, y)

        #Atribuindo ao texto diretor um estilo de paragrafo
        footer1 = Paragraph(text1[1], style2)

        footer1.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
        footer1.drawOn(pdf, 525, 115) #Determinando coordenadas do inicio do texto (x, y)
        
        #Capturando texto titulos
        text2 = self.texts[cont][3]
        #Atribuindo ao texto titulo coordenador um estilo de paragrafo
        footer2 = Paragraph(text2[0], style3)

        footer2.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
        footer2.drawOn(pdf, 190, 100) #Determinando coordenadas do inicio do texto (x, y)
        
        #Atribuindo ao texto titulo diretor um estilo de paragrafo
        footer2 = Paragraph(text2[1], style3)

        footer2.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
        footer2.drawOn(pdf, 550, 100) #Determinando coordenadas do inicio do texto (x, y)

        #Capturando texto instituição
        text3 = self.texts[cont][4]
        footer3 = Paragraph(text3[0], style3)

        footer3.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
        footer3.drawOn(pdf, 188, 85) #Determinando coordenadas do inicio do texto (x, y)

        footer3 = Paragraph(text3[1], style3)

        footer3.wrapOn(pdf, 355, 190) #Determinando pontos de quebra de texto (na direita e esquerda)
        footer3.drawOn(pdf, 525, 85) #Determinando coordenadas do inicio do texto (x, y)

        #Linha de assinatura
        text4 = self.texts[cont][5]
        footer0 = Paragraph(text4[0], style3)

        footer0.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
        footer0.drawOn(pdf, 155, 130) #Determinando coordenadas do inicio do texto (x, y)

        footer0 = Paragraph(text4[0], style3)

        footer0.wrapOn(pdf, 355, 200) #Determinando pontos de quebra de texto (na direita e esquerda)
        footer0.drawOn(pdf, 485, 130) #Determinando coordenadas do inicio do texto (x, y)