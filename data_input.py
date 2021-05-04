from os import path
import sys
import pandas as pd 
class DataInput:
    bold_text_start = "\033[1m"
    bold_text_end = "\033[0;0m"
    supported_file_extensions = [
        '.csv',
    ]
    def change_to_lower_case(self, data):
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace = True)
        return data
    def inputFunction(self):
        try:
            filename, file_extension = path.splitext(sys.argv[1])
            if file_extension == "":
                raise SystemExit(f"Provide the " + self.bold_text_start + "DATASET" + self.bold_text_end +" name (with extension).")
            if file_extension not in self.supported_file_extensions:
                raise SystemExit(f"This file extension is not " + self.bold_text_start + "supported." + self.bold_text_end)
        except IndexError:
            raise SystemExit(f"Provide the " + self.bold_text_start + "DATASET" + self.bold_text_end +" name (with extension).")
        try:
            data = pd.read_csv(filename+file_extension)
        except pd.errors.EmptyDataError:
            raise SystemExit(f"The file is "+ self.bold_text_start + "EMPTY" + self.bold_text_end)
        except FileNotFoundError:
            raise SystemExit(f"File " + self.bold_text_start + "doesn't" + self.bold_text_end)
        data = self.change_to_lower_case(data)
        return data