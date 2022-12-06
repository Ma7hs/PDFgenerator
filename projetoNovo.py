!pip install FPDF

from fpdf import FPDF

descriptionProject = input("Digite a descrição do projeto: ")
hoursProject = input("Digite as horas estimadas da aplicação: ")
hoursValue = input("Digite o valor de hora trabalhada: ")
prizeProject = input("Prazo estimado de conclusão: ")
estimatedTotalValue = int(hoursProject) * int(hoursValue)

newPdf = FPDF()
newPdf.add_page()
newPdf.set_font("Arial")
newPdf.image("template.png", x=0, y=0)


newPdf.text(115, 147, descriptionProject)
newPdf.text(115, 161, hoursProject)
newPdf.text(115, 176, hoursValue)
newPdf.text(115, 191, prizeProject)
newPdf.text(115, 206, str(estimatedTotalValue))


newPdf.output("Orçamento.pdf")
print("PDF gerado com sucesso!")
