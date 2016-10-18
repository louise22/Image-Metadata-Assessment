#-------------------------------------------------------------------------------
# Name:        Image Metadata
# Purpose:     Program captures image metadata from user input in fields, and stores data in a list and writes to a CSV file
#              Enhanced to validate input so no fields are left blank
#              Enhanced to validate image id as an integer
#              Enhanced to include help information about the different licence types
#              Enhanced to add the option of writing or appending to csv file
#              Enhanced to include styles, and more functional layout
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

bgc = '#ccccff'
fgc = 'black'

import tkinter.messagebox
from tkinter.colorchooser import *

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
        window.title("Image Metadata Entry Form")
        window.minsize(width=250, height=310)
        window.configure(background = bgc)

        #Have used a grid layout because it is the most practical for my design
        #Creating space around the fields so everything is centred on GUI
        window.grid_rowconfigure(0, weight=0)
        window.grid_rowconfigure(12, weight=1)
        window.grid_columnconfigure(3, weight=1)
        window.grid_columnconfigure(0, weight=1)

        heading_label = Label(window, fg=fgc, text="Image Metadata", font=("Arial","18"))
        heading_label.grid(row=1, column=1, columnspan=2, pady=5)


        #Initialising variables
        self.ready_to_write = False
        self.noduplicatesrecordlist = []
        self.recordlist = []

        #Labels and entry fields
        imageid_label = Label(window, text='Image ID:')
        imageid_label.grid(row=2, column=1, sticky=E)
        self.imageid_field = Entry(window)
        self.imageid_field.grid(row=2, column=2)

        filename_label = Label(window, text='Filename:')
        filename_label.grid(row=3, column=1, sticky=E)
        self.filename_field = Entry(window)
        self.filename_field.grid(row=3, column=2)

        title_label = Label(window, text='Title:')
        title_label.grid(row=4, column=1, sticky=E)
        self.title_field = Entry(window)
        self.title_field.grid(row=4, column=2)

        owner_label = Label(window, text='Owner:')
        owner_label.grid(row=5, column=1, sticky=E)
        self.owner_field = Entry(window)
        self.owner_field.grid(row=5, column=2)

        location_label = Label(window, text='Location:')
        location_label.grid(row=6, column=1, sticky=E)
        self.location_field = Entry(window)
        self.location_field.grid(row=6, column=2)

        #code for pulldown window
        #Have used a dropdown menu so only one of the 6 options can be selected
        licence_label = Label(window, text='Licence:')
        licence_label.grid(row=7, column=1, sticky=E)
        self.licence_field = StringVar()
        global optionmenu   #Must be global so that highlightbackground can be changed when background colour is changed
        optionmenu = OptionMenu(window, self.licence_field, "CC0", "BY", "BY-SA", "BY-NC", "BY-ND", "BY-NC-SA", "BY-NC-ND")
        optionmenu.config(width=10,highlightbackground = bgc)
        optionmenu.grid(row=7, column=2, sticky=W)

        #Help button for licence info
        info_button = Button(window, text='?', command=self.licence_help)
        info_button.grid(row=7, column=2, sticky=E)

        submit_button = Button(window, text='Submit', command=self.doSubmit)
        submit_button.grid(row=8, column=2, sticky=W)

        csv_button_label = Label(window, text='Convert Record to CSV File')
        csv_button_label.grid(row=9, column=1, columnspan=2, pady=5)

        #User has option to either write or append data to CSV
        write_button = Button(window, text='Write', width = 8, command=self.writetocsv)
        write_button.grid(row=10, column=1, columnspan=2, sticky=W, padx=12)

        append_button = Button(window, text='Append', width = 8, command=self.appendtocsv)
        append_button.grid(row=10, column=1, columnspan=2, sticky=E, padx=12)

        bgchange_Button = Button(window, text='Choose Background Colour', command=lambda: self.getColor(window))
        bgchange_Button.grid(row=11, column=1, columnspan=2, pady=8)

        #To change label backgrounds when user selects background colour
        global labels
        labels = [heading_label, imageid_label, filename_label, title_label, owner_label, location_label, licence_label, csv_button_label]
        for i in labels:
            i.configure(bg = bgc)


        window.mainloop()

    def licence_help(self):
        #Gives info about licences in a messagebox
        info = 'CC0 = Freeing content globally without restrictions'+'\nBY = Attribution alone'+'\nBY-SA = Attribution + ShareAlike'+'\nBY-NC = Attribution + Noncommercial'+'\nBY-ND = Attribution + NoDerivatives'+'\nBY-NC-SA = Attribution + Noncommercial + ShareAlike'+'\nBY-NC-ND = Attribution + Noncommercial + NoDerivatives'
        tkinter.messagebox.showinfo('Licences',info)


    def getColor(self,parent):
        #Allows user to select background colour with the colourchooser
        color = colorchooser.askcolor()
        bgc = color[1]    #to pick up the color name in HTML notation, i.e. the 2nd element of the tuple returned by the colorchooser
        parent.configure(background = bgc) #change main background colour
        for i in labels: #change the background of labels
            i.configure(bg = bgc)
        optionmenu.config(highlightbackground = bgc) #change the background of the optionmenu


    def doSubmit(self):
        #test uniqueness of each image id entered
        noduplicate = True;
        for record in self.noduplicatesrecordlist:
            if self.imageid_field.get() == record.get_imageid():
                noduplicate= False
                tkinter.messagebox.showwarning('Warning!','Duplicate Image ID, Please Re-enter Image ID');
                print('Please enter image ID again');


        if noduplicate == True:
            #Ensuring there is a value entered in all fields
            if len(self.imageid_field.get()) <1 or len(self.filename_field.get()) <1 or len(self.title_field.get()) <1 or len(self.owner_field.get()) <1 or len(self.location_field.get()) <1 or len(self.licence_field.get()) <1:
                print('Enter a value for all fields')
                tkinter.messagebox.showwarning('Warning!','Please enter a value for all fields')

            else:
                try:
                    validated_imageid = int(self.imageid_field.get())#Ensuring imageid is an integer
                    self.noduplicatesrecordlist.append(Image(self.imageid_field.get(),self.filename_field.get(), self.title_field.get() , self.owner_field.get(), self.location_field.get(), self.licence_field.get()))
                    self.recordlist.append(Image(self.imageid_field.get(),self.filename_field.get(), self.title_field.get() , self.owner_field.get(), self.location_field.get(), self.licence_field.get()))
                    self.ready_to_write= True
                    print(self.filename_field.get(),'has been submitted')
                    tkinter.messagebox.showinfo('Notice','Submission Sucessful')

                    #Clearing fields after data has been submitted
                    self.imageid_field.delete(0, END)
                    self.filename_field.delete(0, END)
                    self.title_field.delete(0, END)
                    self.owner_field.delete(0, END)
                    self.location_field.delete(0, END)

                except:
                    tkinter.messagebox.showwarning('Warning!','Please enter numeric image ID')
                    print('Please enter numeric image ID')



    def writetocsv(self):
        #To write the data (override previous data)
        import csv
        file_name = 'image_database.txt'

        if self.ready_to_write: #checks data has been previously validated
            ofile = open(file_name, 'w')
            writer = csv.writer(ofile, delimiter=',')
            print('Submitted records written to csv')
            for record in self.recordlist:
                writer.writerow([record.get_imageid(),record.get_filename(), record.get_title(), record.get_owner(), record.get_location(), record.get_licence()])
            ofile.close()
            tkinter.messagebox.showinfo('Notice',file_name+' File Generated Sucessfully')
        else:
            tkinter.messagebox.showwarning('Error!', 'Please validate data')

        self.ready_to_write= False
        self.recordlist = []

    def appendtocsv(self):
        #To append the data (add to previous data)
        import csv
        file_name = 'image_database.txt'

        if self.ready_to_write: #cheacks data has been previously validated
            ofile = open(file_name, 'a')
            writer = csv.writer(ofile, delimiter=',')
            print('Submitted records appended to csv')
            for record in self.recordlist:
                writer.writerow([record.get_imageid(),record.get_filename(), record.get_title(), record.get_owner(), record.get_location(), record.get_licence()])
            ofile.close()
            tkinter.messagebox.showinfo('Notice',file_name+' File Generated Sucessfully')
        else:
            tkinter.messagebox.showwarning('Error!', 'Please validate data')

        self.ready_to_write= False
        self.recordlist = []


GUI()




