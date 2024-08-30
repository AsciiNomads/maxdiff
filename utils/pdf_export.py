from fpdf import FPDF
import matplotlib.pyplot as plt
import io
import copy


# Function to export MaxDiff scores to a PDF file
def export_maxdiff_to_pdf(maxdiff_scores, filename, image_path):
    def sanitize_text(text):
        return text.encode('latin-1', 'replace').decode('latin-1')

    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "MaxDiff Survey Results", ln=True, align="C")

    # List of features and their MaxDiff scores
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(0, 10, "Features and MaxDiff Scores:", ln=True)

    # Define cell width and height
    cell_width = 40
    cell_height = 10

    # Add table headers
    pdf.cell(cell_width//3, cell_height, "Rank", border=1)
    pdf.cell(cell_width*2//3, cell_height, "Question ID", border=1)
    pdf.cell(cell_width*4//5, cell_height, "Most Preferred", border=1)
    pdf.cell(cell_width*4//5, cell_height, "Least Preferred", border=1)
    pdf.cell(cell_width*4//5, cell_height, "Appearances", border=1)
    pdf.cell(cell_width*3//5, cell_height, "Score %", border=1)

    pdf.ln(cell_height)  # Move to the next line
    
    maxdiff_scores.sort(key=lambda x: x.score, reverse=True)

    # Add table data
    for i, item in enumerate(maxdiff_scores):
        pdf.cell(cell_width//3, cell_height, str(i+1), border=1)
        pdf.cell(cell_width*2//3, cell_height, str(item.id), border=1)
        pdf.cell(cell_width*4//5, cell_height, str(item.most_preferred), border=1)
        pdf.cell(cell_width*4//5, cell_height, str(item.least_preferred), border=1)
        pdf.cell(cell_width*4//5, cell_height, str(item.total_proposed), border=1)
        pdf.cell(cell_width*3//5, cell_height, str(item.score).split('.')[0], border=1)
        pdf.ln(cell_height)  # Move to the next line

    # Add a line break
    pdf.ln(10)

    # Add questions ID and sanitized text
    for question in maxdiff_scores:
        question_id = str(question.id)
        question_text = sanitize_text(question.question_text)
        pdf.set_font("Arial", size=8)
        pdf.cell(200, 10, f"ID: {question_id} - {question_text}", ln=True)

    # Add a line break
    pdf.ln(10)

    # Add the plot image to the PDF
    pdf.ln(10)
    pdf.image(image_path, x=10, w=180)

    # Output the PDF to a file
    pdf.output(filename)



# # Example MaxDiff scores (you can replace this with your actual data)
# maxdiff_scores = {"Feature A": 0, "Feature B": 0, "Feature C": 0}

# # Export to PDF
# filename = "maxdiff_scores.pdf"
# export_maxdiff_to_pdf(maxdiff_scores, filename)
