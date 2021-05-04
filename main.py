from data_description import DataDescription
from data_input import DataInput
from imputation import Imputation
from download import Download
from categorical import Categorical
from feature_scaling import FeatureScaling

class Preprocessor:
    bold_text_start = "\033[1m"
    bold_text_end = "\033[0;0m"
    tasks = [
        '1. Data Description',
        '2. Handling NULL values',
        '3. Encoding Categorical Data',
        '4. Feature Scaling of the Dataset',
        '5. Download the Modified Dataset'
    ]
    data = 0
    def __init__(self):
        self.data = DataInput().inputFunction()
        print("\n\n" + self.bold_text_start + "MACHINE LEARNING PREPROCESSOR CLI" + self.bold_text_end + "\n\n")
    def removeTargetColumn(self):
        print("Columns\n")
        for column in self.data.columns.values:
            print(column, end = "  ")
        while(1):
            column = input("\nWhich is the target variable:[enter -1 to exit]  ").lower()
            if column == "-1":
                exit()
            choice = input("Are you sure?(y/n) ")
            if choice=="y" or choice=="Y":
                try:
                    self.data.drop([column], axis = 1, inplace = True)
                except KeyError:
                    print("No column present with this name. Try again......")
                    continue
                print("Done......")
                break
            else:
                print("Try again with the correct column name...")
        return
    def printData(self):
        print(self.data)
    def preprocessorMain(self):
        self.removeTargetColumn()
        while(1):
            print("\nTasks (Preprocessing)\n")
            for task in self.tasks:
                print(task)
            while(1):
                try:
                    choice = int(input("\nWhat do you want to do? [enter -1 to exit]:  "))
                except ValueError:
                    print("Integer Value required. Try again.....")
                    continue
                break
            if choice == -1:
                exit()
            elif choice==1:
                DataDescription(self.data).describe()
            elif choice==2:
                self.data = Imputation(self.data).imputer()
            elif choice==3:
                self.data = Categorical(self.data).categoricalMain()
            elif choice==4:
                self.data = FeatureScaling(self.data).scaling()
            elif choice==5:
                Download(self.data).download()
            else:
                print("\nWrong choice!! Try again...")
obj = Preprocessor()
obj.preprocessorMain()