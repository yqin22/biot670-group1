#Import libraries
from tkinter import *
import webbrowser
from tkinter import filedialog
from tkinter.filedialog import askopenfile, TOP,askopenfilename

root=Tk()
root.title("Gene Fusion Viewer")


#Cereate the frame for the menubar
frame= LabelFrame(root, padx=5,pady=5)
frame.grid(row=1, column=1, padx=10, pady=10, sticky='news', rowspan=2)

#Just a dummy function for the menu buttons until actual functions are created
def donothing():
   filewin = Toplevel(frame)
   button = Button(filewin, text="Do nothing button")
   button.pack()

#function to open file
def open_file():
    file = askopenfile(mode='r', filetypes=[('Python Files', '*.BAM')])
    if file is not None:
       content = file.read()
       print(content)


    btn = Button(root, text='Import BAM File', command=lambda: open_file())
    btn.pack()


#Function to open the bam file from Url
def openweb():
    link = Entry(root,width=100, borderwidth=5)
    webbrowser.open(link.get())

    Btn = Button(root, command=openweb)
    Btn.pack()
    

  
    

   
#Creating the menubar
menubar = Menu(frame)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Load from File", command=open_file)
filemenu.add_command(label="Load from Url", command=openweb)
filemenu.add_command(label="New Session", command=donothing)
filemenu.add_command(label="Open Session", command=donothing)
filemenu.add_command(label="Save Session", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Rename", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Load Genomes from File", command=donothing)
editmenu.add_command(label="Load Genomes from URL", command=donothing)

menubar.add_cascade(label="Genomes", menu=editmenu)
tracksmenu=Menu(menubar,tearoff=0)

tracksmenu.add_command(label="Sort Tracks", command=donothing)
tracksmenu.add_command(label="Group Tracks", command=donothing)
tracksmenu.add_command(label="Filter Tracks", command=donothing)
tracksmenu.add_command(label="Overlay Data", command=donothing)


tracksmenu.add_separator()

tracksmenu.add_command(label="Fit Data to Window", command=root.quit)
menubar.add_cascade(label="Tracks", menu=tracksmenu)

regionmenu = Menu(menubar, tearoff=0)
regionmenu.add_command(label="Navigator", command=donothing)
regionmenu.add_command(label="Gene list", command=donothing)
menubar.add_cascade(label="Region", menu=regionmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=help)
helpmenu.add_command(label="About...", command=help)
menubar.add_cascade(label="Help", menu=helpmenu)

frame2= LabelFrame(root, padx=5,pady=5)
frame2.grid(row=1, column=1, padx=0, pady=10, sticky='news')

# The help and about file.  Still working on this
def help():
   filename= askopenfilename("About.txt")
   f= open(filename)
   text=f.read  
   print (text)

# Create the genome menu
tkvar = StringVar(frame2)
 # List with options
choices = [ 'Human (hg38)','Human (hg19)','more...' ]
popupMenu = OptionMenu(frame2, tkvar, *choices)
popupMenu.grid(row = 2, column =1,columnspan=3, sticky=W+E)
tkvar.set('Human(hg38)') # set the default option

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

# Create the dropdown menu for chromosomes
tchromosome = StringVar(frame2)
 # List with options
chromo_choice= [ 'All','chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9',
                'chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19',
                'chr20','chr21','chr22','chrX','chrY','chrM' ]
popupMenu = OptionMenu(frame2, tchromosome, *chromo_choice)
popupMenu.grid(row = 2, column =5,columnspan=5)
tchromosome.set('All') # set the default option

# on change dropdown value
def change_dropdown(*args):
    print( tchromosome.get() )

# link function to change dropdown
tchromosome.trace('w', change_dropdown)

#Create Search box and define  search function. This takes the user
#text input and search asginst the two genes in the 'text' list.
fram = Frame(root) 
Label(fram,text='Find Gene:').pack(side=LEFT)  
edit = Entry(fram)  
edit.pack(side=LEFT, fill=BOTH, expand=1)  
edit.focus_set()  
butt = Button(fram, text='Go')   
butt.pack(side=RIGHT)  
fram.grid(row = 1, column =10,columnspan=5)
  
  
#text = Text(root)  
#text.insert('1.0','''Type your text here''')  
#text.grid(row = 2, column =15,columnspan=5) 
text= ['park7', 'ACADM','ABCA1']
  
  
  
def find(): 
      
    text.tag_remove('found', '1.0', END)  
    s = edit.get()  
    if s: 
        idx = '1.0'
        while 1: 
            idx = text.search(s, idx, nocase=1,  
                              stopindex=END)  
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))  
            text.tag_add('found', idx, lastidx)  
            idx = lastidx 
    text.tag_config('found', foreground='red')
edit.focus_set() 
butt.config(command=find)

#Create the display box
frame3 = Frame(root,width = 1024, height = 768)
frame3.grid(row = 4, column =1,columnspan=5)
#scrollbar = Scrollbar(frame3, orient='horizontal')
#scrollbar.grid(row=20, column=1)

frame4 = Frame(root,width = 1024, height = 768)
frame4.grid(row = 4, column =10,columnspan=5)
#scrollbar2 = Scrollbar(frame4, orient='horizontal')
#scrollbar2.grid(row=5, column=20 )

#Test images to view scrool and zoom function
Image1 = PhotoImage(file = "fusion_1.png")
Image1_Pack = Label(frame3, image = Image1)
Image1_Pack.grid()

Image2 = PhotoImage(file = "fusion_2.png")
Image2_Pack =Label(frame4, image = Image2)
Image2_Pack.grid()


root.config(menu=menubar)

root.mainloop()