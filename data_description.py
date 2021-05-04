import pandas as pd 
class DataDescription:
    tasks = [
        '\n1. Describe a specific column',
        '2. Show properties of each column',
        '3. Show the dataset'
    ]
    def __init__(self, data):
        self.data = data
    def showDataset(self):
        while(1):
            try:
                rows = int(input(("\nHow many rows(>0) to print? [enter -1 to go back]  ")))
                if rows == -1:
                    break
                if rows <= 0:
                    print("Number of rows given must be +ve...")
                    continue
                print(self.data.head(rows))
            except ValueError:
                print("Enter a valid numeric value. Try again....")
                continue
            break
        return
    def showColumns(self):
        for column in self.data.columns.values:
            print(column, end="  ")
    def describe(self):
        while(1):
            print("\nTasks [Data Description]")
            for task in self.tasks:
                print(task)
            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? [enter -1 to go back]  ")))
                except ValueError:
                    print("Enter a valid numeric value. Try again....")
                    continue
                break
            if choice==-1:
                break
            elif choice==1:
                self.showColumns()
                while(1):
                    describeColumn = input("\n\nWhich Column?  ").lower()
                    try:
                        print(self.data[describeColumn].describe())
                    except KeyError:
                        print("No column present with this name. Try again...")
                        continue
                    break
            elif choice==2:
                print(self.data.describe())
                print("\n\n")
                print(self.data.info())
            elif choice==3:
                self.showDataset()
            else:
                print("\nWrong choice!! Try again..")