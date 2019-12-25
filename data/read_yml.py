import yaml

# 读取文件
with open("./value2.yaml", "r", encoding="utf_8")as f:
    # 加载yaml文件
    data = yaml.safe_load(f)

    print(data)
    print(type(data))

