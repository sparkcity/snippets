#source: https://www.geeksforgeeks.org/how-to-merge-multiple-excel-files-into-a-single-files-with-python/

import glob
import pandas as pd
 
path = "C:/path/to/files"
 
file_list = glob.glob(path + "/*.xlsx")
 
excl_list = []
 
for file in file_list:
    excl_list.append(pd.read_excel(file))
 
excl_merged = pd.DataFrame()
 
for excl_file in excl_list:

    excl_merged = excl_merged.append(
      excl_file, ignore_index=True)

excl_merged.to_excel('name-of-merged-file.xlsx', index=False)