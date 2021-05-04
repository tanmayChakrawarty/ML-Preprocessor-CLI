import pandas as pd 
from data_description import DataDescription
class Imputation:
    bold_text_start = "\033[1m"
    bold_text_end = "\033[0;0m"
    tasks = [
        "\n1. Show number of NULL values",
        "2. Remove columns",
        "3. Fill NULL values (with Mean)",
        "4. Fill NULL values (with Median)",
        "5. Fill NULL values (with Mode)",
        "6. Show the dataset"
    ]
    def __init__(self, data):
        self.data = data
    def showColumns(self):
        print("\nColumns \n")
        for column in self.data.columns.values:
            print(column, end = "  ")
        return
    def printNullValues(self):
        print("\nNULL values of each column:")
        for column in self.data.columns.values:
            # isnull checks on each value of a column that whether the value is null or not.
            print('{0: <20}'.format(column) + '{0: <5}'.format(sum(pd.isnull(self.data[column]))))
        print("")
        return
    def removeColumn(self):
        self.showColumns()
        while(1):
            columns = input("\nEnter all the column"+ self.bold_text_start + "(s)" + self.bold_text_end + "you want to delete [enter -1 to go back]  ").lower()
            if columns == "-1":
                break
            choice = input("Are you sure?(y/n) ")
            if choice=="y" or choice=="Y":
                try:
                    self.data.drop(columns.split(" "), axis = 1, inplace = True)
                except KeyError:
                    print("One or more columns are not present. Try again.....")
                    continue
                print("Done..")
                break
            else:
                print("Not deleted..")
        return
    def fillNullWithMean(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name:[enter -1 to go back]  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mean())
                except KeyError:
                    print("Column is not present. Try again.....")
                    continue
                except TypeError:
                    # Imputation is only possible on some specific datatypes like int, float etc.
                    print("The Imputation is not possible here. Please try on another column.")
                    continue
                print("Imputation successful.....")
                break
            else:
                print("No change...")
        return
    def fillNullWithMedian(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name:[enter -1 to go back]  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].median())
                except KeyError:
                    print("Column is not present. Try again....")
                    continue
                except TypeError:
                    print("The Imputation is not possible here.Please try on another column.")
                    continue
                print("Imputation successful....")
                break
            else:
                print("No change...")
        return
    def fillNullWithMode(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name:[enter -1 to go back]  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mode()[0])
                except KeyError:
                    print("Column is not present. Try again....")
                    continue
                except TypeError:
                    print("The Imputation is not possible here. Please try on another column.")
                    continue
                print("Imputation successful....")
                break
            else:
                print("No change...")
        return
    def imputer(self):
        while(1):
            print("\nImputation Tasks")
            for task in self.tasks:
                print(task)
            while(1):
                try:
                    choice = int(input(("\nWhat you want to do? [enter -1 to go back]  ")))
                except ValueError:
                    print("Integer value required. Try again....")
                    continue
                break

            if choice == -1:
                break

            elif choice==1:
                self.printNullValues()

            elif choice==2:
                self.removeColumn()

            elif choice==3:
                self.fillNullWithMean()

            elif choice==4:
                self.fillNullWithMedian()
            
            elif choice==5:
                self.fillNullWithMode()

            elif choice==6:
                DataDescription.showDataset(self)

            else:
                print("\nWrong choice!! Try again..")
        return self.data