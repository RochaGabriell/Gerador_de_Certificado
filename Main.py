from CertificadoGenerator import CertificateGenerator

#As letras são corrigidas no LINUX - Não ocorre pelo menos -

file = "Arquivo\database.csv"
img = "Modelo\model.jpg"


certificate = CertificateGenerator(img, file)
certificate.text_generator()
print("Texto gerado !")
certificate.save_as_pdf()
print("Pdf salvo!")

#Certificado como imagem não funciona devido ao poppler, porém segundo fontes esse problema não ocorre no LINUX caso queira testar
#certificate.save_as_img()
