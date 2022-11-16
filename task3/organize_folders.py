"""create and organize files from data folder"""
import os
def read_list(file):
    """read the list from students.cvs"""
    with open(file,'r',encoding="utf-8") as csv:
        register= csv.readlines()
        register= register[1:]
    return register
def create_folders(folder_name):
    """create folders acording to student list"""
    os.makedirs(folder_name,exist_ok=True)

def filter_files(folder_origin,key):
    """filter files from folder_origin acording to key criterial"""
    file_list=os.listdir(folder_origin)
    filter_file_list=[s for s in file_list if key in s]
    return filter_file_list 
def filter_folders(folder_origin):
    """filter the folders from origin"""
    file_list=os.listdir(folder_origin)
    filter_file_list=[s for s in file_list if os.path.isdir(f"{folder_origin}/{s}")]
    return filter_file_list
def move_files(list,origin_file,destination_file):
    """move files from a list from old to new direction"""
    for file_name in list:
        old = f"{cwd}/{origin_file}/{file_name}"
        new = f"{cwd}/{destination_file}/{file_name}"
        os.renames(old,new)
#======================================================================================
folder_names=read_list('students.csv')#['Telma Rios,14\n', 'Games,15\n',...
for name in folder_names:
    folder_name =name.split(",")[0]
    create_folders(folder_name)
cwd=os.getcwd()
pdf_files=filter_files("data",".pdf")#f"{os.getcwd()}/data"
game_folders=filter_folders("data")
move_files(game_folders,"data","Games")
move_files(pdf_files,"data","Tutorials")
