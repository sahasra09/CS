import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_folder(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dir,files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root,file)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = "/"+file_to+"/"+relative_path
                print(dropbox_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path)

def main():
    access_token = 'wE1yFTm0NoQAAAAAAAAAAZomuuf4gaG9VWMzGWAPlNHjURpaaFMJRSPlNFwVleBp'
    transferdata = TransferData(access_token)

    file_from = 'C:\Users\Sree Sahasra\Desktop\CLASS 100 HA'
    file_to = input('Enter your dropbox path to move the folder to:-')
    transferdata.upload_folder(file_from,file_to)
    print("Files uploaded successfully!")

if __name__ == '__main__':
    main()
