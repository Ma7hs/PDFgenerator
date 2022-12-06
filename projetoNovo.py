from fpdf import FPDF

descriptionProject = input("Digite a descrição do projeto: ")
hoursProject = input("Digite as horas estimadas da aplicação: ")
hoursValue = input("Digite o valor de hora trabalhada: ")
prizeProject = input("Prazo estimado de conclusão: ")
estimatedTotalValue = int(hoursProject) * int(hoursValue)

newPdf = FPDF()
newPdf.add_page()
newPdf.set_font("Arial")
newPdf.image("modeloOrcamento.png")

newPdf.output("Orçamento.pdf")
print("PDF gerado com sucesso!")