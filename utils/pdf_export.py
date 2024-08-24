from fpdf import FPDF
import matplotlib.pyplot as plt
import io


# Function to export MaxDiff scores to a PDF file
def export_maxdiff_to_pdf(maxdiff_scores, filename, image_path):

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
    pdf.cell(cell_width, cell_height, "question", border=1)
    pdf.cell(cell_width, cell_height, "most_preferred", border=1)
    pdf.cell(cell_width, cell_height, "least_preferred", border=1)
    pdf.cell(cell_width, cell_height, "total_proposed", border=1)

    pdf.ln(cell_height)  # Move to the next line

    # Add table data
    for item in maxdiff_scores:
        pdf.cell(cell_width, cell_height, item.question_text, border=1)
        pdf.cell(cell_width, cell_height, str(item.most_preferred), border=1)
        pdf.cell(cell_width, cell_height, str(item.least_preferred), border=1)
        pdf.cell(cell_width, cell_height, str(item.total_proposed), border=1)
        pdf.ln(cell_height)  # Move to the next line

    # Generate the plot image in memory
    # items = list(maxdiff_scores.keys())
    # scores = list(maxdiff_scores.values())

    # plt.figure(figsize=(8, 6))
    # plt.bar(items, scores, color="skyblue")
    # plt.xlabel("Features")
    # plt.ylabel("MaxDiff Score")
    # plt.title("MaxDiff Scores of Survey Features")
    # plt.ylim(
    #     -max(abs(min(scores)), max(scores)) - 1, max(abs(min(scores)), max(scores)) + 1
    # )
    # plt.axhline(0, color="black", linewidth=0.5)

    # # Save the plot to a bytes buffer
    # buf = io.BytesIO()
    # plt.savefig(buf, format="png")
    # buf.seek(0)

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
