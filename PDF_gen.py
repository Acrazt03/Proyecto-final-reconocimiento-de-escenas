from fpdf import FPDF

campos = {'ID':0, 'Nombres':1, 'Apellidos':2, 'Fecha de nacimiento':3, 'Edad':4, 'Genero':5, 'Estatura':6, 'Peso':7,'Piel':8 ,'Ojos':9, 'Cabello':10 , 'Cicatrices':11 , 'Alias':12  , 'Padre':13 , 'Madre':14 , 'Direccion':15 , 'Delitos':16 , 'Casos asociados':17 , 'Tipo de instrumento usado':18, 'imagenes':19}

def printBlankLine(pdf, w=190,h=3,ln=1):
    #pdf.set_fill_color(255, 255, 255)
    pdf.cell(w=w, h = h, txt = '', border = 0, ln = ln, 
          align = 'C', fill = False, link = '')

def generarPDF(datos):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()

    pdf.set_font('helvetica', 'BI', 16)
    pdf.set_text_color(0,0,0)

    pdf.image("logo-policia.png", w = 30, h = 30, type = 'PNG', link = '', x=pdf.w/2-30/2,y=10)

    printBlankLine(pdf,w=45,h=10,ln=1)

    pdf.cell(w=10,h=23,txt='',border=0,ln=1)

    pdf.cell(w=80, h = 10, txt = 'FICHA TECNICA PN20220415', border = 1, ln = 0, 
            align = 'C', fill = False, link = '')

    nombre = datos[campos['Nombres']] + " " + datos[campos['Apellidos']]

    printBlankLine(pdf,w=45-len(nombre),h=10,ln=0)

    pdf.cell(w=3.5*len(nombre), h = 10, txt = nombre, border = 1, ln = 1, 
            align = 'C', fill = False, link = '')

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

    pdf.image("foto2.jpg", w = 60, h = 60, type = 'JPG', link = '', x=30,y=95)

    #pdf.multi_cell(40,10,'Hello World!,how are you today',1,0)

    printBlankLine(pdf,w=5,h=80,ln=0)

    ID = datos[campos['ID']]
    FechaNac = datos[campos['Fecha de nacimiento']]
    Edad = datos[campos['Edad']]
    Genero = datos[campos['Genero']]
    Estatura = datos[campos['Estatura']]
    Peso = datos[campos['Peso']]
    TonoPiel = datos[campos['Piel']]
    Ojos = datos[campos['Ojos']]
    Cabello = datos[campos['Cabello']]
    Cicatrices = datos[campos['Cicatrices']]
    Alias = datos[campos['Alias']]

    descripcion_text = """
    ID: {}
    Fecha de Nacimiento: {}
    Edad: {}
    Género: {}
    Estatura: {}
    Peso: {} 
    Tono de piel: {}
    Ojos: {}
    Cabello: {}
    Cicatrices: {}
    Alias o apodo: {}
    """.format(ID,FechaNac,Edad,Genero,Estatura,Peso,TonoPiel,Ojos,Cabello,Cicatrices,Alias)

    pdf.set_font('helvetica', '', 8)
    pdf.multi_cell(80 ,7,descripcion_text,True)

    printBlankLine(pdf,h=5)

    pdf.set_font('helvetica', 'BU', 16)
    pdf.set_fill_color(189, 216, 237)
    pdf.cell(w=190, h = 15, txt = 'OTRO DATOS', border = 0, ln = 1, 
            align = 'C', fill = True, link = '')

    printBlankLine(pdf,h=3)

    Padre = datos[campos['Padre']]
    Madre = datos[campos['Madre']]
    Dirreccion = datos[campos['Direccion']]

    descripcion_text = """
    Padre: {}

    Madre: {}

    Dirección: {}

    """.format(Padre,Madre,Dirreccion)

    pdf.set_font('helvetica', '', 12)
    pdf.multi_cell(190 ,3,descripcion_text,True)

    printBlankLine(pdf,h=5)

    pdf.set_font('helvetica', 'BU', 16)
    pdf.set_fill_color(189, 216, 237)
    pdf.cell(w=190, h = 15, txt = 'RECORD DELICTIVO', border = 0, ln = 1, 
            align = 'C', fill = True, link = '')

    printBlankLine(pdf,h=3)

    Delitos = datos[campos['Delitos']]
    OtrosCasos = datos[campos['Casos asociados']]
    Instrumentos = datos[campos['Tipo de instrumento usado']]

    descripcion_text = """
    Delitos: {}

    Otros casos: {}

    Instrumentos usados: {}

    """.format(Delitos,OtrosCasos,Instrumentos)

    pdf.set_font('helvetica', '', 12)
    pdf.multi_cell(190 ,3,descripcion_text,True)

    pdf.output('Reporte.pdf')
    print("Reporte generado")
