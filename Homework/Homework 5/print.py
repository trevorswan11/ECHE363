from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import string

def clean_text(line):
    # Replace tabs with spaces (or adjust as needed)
    line = line.replace("\t", "    ")  # Replace tabs with 4 spaces
    # Remove non-printable characters, but keep spaces, line breaks, and basic punctuation
    line = ''.join(c if c.isprintable() else ' ' for c in line)  # Replace non-printable with space
    return line

def text_to_pdf(input_file, output_file):
    with open(input_file, 'r', newline=None, encoding='utf-8') as file:
        lines = file.readlines()

    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    text_object = c.beginText(40, height - 40)
    text_object.setFont("Helvetica", 10)
    line_height = 12  # Adjust line height

    for line in lines:
        # Normalize line endings to avoid issues with \r\n
        line = line.replace("\r\n", "\n").replace("\r", "\n")
        
        # Clean the line before adding it to the PDF
        cleaned_line = clean_text(line)

        # If the text exceeds the bottom margin, add a new page
        if text_object.getY() - line_height < 40:
            c.drawText(text_object)
            c.showPage()  # Start a new page
            text_object = c.beginText(40, height - 40)
            text_object.setFont("Helvetica", 10)

        # Preserve the indentation and add the cleaned line
        text_object.textLine(cleaned_line)

    c.drawText(text_object)
    c.save()
    
text_to_pdf('tcs94_ECHE363_HW5-1.py', 'tcs94_ECHE363_HW5-1.pdf')
