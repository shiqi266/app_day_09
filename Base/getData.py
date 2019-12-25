import os

import yaml


class Gget():
    # 解析文件
    # def get_yml(self,name):
    #     # 读n os.sep:获取系统路径分隔符
    #     with open("./data" + os.sep + name, "r", encoding="utf-8")as f:
    #         return yaml.safe_load(f)

    def a_get(self,name):
        with open("./data" +os.sep+name,"r",encoding="utf-8")as f:
            return yaml.safe_load(f)