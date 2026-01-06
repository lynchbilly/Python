# CS50 Shirtificate
# Generates a PDF certificate with a shirt

from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Title
        self.set_font("helvetica", "B", 50)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.ln(70)


def main():
    # Get name from user
    name = input("Name: ")
    
    # Create PDF
    pdf = PDF()
    pdf.add_page()
    
    # Add shirt image
    pdf.image("shirtificate.png", x=10, y=70, w=190)
    
    # Add name on shirt
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 213, f"{name} took CS50", align="C")
    
    # Save PDF
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
