import io
import PyPDF2 # type: ignore
from reportlab.pdfgen import canvas # type: ignore
from reportlab.lib.pagesizes import A4 # type: ignore
import random
import string
import requests

class CodeGenerator:
    def __init__(self):
        self.used_codes = set()

    def generate_code(self, prefix='CRT', length=6):
        while True:
            # Generate a random portion for the course code
            random_portion = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
            # Combine the prefix with the random portion
            course_code = f'{prefix}{random_portion}'
            # Check if the generated course code is unique
            if course_code not in self.used_codes:
                self.used_codes.add(course_code)
                return course_code


code_gen = CodeGenerator()


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
        

def setInfo(index, data):
        data = data[index]
        code = code_gen.generate_code()

        replacements = {
            '{TEACHER}': data["teacherName"],
            '{DATE}': data["Date"],
            '{COURSE}': data["courseName"],
            '{STUDENT}': data["userName"]
        }

        placeholder_positions = {
            '{TEACHER}': (100, 125),
            '{DATE}': (165, 227),
            '{COURSE}': (90, 260),
            '{STUDENT}': (90, 350)
        }

        input_pdf_path = "server/static/certificate/certificate_template.pdf"
        output_pdf_path = f"server/static/certificate/{code}.pdf"

        create_new_pdf(input_pdf_path, output_pdf_path, replacements, placeholder_positions)
        
        return output_pdf_path