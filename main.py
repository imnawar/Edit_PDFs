# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog
#Import the required Libraries
from PyPDF2 import PdfWriter, PdfReader
# Function for opening the
# file explorer window
def browseFiles():
	# The file to be signed 
	filename1 = filedialog.askopenfilename(
										title = "اختر الملف المراد ختمه",
										filetypes = (("PDF files",
														"*.pdf*"),
													("all files",
														"*.*")))
	
	# Signature file
	filename2 = filedialog.askopenfilename(
										title = "اختر ملف الختم",
										filetypes = (("PDF files",
														"*.pdf*"),
													("all files",
														"*.*")))
	
	# Make an object to read the pdf file 
	reader = PdfReader(filename1)
	# Make an object to sign on the pdf 
	writer = PdfWriter()
	# Loop over all pdf file pages to sign 
	for index in range(reader.getNumPages()):
		# get each page content 
		content_page = reader.pages[index]
		mediabox = content_page.mediabox
		# read the sign pdf file as "STAMP"
		reader_stamp = PdfReader(filename2)
		image_page = reader_stamp.pages[0]
		# Signing
		image_page.merge_page(content_page)
		image_page.mediabox = mediabox
		# Save the signed page as a new file
		writer.add_page(image_page)
	# Save the final pdf after all pages are signed 
	saved_file = filename1.split('.')[0] + "_مع الختم " +'.pdf'
	with open(saved_file, "wb") as fp:
		writer.write(fp)
	window.destroy()
	
def main():																								
	# Create the root window
	window = Tk()

	# Set window title
	window.title('اضافة ختم على ملف الـ pdf')

	# Set window size
	window.geometry("680x200")

	#Set window background color
	window.config(background = "white")

	# Create a File Explorer label
	label_file_explorer = Label(window,
								text = "الرجاء اختيار الملف المراد ختمه اولًا \n ثم ملف الختم...",
								width = 100, height = 4,
								fg = "blue")

		
	button_explore = Button(window,
							text = "اختيار الملف ثم الختم ",
							command = browseFiles)

	label_file_explorer.grid(column = 1, row = 1)

	button_explore.grid(column = 1, row = 2)

	window.mainloop()


if __name__ == "__main__":
    main()
