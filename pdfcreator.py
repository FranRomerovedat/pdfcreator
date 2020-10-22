from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

names = ['name1', 'name2', 'name3']

for name in names:
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 25)
    can.setFillColorRGB(255, 255, 255)
    can.drawString(650, 118, name)
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # read your existing PDF
    existing_pdf = PdfFileReader(open('Users/file.pdf', "rb"))
    output = PdfFileWriter()

    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    # finally, write "output" to a real file
    filename = name+"finalfile.pdf"
    outputStream = open(filename, "wb")
    output.write(outputStream)
    outputStream.close()


