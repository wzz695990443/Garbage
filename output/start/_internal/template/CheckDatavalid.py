import pandas as pd
from datetime import datetime

class Check_CompanyData:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.required_columns = ['no', 'name', 'valid_begin', 'valid_end', 'sys_cat', 'linkman1', 'ratecode', 'mobile', 'phone', 'fax', 'saleman', 'street']
    
    def check_columns_exist(self):
        missing_columns = [col for col in self.required_columns if col not in self.dataframe.columns]
        if missing_columns:
            print(f"Missing columns: {missing_columns}")
            return False
        return True
    
    def check_date_format(self, date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    
    def check_dates_valid(self):
        date_columns = ['valid_begin', 'valid_end']
        for col in date_columns:
            if not self.dataframe[col].apply(self.check_date_format).all():
                print(f"Invalid date format in column: {col}")
                return False
        return True
    
    def validate_data(self):
        if not self.check_columns_exist():
            return False
        if not self.check_dates_valid():
            return False
        return True

# 示例用法
if __name__ == "__main__":
    data = {
        'no': [1, 2],
        'name': ['Company A', 'Company B'],
        'valid_begin': ['2023-01-01', '2023-02-01'],
        'valid_end': ['2023-12-31', '2024-12-31'],
        'sys_cat': ['Cat A', 'Cat B'],
        'linkman1': ['John Doe', 'Jane Smith'],
        'ratecode': ['RC1', 'RC2'],
        'mobile': ['1234567890', '0987654321'],
        'phone': ['1112223333', '4445556666'],
        'fax': ['7778889999', '9998887777'],
        'saleman': ['Salesman A', 'Salesman B'],
        'street': ['Street A', 'Street B']
    }
    df = pd.DataFrame(data)
    validator = Check_CompanyData(df)
    is_valid = validator.validate_data()
    print(f"Data is valid: {is_valid}")