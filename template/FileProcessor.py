"""

"""

import os
from abc import abstractmethod,ABC
import json
import configparser
import pandas as pd

class FileProcessorStrategy(ABC):
    """
    文件处理抽象类，定义了文件处理的基本方法
    """

    def __init__(self,file_path:str):
        self.filepath = file_path
        self.data = None
        # 检测路径是文件还是文件夹
        if os.path.isdir(self.filepath):
            raise ValueError(f"{self.filepath} 是一个文件夹，而不是文件")
        else:
            # 确保文件夹存在
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

        # 检测文件是否存在
        file_exists = os.path.exists(self.filepath)
        if not file_exists:
            with open(self.filepath, 'w') as file:
                pass

    @abstractmethod
    def write_file(self,data, mode:str = 'update'):
        pass

    @abstractmethod
    def get_data(self, *args, **kwargs):
        pass


class JsonFileProcessor(FileProcessorStrategy):
    """
    JSON文件处理类，继承自FileProcessor抽象类，实现处理JSON文件的方法
    """
    def write_file(self,data, mode:str = 'update'):
        if mode == 'update':
            with open(self.filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        elif mode == 'append':
            with open(self.filepath, 'a', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

    def get_data(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        return self.data


class ExcelFileProcessor(FileProcessorStrategy):
    """
    Excel文件处理类，继承自FileProcessor抽象类，实现读取Excel文件的方法
    """
    def write_file(self,data,mode:str = 'update'):
        pass

    def get_data(self, file_type:str = 'dict'):
        file = pd.read_excel(self.filepath)
        match file_type:
            case 'dict':
                return file.to_dict(orient='records')


class IniFileProcessor(FileProcessorStrategy):
    """
    ini文件处理类，继承自FileProcessor抽象类，实现读取ini文件的方法
    """
    def __init__(self,file_path:str):
        super().__init__(file_path)
        self.config = configparser.ConfigParser()

    def write_file(self,data = None,mode:str = 'update',section_name:str = None):
        self._set_section(section_name)
        if data is not None:
            if type(data) == dict:
                for key,value in data.items():
                    self.config.set(section_name,key,value)
        if mode == 'update':
            with open(self.filepath, 'w') as configfile:
                self.config.write(configfile)
        self.config.remove_section(section_name)

    def get_data(self):
        pass

    def _set_section(self,section_name:str = None):
        if not self.config.has_section(section_name):
            self.config.add_section(section_name)
            return True
        else:
            return False

class CsvFileProcessor(FileProcessorStrategy):
    """
    csv文件处理类，继承自FileProcessor抽象类，实现读取csv文件的方法
    """
    def write_file(self,data,mode:str = 'update'):
        pass
    def get_data(self, file_type:str = 'dict'):
        pass



class FileProcessor:
    """
    文件处理类，根据文件类型选择对应的处理器，并调用处理器的读取方法
    """
    def __init__(self,file_path:str):
        self.file_path = file_path
        self.file_type = self.file_path.split('.')[-1]

    def get_data(self):
        match self.file_type:
            case 'json':
                processor = JsonFileProcessor(self.file_path)
            case 'xlsx':
                processor = ExcelFileProcessor(self.file_path)
            case 'ini':
                processor = IniFileProcessor(self.file_path)
            case 'csv':
                processor = CsvFileProcessor(self.file_path)
            case _:
                raise ValueError(f"不支持的文件类型：{self.file_type}")

        return processor.get_data()

    def write_file(self,data,mode:str = 'update'):
        match self.file_type:
            case 'json':
                processor = JsonFileProcessor(self.file_path)
                processor.write_file(data,mode)
            case 'xlsx':
                processor = ExcelFileProcessor(self.file_path)
                processor.write_file(data,mode)
            case 'ini':
                processor = IniFileProcessor(self.file_path)
                processor.write_file(data,mode)
            case 'csv':
                processor = CsvFileProcessor(self.file_path)
                processor.write_file(data,mode)
            case _:
                raise ValueError(f"不支持的文件类型：{self.file_type}")