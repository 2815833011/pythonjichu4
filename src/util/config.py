
'''
这里封装的是 读取conf.yaml 文件内容 conf.yaml 文件是一个数据文件管理文件

yamlload.py只负责读取文件内容。config.py负责告诉 yamlload读取哪个文件
'''

from src.util.yamlload import YamlLoad
class Conf:
    def __init__(self):
        self.yaml=YamlLoad()
        self.conf="conf/conf.yaml"

    def get_driver_path(self,browser="chrome"):
        return self.yaml.fileload(self.conf)["chromedriver"][browser]
    
    def get_test_data(self,data_path,data_name):
        datapath=self.yaml.fileload(self.conf)["testdata"][data_path]
        return self.yaml.fileload(datapath)[data_name]