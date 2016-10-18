#-------------------------------------------------------------------------------
# Name:        Image Metadata
# Purpose:     Program captures image metadata from user input in fields, and stores data in a list and writes to a CSV file
#
# Author:      Louise Brett
#
# Created:     23/09/2016
# Copyright:   (c) Louise Brett 2016
# Licence:     CC
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

from tkinter import *

bgc = '#a4d1ff'
fgc = 'black'
buttonc = 'whitesmoke'

import tkinter.messagebox

class Image:
    def __init__(self, imageid, filename, title, owner, location, licence):
        self.imageid = imageid
        self.filename = filename
        self.title = title
        self.owner = owner
        self.location = location
        self.licence = licence


    def get_imageid(self):
        return self.imageid

    def get_filename(self):
        return self.filename

    def get_title(self):
        return self.title

    def get_owner(self):
        return self.owner

    def get_location(self):
        return self.location

    def get_licence(self):
        return self.licence


class GUI:
    def __init__(self):

        window = Tk()
        window.title("Data Entry for Image Metadata")
        window.minsize(width=600, height=400)
        window.configure(background = bgc)

        heading_label = Label(window, bg=bgc, fg=fgc, text="Images", font=("Times","24"))
        heading_label.pack()

        self.recordlist = []

        imageid_label = Label(window, text='Image ID:', bg=bgc)
        imageid_label.pack(anchor="c")
        self.imageid_field = Entry(window)
        self.imageid_field.pack(anchor="c")

        filename_label = Label(window, text='Filename:', bg=bgc)
        filename_label.pack()
        self.filename_field = Entry(window)
        self.filename_field.pack()

        title_label = Label(window, text='Image Title:', bg=bgc)
        title_label.pack()
        self.title_field = Entry(window)
        self.title_field.pack()

        owner_label = Label(window, text='Owner:', bg=bgc)
        owner_label.pack()
        self.owner_field = Entry(window)
        self.owner_field.pack()

        location_label = Label(window, text='Location:', bg=bgc)
        location_label.pack()
        self.location_field = Entry(window)
        self.location_field.pack()

        #code for pulldown window
        licence_label = Label(window, text='Licence', bg=bgc)
        licence_label.pack()
        self.licence_field = StringVar()
        OptionMenu(window, self.licence_field, "CC0", "BY", "BY-SA", "BY-NC", "BY-ND", "BY-NC-SA", "BY-NC-ND").pack()


        csv_button_label = Label(window, text='Convert Record to csv', bg=bgc)
        csv_button_label.pack()

        button = Button(window, text='Write to csv', width = 8, command=self.writetocsv, bg = buttonc)
        button.pack(side="left", fill='none', expand=True, padx=1, pady=1)



        window.mainloop()


    def writetocsv(self):
        #To write the data (override previous data)
        import csv
        file_name = 'image_database.txt'

        ofile = open(file_name, 'w')
        writer = csv.writer(ofile, delimiter=',')
        for record in self.recordlist:
            print(record.get_imageid())
            writer.writerow([record.get_imageid(),record.get_filename(), record.get_title(), record.get_owner(), record.get_location(), record.get_licence()])
        ofile.close()
        tkinter.messagebox.showinfo('Notice',file_name+' File Generated Sucessfully')

        #Clearing fields after data has been writen to CSV file
        self.imageid_field.delete(0, END)
        self.filename_field.delete(0, END)
        self.title_field.delete(0, END)
        self.owner_field.delete(0, END)
        self.location_field.delete(0, END)



GUI()




