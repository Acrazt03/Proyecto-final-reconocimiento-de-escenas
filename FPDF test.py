from fpdf import FPDF

# create FPDF object
# Layout ('P','L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
pdf = FPDF('P', 'mm', 'A4')

# Add a page
pdf.add_page()

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
pdf.set_font('helvetica', 'BI', 16)
pdf.set_text_color(0,0,0)

# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)FICHA TECNICA PN20220415
# border (0 False; 1 True - add border around cell)

def printBlankLine(pdf, w=190,h=3,ln=1):
    #pdf.set_fill_color(255, 255, 255)
    pdf.cell(w=w, h = h, txt = '', border = 0, ln = ln, 
          align = 'C', fill = False, link = '')

pdf.image("logo-policia.png", w = 30, h = 30, type = 'PNG', link = '', x=pdf.w/2-30/2,y=10)

printBlankLine(pdf,w=45,h=10,ln=1)

pdf.cell(w=10,h=23,txt='',border=0,ln=1)

pdf.cell(w=80, h = 10, txt = 'FICHA TECNICA PN20220415', border = 1, ln = 0, 
          align = 'C', fill = False, link = '')

printBlankLine(pdf,w=45,h=10,ln=0)

pdf.cell(w=65, h = 10, txt = 'Alejandra Ortega Nunez', border = 1, ln = 1, 
          align = 'R', fill = False, link = '')

printBlankLine(pdf)

pdf.set_fill_color(68, 115, 197)
pdf.cell(w=190, h = 7, txt = '', border = 0, ln = 1, 
          align = 'C', fill = True, link = '')

printBlankLine(pdf)

pdf.set_font('helvetica', 'BU', 16)
pdf.set_fill_color(189, 216, 237)
pdf.cell(w=190, h = 15, txt = 'DESCRIPCION', border = 0, ln = 1, 
          align = 'C', fill = True, link = '')

printBlankLine(pdf)
printBlankLine(pdf,w=10,ln=0)

#print(pdf.w,pdf.h)#210,297

pdf.set_fill_color(0,113,193)
pdf.cell(w=80, h = 80, txt = '', border = 0, ln = 0, 
          align = 'C', fill = True, link = '')

pdf.image("Alejandra_0.JPG", w = 60, h = 60, type = 'JPG', link = '', x=30,y=95)

#pdf.multi_cell(40,10,'Hello World!,how are you today',1,0)

printBlankLine(pdf,w=5,h=80,ln=0)

descripcion_text = """ID:
Fecha de Nacimiento:
Edad:
Género:
Estatura:
Peso: 
Tono de piel:
Ojos:
Cabello:
Cicatrices:
Alias o apodo:
"""

pdf.set_font('helvetica', '', 8)
pdf.multi_cell(80 ,7,descripcion_text,True)

printBlankLine(pdf,h=5)

pdf.set_font('helvetica', 'BU', 16)
pdf.set_fill_color(189, 216, 237)
pdf.cell(w=190, h = 15, txt = 'OTRO DATOS', border = 0, ln = 1, 
          align = 'C', fill = True, link = '')

printBlankLine(pdf,h=3)

descripcion_text = """
Padre:

Madre:

Dirección:

"""

pdf.set_font('helvetica', '', 14)
pdf.multi_cell(190 ,4,descripcion_text,True)

printBlankLine(pdf,h=5)

pdf.set_font('helvetica', 'BU', 16)
pdf.set_fill_color(189, 216, 237)
pdf.cell(w=190, h = 15, txt = 'RECORD DELICTIVO', border = 0, ln = 1, 
          align = 'C', fill = True, link = '')

printBlankLine(pdf,h=3)

descripcion_text = """
Delitos:

Otros casos:

Instrumentos usados:

"""

pdf.set_font('helvetica', '', 14)
pdf.multi_cell(190 ,4,descripcion_text,True)

pdf.output('pdf_1.pdf')