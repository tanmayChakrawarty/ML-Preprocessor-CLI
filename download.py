import pandas as pd 
class Download:
    bold_text_start = "\033[1m"
    bold_text_end = "\033[0;0m"
    def __init__(self, data):
        self.data = data
    def download(self):
        toDownload = {}
        for column in self.data.columns.values:
            toDownload[column] = self.data[column]
        newFileName = input("\nEnter the " + self.bold_text_start +"FILENAME" + self.bold_text_end +" you want? [enter -1 to go back]:  ")
        if newFileName=="-1":
            return
        newFileName = newFileName + ".csv"
        pd.DataFrame(self.data).to_csv(newFileName, index = False)
        print("Task completed....")
        if input("Do you want to exit now? (y/n) ").lower() == 'y':
            print("Exiting...")
            exit()
        else:
            return