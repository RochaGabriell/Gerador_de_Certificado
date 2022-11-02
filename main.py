from src.generator import CertificateGenerator

def main():
    file = "database/database.csv"
    img = "database/certificado_molde.jpg"

    print("Gerando certificados...")
    certificate = CertificateGenerator(img, file)
    print("Gerando textos...")
    certificate.text_generator()
    print("Gerando PDFs...")
    certificate.save_as_pdf()
    print("Gerando imagens...")
    certificate.save_as_img()
    print("Certificados gerados com sucesso!")

if __name__ == "__main__":
    main()