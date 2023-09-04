""" Get lhc datasets """

from zipfile import ZipFile
from tqdm import tqdm
import os
import wget


URL = "https://www.dropbox.com/scl/fi/gvmelw7u619moo8nyg3j7/ErUMData.zip?rlkey=kq4do1fmalppjt2v24lzau4li&dl=1"
NAME = "ErUMData.zip"
wget.download(URL, f"{NAME}")

# Re-open the newly-created file with ZipFile()
with ZipFile(NAME ,"r") as zip_ref:
     for file in tqdm(iterable=zip_ref.namelist(), total=len(zip_ref.namelist())):
          zip_ref.extract(member=file)
          
os.remove(NAME)