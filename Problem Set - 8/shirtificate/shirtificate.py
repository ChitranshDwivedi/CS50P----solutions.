from fpdf import FPDF

def main():
    name = input("Name: ")
    shirtificate(name)

def shirtificate(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=30)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.image("shirtificate.png", x=10, w=190)

    pdf.set_font("Helvetica", "B", size=26)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(pdf.get_y() - 100) 
    pdf.cell(0, 0, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

main()

