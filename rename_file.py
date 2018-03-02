import os
import string
def rename_files():
      #get file names from a folder
      file_list = os.listdir(r"D:\Art Work\New folder")
      print(file_list)
      print("--------------------------------------------------------")
      saved_path=os.getcwd()
      #print(saved_path)
      os.chdir(r"D:\Art Work\New folder")
      for file_name in file_list :
          print("Old name: "+file_name)
          print("New name:"+file_name.translate(('so',1)))
          os.rename(file_name,file_name.translate(('so',1)))
      os.chdir(saved_path)

rename_files()


