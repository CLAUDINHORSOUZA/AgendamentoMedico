from fpdf import FPDF

def gerar_pdf(dados, nome_arquivo="medico.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for chave, valor in dados.items():
        pdf.cell(200, 10, txt=f"{chave}: {valor}", ln=True)

    pdf.output(nome_arquivo)
    return nome_arquivo

