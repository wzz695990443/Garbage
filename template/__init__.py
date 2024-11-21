import FileProcessor

data = FileProcessor.ExcelFileProcessor('C:\\Users\\wzw\\AppData\\Roaming\\SQLyog\\Favorites\\02、协议单位迁移\\协议单位迁移模板.xlsx')
for i in data.get_data():
    print(i)