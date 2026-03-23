from fpdf import FPDF
import re
import sys


class CreateShirt:
    def __init__(self, name):
        """
        Initializes the shirt object and validates the user's name.
        """
        # Ensure name is between 1-20 characters and contains only valid symbols
        if not re.search(r"^[\w ]{1,20}$", name):
            sys.exit("Not a name")
        self.name = name

    def create_pdf(self):
        """
        Generates a PDF certificate featuring a T-shirt with the user's name.
        """

        pdf = FPDF()
        pdf.add_page()
        # Configure Header: Large centered title at the top
        pdf.set_font("helvetica", style="B", size=45)
        pdf.cell(0, 50, "CS50 Shirtificate", align="C")

        # Image: Positions the shirt image to cover most of the page width
        pdf.image("shirtificate.png", x=10, y=70, w=190)

        # Overlay Text: Switches to white and positions the cursor over the shirt's chest area
        pdf.set_y(140)
        pdf.set_font("helvetica", style="B", size=24)
        pdf.set_draw_color(255, 255, 255)
        pdf.cell(0, 15, f"{self.name} took CS50", align="C")
        pdf.output("shirtificate.pdf")


def main():
    # Get user input and initiate the PDF generation process
    name = input("Name for T-Shirt: ")
    shirt = CreateShirt(name)
    shirt.create_pdf()


if __name__ == "__main__":
    main()
