import PIL
import tkinter.filedialog
files_list=tkinter.filedialog.askopenfilenames()
for file in files_list:
    print(file)