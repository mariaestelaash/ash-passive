from PyPDF2 import PdfReader, PdfWriter
import pandas as pd

def clean_unnecessary_collumns(df,name):
  header = ["ID",'Penetration No.','Location','FRL','Ref','Building Element',
            'Variant','Asset Building Level',
            'Is Active','Type','Label', 'Contractor']
  df.to_csv(name+'.csv',columns= header,index = False)

def sort_by_location(archive_name):
  df = archive_name
  df = df.sort_values(by=['ID'],ascending=False)
  df = df.sort_values(by=['Location'])
  return df


def split_pages(pdf_file_path,pages):
  file_base_name = pdf_file_path.replace('.pdf', '')

  pdf = PdfReader(pdf_file_path)
  count = 0
  for page_num in pages:
    pdfWriter = PdfWriter()
    pdfWriter.add_page(pdf.pages[page_num])
    with open(str(count)+'PAGE_{0}_subset.pdf'.format(file_base_name), 'wb') as f:
      pdfWriter.write(f)
      f.close()
    count +=1