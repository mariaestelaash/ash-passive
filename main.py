import tkinter as tk
from tkinter import filedialog
import pandas as pd
from tkinter import messagebox

#dont forget to write achive name is releated to the last upload

def clean_unnecessary_collumns(df,name):
  header = ["ID",'Penetration No.','Location','FRL','Ref', 'Is Active']
  df.to_csv(name+'.csv',columns= header,index = False)

def sort_by_location(archive_name):
  df = archive_name
  df = df.sort_values(by=['ID'],ascending=False)
  df = df.sort_values(by=['Location'])
  return df


def submit_action():
    file_path = file_entry.get()
    text_input = text_entry.get("1.0", "end-1c") or "report"
    csv_data = pd.read_csv(
                file_path)
    new_df = sort_by_location(csv_data)
    clean_unnecessary_collumns(new_df,text_input)
    messagebox.showinfo("Submission", "Done")
    file_entry.delete(0, tk.END)
    text_entry.delete("1.0", tk.END)

def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# Create the main window
root = tk.Tk()
root.title("Ashpassive App - v.0.0.1")

# File Input
file_label = tk.Label(root, text="File:")
file_label.grid(row=0, column=0, padx=5, pady=5)
file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1, padx=5, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Text Input
text_label = tk.Label(root, text="Text:")
text_label.grid(row=1, column=0, padx=5, pady=5)
text_entry = tk.Text(root, height=3, width=40)
text_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()


