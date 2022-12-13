from fpdf import FPDF
projeto = input('digite o nome do projeto: ')
horas_estimadas = input('horas estimadas: ')
valor_da_hora = input('valor da hora: ')
prazo = input('prazo estimado: ')
valor_total = int(valor_da_hora) * int(horas_estimadas)


pdf = FPDF()
pdf.add_page()
pdf.image('template.png', x=0, y=0)
pdf.set_font('Arial')

pdf.text(115, 145, projeto.capitalize())
pdf.text(115, 160, str(horas_estimadas))
pdf.text(115, 175, str(valor_da_hora))
pdf.text(115, 190, prazo.capitalize())
pdf.text(115, 205, str(valor_total))
pdf.output('orçamentos.pdf')
