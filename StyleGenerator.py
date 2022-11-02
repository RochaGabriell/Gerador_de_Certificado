from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib  import colors

class Style:

    def __init__(self) -> None:
        
        self.styles = []

    def create_style(self):

        styles = getSampleStyleSheet()
        #Criando estilos de paragrafos
        style = ParagraphStyle( name='Normal_CENTER',
                                parent=styles['Normal'],
                                fontName='Helvetica',
                                wordWrap='LTR',
                                alignment=TA_JUSTIFY,
                                fontSize=13,
                                leading=23,
                                textColor=colors.HexColor('#000'),
                                splitLongWords=True,
                                spaceShrinkage=0.05,
                                )
        style2 = ParagraphStyle( name='Left',
                                    parent=styles['Normal'],
                                    fontName='Helvetica',
                                    wordWrap='LTR',
                                    alignment=TA_JUSTIFY,
                                    fontSize=12,
                                    leading=23,
                                    textColor=colors.HexColor('#000'),
                                    splitLongWords=True,
                                    spaceShrinkage=0.05,
                                )
        style3 = ParagraphStyle( name='Left',
                                    parent=styles['Normal'],
                                    fontName='Helvetica',
                                    wordWrap='LTR',
                                    alignment=TA_JUSTIFY,
                                    fontSize=11,
                                    leading=23,
                                    textColor=colors.HexColor('#000'),
                                    splitLongWords=True,
                                    spaceShrinkage=0.05,
                                )
        
        self.styles = [style, style2, style3]

    def get_styles(self):

        return self.styles