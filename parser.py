import os
import re

### 01.MAKE "File List" with Folder Postion ###
def mk_file_list(Folder_POS):
    raw_path = os.getcwd()
    data_path = os.path.join(raw_path, Folder_POS)
    file_path = os.path.join(raw_path, "data_list")
    file_list = os.listdir(data_path)
    return file_list

### 02.MAKE "Sample List" with File Format ###
def mk_sample_list(File_Format):
    file_list = mk_file_list(args.Folder_POS)
    sample_list = []
    for sample in file_list:
        if "R1" or "r1" in File_Format:
            if "R1" in File_Format: 
                sample_list.append(re.sub("_R1_.*","",sample))
            elif "r1" in File_Format:
                sample_list.append(re.sub(".r1.*","",sample))
            else:
                print(f"Not Matched Correct Format[{File_Format}] in {sample}")
        else:
            print("Not Correct Format\n", "R1 or r1")
    return sample_list

### 03.MAKE "TNID DICTIONARY" with TNID tsv ###
def read_TNID_tsv(TNID_tsv):
    TNID_file = pd.read_csv(TNID_tsv, sep='\t', header=None)
    TNID_Dic = {}
    for TNID, sam_name in zip(TNID_file.iloc[:,0], TNID_file.iloc[:,1]):
        TNID_Dic[TNID] = sam_name
    return TNID_Dic

### 04.MAKE "TNID DICTIONARY" with TNID tsv ###
def find_Project(TBD_Folder):
    TBD_ID = re.sub(".*TBD","TBD", TBD_Folder).split("_")[0]
    return TBD_ID



if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-F', "--Folder", dest='Folder_POS')
    parser.add_argument('-Fm', "--Format", dest='File_Format')
    parser.add_argument('-TN', "--TNIDtsv", dest='TNID_tsv')
    parser.add_argument('-TBD', "--TBD_folder", dest='TBD_Folder')

    args = parser.parse_args()

### 01.MAKE "File List" with Folder Postion ###
    if args.Folder_POS:
        file_list = mk_file_list(args.Folder_POS)
        print(f'File List : {file_list}')
    else:
        print('-F', "--Folder")

### 02.MAKE "Sample List" with File Format ###
    if (args.File_Format) and (args.Folder_POS):
        sample_list = mk_sample_list(args.File_Format)
        print(f'Sample List : {sample_list}')
    else:
        print('-Fm', "--Format")

### 03.MAKE "TNID DICTIONARY" with TNID tsv ###
    if args.TNID_tsv:
        import pandas as pd
        TNID_Dic = read_TNID_tsv(args.TNID_tsv)
        print(f'TNID Dictionary : {TNID_Dic}')
    else:
        print('-TN', '--TNIDtsv')

### 04.MAKE "TNID DICTIONARY" with TNID tsv ###
    if args.TBD_Folder:
        TBD_ID = find_Project(args.TBD_Folder)
        print(TBD_ID)
    else:
        print('-TBD', "--TBD_folder")
