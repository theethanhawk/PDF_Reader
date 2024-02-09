import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename
from tkinter import Tk

def read_pdf_aloud(pdf_path):
    # Updated to use PdfReader instead of PdfFileReader
    with open(pdf_path, 'rb') as file:
        pdfreader = PyPDF2.PdfReader(file)
        pages = len(pdfreader.pages)  # Updated to get the number of pages

        reader = pyttsx3.init()  # Initialize the reader once

        for num in range(pages):
            page = pdfreader.pages[num]  # Updated to access pages
            text = page.extract_text()  # Updated method name to extract_text
            reader.say(text)
            reader.runAndWait()

if __name__ == '__main__':
    Tk().withdraw()  # Avoids the empty tkinter window
    book = askopenfilename()  # Show the dialog only when the script is executed directly

    if book:  # Proceed only if a file is selected
        read_pdf_aloud(book)
    else:
        print("No file selected.")