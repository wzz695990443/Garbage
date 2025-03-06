class DataPipeline:
    def __init__(self):
        self.processors = []  # 处理器列表

    def add_processor(self, processor):
        self.processors.append(processor)
        return self

    def __call__(self, data):
        for processor in self.processors:
            data = processor(data)  # 依次调用处理器
        return data


class DataProcessor:
    def __init__(self, name, transform_func):
        self.name = name  # 处理器名称
        self.transform = transform_func  # 数据处理函数

    def __call__(self, data):
        print(f"正在执行 {self.name} 处理")
        return self.transform(data)
