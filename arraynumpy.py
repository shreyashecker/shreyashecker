import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd 


class menudriven(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Menu Driven")
        self.window.geometry("800x800")
        self.window.resizable(False, False)
        self.window.configure(background="light blue")
        self.frame = tk.Frame(self.window)
        self.frame.configure(background="light blue")
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.label = ttk.Label(self.frame, text="WELCOME TO EXPLORER  ", font=("calibri bold", 10), background="light blue")
        self.label.place(x=200, y=50)
        self.labelintro = ttk.Label(self.frame, text="FIND ALL THE EXAMPLES RELATED TO VARIOUS OPERATIONS ON ARRAYS AND IRIS DATA", font=("calibri bold", 10), background="light blue")
        self.labelintro.place(x=200, y=100)
        self.labelintro2 = ttk.Label(self.frame, text="THIS APPLICATION CONTAINS \n BASIC OPERATION ON ARRAY \n MATHEMATICAL OPERATIONS ON ARRAY \n STATISTICAL OPERATIONS ON ARRAY \n OPERATIONS ON IRIS DATA", font=("calibri bold", 10), background="light blue")
        self.labelintro2.place(x=200, y=150)

       
        self.combobox1 = ttk.Combobox(self.frame, values=["Play with Files", "Play with arrays"], width=40)
        self.combobox1.place(x=200, y=250)
        self.combobox1.set("Choose an option")
        self.proceedbutton = ttk.Button(self.frame, text="PROCEED", command=self.decidefunction)
        self.proceedbutton.place(x=200, y=300)

        self.arr1d = np.array([1, 2, 3, 4, 5])
        self.arr2d = np.array([[1, 2, 3], [4, 5, 6]])
        self.arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

        self.data = np.array([10, 20, 30, 40, 50])
        self.erroroutput = ttk.Label(self.frame, text="", font=("calibri bold", 10), background="light blue")


        self.decidefunction()

    def decidefunction(self):
        option = self.combobox1.get()
        if option == "Play with Files":
            self.fileintro()
        elif option == "Play with arrays":
            self.mainscreen()
        else:
            self.erroroutput.configure(text="Invalid option selected")

    def fileintro(self):
        self.labelintro.destroy()
        self.combobox1.destroy()
        self.proceedbutton.destroy()
        self.labelintro2.destroy()
        self.label1 = ttk.Label(self.frame, text="Choose an option", font=("calibri bold", 10), background="light blue")
        self.label1.place(x=200, y=100)
        self.combobox = ttk.Combobox(self.frame, values=["group data by species", "Calculate mean, min, and max of Sepal length", "Remove rows containing missing value", "fill missing values with mean", "display columns name"], width=40)
        self.combobox.place(x=200, y=150)
        self.combobox.set("Choose an option")
        self.combobox.bind("<<ComboboxSelected>>", self.filelogic)
        self.output = ttk.Label(self.frame, text="Output will be displayed here", font=("calibri bold", 10), background="light blue")
        self.output.place(x=200, y=200)

    def filelogic(self, event):
        option = self.combobox.get()
        url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
        df = pd.read_csv(url)
        if option == "group data by species":
            grouped = df.groupby("species").size()
            self.output.configure(text="The data grouped by species is\n" + str(grouped))
            
        elif option == "Calculate mean, min, and max of Sepal length":
            self.output.configure(text="Mean of Sepal length is " + str(df["sepal_length"].mean()) + "\nMin of Sepal length is " + str(df["sepal_length"].min()) + "\nMax of Sepal length is " + str(df["sepal_length"].max()))
        elif option == "Remove rows containing missing value":
            df_cleaned = df.dropna()
            self.output.configure(text="The data after removing rows with missing values is\n" + str(df_cleaned.head(8)))

        elif option == "fill missing values with mean":
            df_filled = df.fillna(df.mean(numeric_only=True))
            self.output.configure(text="The data after filling missing values with mean is\n" + str(df_filled.head(8)))

        elif option == "display columns name":
            self.output.configure(text="The column names are\n" + str(df.columns))
        else:
            self.output.configure(text="Invalid option selected")


    def mainscreen(self):
        self.labelintro.destroy()
        self.combobox1.destroy()
        self.proceedbutton.destroy()
        self.labelintro2.destroy()
        self.frame2 = tk.Frame(self.window)
        self.frame2.configure(background="light blue")
        self.frame2.place(x=0, y=0, relwidth=1, relheight=1)

        self.label1 = ttk.Label(self.frame2, text="Choose an option", font=("calibri bold", 10), background="light blue")
        self.label1.place(x=200, y=100)
        self.combobox = ttk.Combobox(self.frame2, values=["print", "reshaped", "sliced", "indexing", "ADD ARRAY", "SUBTRACT ARRAY", "MULTIPLY ARRAY", "DIVIDE ARRAY", "DOT PRODUCT", "CROSS PRODUCT", "MEAN", "MEDIAN", "STANDARD DEVIATION", "VARIENCE", "CORRELATION COEEFICIENT"], width=40)
        self.combobox.place(x=200, y=150)
        self.combobox.set("Choose an option")
        self.combobox.bind("<<ComboboxSelected>>", self.logic)
        self.output = ttk.Label(self.frame2, text="Output will be displayed here", font=("calibri bold", 10), background="light blue")
        self.output.place(x=200, y=200)

    def logic(self, event):
        option = self.combobox.get()
        if option == "print":
            self.print()
        elif option == "reshaped":
            self.reshaped()
        elif option == "sliced":
            self.sliced()
        elif option == "indexing":
            self.indexing()
        elif option == "ADD ARRAY":
            self.add()
        elif option == "SUBTRACT ARRAY":
            self.subtract()
        elif option == "MULTIPLY ARRAY":
            self.multiply()
        elif option == "DIVIDE ARRAY":
            self.divide()
        elif option == "DOT PRODUCT":
            self.dotproduct()
        elif option == "CROSS PRODUCT":
            self.crossproduct()
        elif option == "MEAN":
            self.mean()
        elif option == "MEDIAN":
            self.median()
        elif option == "STANDARD DEVIATION":
            self.standarddeviation()
        elif option == "VARIENCE":
            self.varience()
        elif option == "CORRELATION COEEFICIENT":
            self.correlationcoeefficient()
        else:
            self.output.configure(text="Invalid option selected")

    def print(self):
        self.output.configure(text="1d array is\n" + str(self.arr1d) + "\n2d array is\n" + str(self.arr2d) + "\n3d array is\n" + str(self.arr3d))

    def reshaped(self):
        reshapedarr1d = self.arr1d.reshape(5, 1)
        reshapedarr2d = self.arr2d.reshape(3, 2)
        reshapedarr3d = self.arr3d.reshape(2, 3, 2)
        self.output.configure(text="reshaped 1d array is\n" + str(reshapedarr1d) + "\nreshaped 2d array is\n" + str(reshapedarr2d) + "\nreshaped 3d array is\n" + str(reshapedarr3d))

    def sliced(self):
        slicingarr1d = self.arr1d[1:4]
        slicingarr2d = self.arr2d[1, 1]
        slicingarr3d = self.arr3d[1, 1, 1]
        self.output.configure(text="sliced 1d array is\n" + str(slicingarr1d) + "\nsliced 2d array is\n" + str(slicingarr2d) + "\nsliced 3d array is\n" + str(slicingarr3d))

    def indexing(self):
        indexingarr1d = self.arr1d[2]
        indexingarr2d = self.arr2d[1, 2]
        indexingarr3d = self.arr3d[1, 1, 2]
        self.output.configure(text="indexed 1d array is\n" + str(indexingarr1d) + "\nindexed 2d array is\n" + str(indexingarr2d) + "\nindexed 3d array is\n" + str(indexingarr3d))

    def add(self):
        arr1 = np.array([1, 2, 3, 4, 5])
        arr2 = np.array([6, 7, 8, 9, 10])
        arr3 = arr1 + arr2
        self.output.configure(text=f"The sum of {arr1} and {arr2} is " + str(arr3))

    def subtract(self):
        arr1 = np.array([1, 2, 3, 4, 5])
        arr2 = np.array([6, 7, 8, 9, 10])
        arr3 = arr1 - arr2
        self.output.configure(text=f"The difference of {arr1} and {arr2} is " + str(arr3))

    def multiply(self):
        arr1 = np.array([1, 2, 3, 4, 5])
        arr2 = np.array([6, 7, 8, 9, 10])
        arr3 = arr1 * arr2
        self.output.configure(text=f"The product of {arr1} and {arr2} is " + str(arr3))

    def divide(self):
        arr1 = np.array([1, 2, 3, 4, 5])
        arr2 = np.array([6, 7, 8, 9, 10])
        arr3 = arr1 / arr2
        self.output.configure(text=f"The division of {arr1} and {arr2} is " + str(arr3))

    def dotproduct(self):
        arr1 = np.array([1, 2, 3, 4, 5])
        arr2 = np.array([6, 7, 8, 9, 10])
        arr3 = np.dot(arr1, arr2)
        self.output.configure(text=f"The dot product of {arr1} and {arr2} is " + str(arr3))

    def crossproduct(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        arr3 = np.cross(arr1, arr2)
        self.output.configure(text=f"The cross product of {arr1} and {arr2} is " + str(arr3))

    def mean(self):
        self.datalabel = ttk.Label(self.frame2, text=f"THE DATA IS {self.data}", font=("calibri bold", 10), background="light blue")
        self.datalabel.place(x=200, y=180)
        self.output.configure(text="The mean of the array is " + str(np.mean(self.data)))

    def median(self):
        self.datalabel = ttk.Label(self.frame2, text=f"THE DATA IS {self.data}", font=("calibri bold", 10), background="light blue")
        self.datalabel.place(x=200, y=180)
        self.output.configure(text="The median of the array is " + str(np.median(self.data)))

    def standarddeviation(self):
        self.datalabel = ttk.Label(self.frame2, text=f"THE DATA IS {self.data}", font=("calibri bold", 10), background="light blue")
        self.datalabel.place(x=200, y=180)
        self.output.configure(text="The standard deviation of the array is " + str(np.std(self.data)))

    def varience(self):
        self.datalabel = ttk.Label(self.frame2, text=f"THE DATA IS {self.data}", font=("calibri bold", 10), background="light blue")
        self.datalabel.place(x=200, y=180)
        self.output.configure(text="The varience of the array is " + str(np.var(self.data)))

    def correlationcoeefficient(self):
        arr1 = np.array([1, 2, 3, 4, 5])
        arr2 = np.array([6, 7, 8, 9, 10])
        arr3 = np.corrcoef(arr1, arr2)
        self.output.configure(text=f"The correlation coefficient of {arr1} and {arr2} is " + str(arr3))


if __name__ == "__main__":
    app = menudriven()
    app.window.mainloop()
