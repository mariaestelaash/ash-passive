import pandas as pd
import io
import requests 
from requests.auth import HTTPBasicAuth
import tkinter as tk
from tkinter import filedialog


def get_ids(path):
  df = pd.read_csv(path)
  list_ids = []
  for id in df['Asset ID']:
    list_ids.append( id)
  return list_ids

def api_connection(client_id,client_secret,user_name,password):
  token_url = 'https://ashpassive.onuptick.com/api/oauth2/token/'
  
  # Make a request to get the access token
  token_response = requests.post(token_url, auth=HTTPBasicAuth(client_id, client_secret), data={
      'grant_type': 'password',
      'username': user_name,
      'password': password,
      'client_id': client_id,
      'client_secret': client_secret
  })

  return token_response

def check_photos(token_response,list_ids):
  if token_response.status_code == 200:
    access_token = token_response.json().get('access_token')
    id_without_photo = []
    for id in list_ids:
      api_url = f'https://ashpassive.onuptick.com/api/v2/uploads/assets/{id}/photos/'
      headers = {'Authorization': 'Bearer ' + access_token}

      # Make a request to the API endpoint
      api_response = requests.get(api_url, headers=headers)
      if api_response.json()['total'] == 0:
        id_without_photo.append(id)
      
  else:
      print("Failed to make request to API:", api_response.status_code)
  return {'ids' :id_without_photo}

def create_new_df(df,level):
  df = pd.DataFrame(df)
  df.to_csv(f'assets_id_no_photo_{level}',index=False)
def submit():
    client_id_val = client_id.get()
    client_secret_val = client_secret.get()
    user_name_val = user_name.get()
    password_val = password.get()
    level_name_val = level_name.get()
    file_path = file_entry.get()
    list_ids = get_ids(
                file_path)
    token_response = api_connection(client_id_val,
                                  client_secret_val,
                                   user_name_val,
                                    password_val
                                              )
    df = check_photos(token_response, list_ids)
    create_new_df(df,level_name_val)

def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# Create main window
root = tk.Tk()
root.title("Audit team - AshPassive Fire")

# Client ID
client_id_label = tk.Label(root, text="Client ID:")
client_id_label.grid(row=0, column=0)
client_id = tk.Entry(root)
client_id.grid(row=0, column=1)

# Client Secret
client_secret_label = tk.Label(root, text="Client Secret:")
client_secret_label.grid(row=1, column=0)
client_secret = tk.Entry(root)
client_secret.grid(row=1, column=1)

# User Name
user_name_label = tk.Label(root, text="User Name:")
user_name_label.grid(row=2, column=0)
user_name = tk.Entry(root)
user_name.grid(row=2, column=1)

# Password
password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0)
password = tk.Entry(root, show="*")
password.grid(row=3, column=1)

# Level Name
level_name_label = tk.Label(root, text="Level Name:")
level_name_label.grid(row=4, column=0)
level_name = tk.Entry(root)
level_name.grid(row=4, column=1)

# Button to upload CSV file
file_label = tk.Label(root, text="File:")
file_label.grid(row=5, column=0, padx=5, pady=5)
file_entry = tk.Entry(root, width=40)
file_entry.grid(row=5, column=1, padx=5, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=5, column=2, padx=5, pady=5)


# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=6, columnspan=2)

root.mainloop()