import tkinter as tk
from tkinter import filedialog
import csv
from PyPDF2 import PdfReader, PdfWriter
from tkinter import messagebox


def split_pages(pdf_file_path,pages):
  file_base_name = pdf_file_path.replace('.pdf', '')
  pdf = PdfReader(pdf_file_path)
  count = 0
  for page_num in pages:
    pdfWriter = PdfWriter()
    pdfWriter.add_page(pdf.pages[int(page_num)-1])
    with open(str(count)+'PAGE.pdf', 'wb') as f:
      pdfWriter.write(f)
      f.close()
    count +=1

def browse_pdf():
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    pdf_entry.insert(tk.END, filename)

def submit_pdf():
    file_name = pdf_entry.get()
    num_pages = pages_entry.get()
    pages = num_pages.split(",")
    split_pages(file_name,pages)
    messagebox.showinfo("Submission", "Done")
    pdf_entry.delete(0, tk.END)
    pages_entry.delete(0, tk.END)
   


if __name__ == "__main__":

    root2 = tk.Tk()
    root2.title("PDF Screen - ash passive")

    pdf_label = tk.Label(root2, text="PDF Archive:")
    pdf_label.grid(row=0, column=0, padx=10, pady=10)

    pdf_entry = tk.Entry(root2, width=40)
    pdf_entry.grid(row=0, column=1, padx=10, pady=10)

    pdf_button = tk.Button(root2, text="Browse", command=browse_pdf)
    pdf_button.grid(row=0, column=2, padx=10, pady=10)

    pages_label = tk.Label(root2, text="Number of Pages:")
    pages_label.grid(row=1, column=0, padx=10, pady=10)
    
    
    pages_entry = tk.Entry(root2, width=40)
    pages_entry.grid(row=1, column=1, padx=10, pady=10)

    submit_button_pdf = tk.Button(root2, text="Submit", command=submit_pdf)
    submit_button_pdf.grid(row=2, column=1, padx=10, pady=10)
    created_by_label = tk.Label(root2, text="by: Maria Estela")
    created_by_label.grid(row=3, column=1, padx=5, pady=5)


    root2.mainloop()