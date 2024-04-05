import io
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

data = {
    "teacher_name": "",
    "student_name": "",
    "course_name": "",
    "date_completed": "",
    "student_username": "",
    "course_code": ""
}

def create_new_pdf(input_pdf_path, output_pdf_path, replacements, placeholder_positions):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)

    for placeholder, value in replacements.items():
        x, y = placeholder_positions[placeholder]
        if placeholder == '{TEACHER}':
            can.setFont("Times-Italic", 24)
        elif placeholder == '{DATE}':
            can.setFont("Helvetica", 15)
        else:
            can.setFont("Helvetica-Bold", 24)
        can.drawString(x, y, value)
    can.save()

    packet.seek(0)
    new_pdf = PyPDF2.PdfReader(packet)
    existing_pdf = PyPDF2.PdfReader(open(input_pdf_path, "rb"))
    output = PyPDF2.PdfWriter()
    
    for page_number in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[page_number]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

    with open(output_pdf_path, "wb") as output_stream:
        output.write(output_stream)

replacements = {
    '{TEACHER}': data["teacher_name"],
    '{DATE}': data["date_completed"],
    '{COURSE}': data["course_name"],
    '{STUDENT}': data["student_name"]
}

placeholder_positions = {
    '{TEACHER}': (100, 125),
    '{DATE}': (165, 227),
    '{COURSE}': (90, 260),
    '{STUDENT}': (90, 350)
}

input_pdf_path = "server/static/certificate_template.pdf"
output_pdf_path = "server/static/certificate_{}_{}.pdf".format(data["student_username"], data["course_code"])

create_new_pdf(input_pdf_path, output_pdf_path, replacements, placeholder_positions)
