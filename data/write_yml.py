import yaml

data={"key":{
    "keys01": {"e":{"value":"你好"},"value":"你好"},
    "keys02": {"e":[4,5,6],"value":456}
}}

with open("./ww.yaml","w",encoding="utf-8")as f:
    yaml.safe_dump(data,f,encoding="utf-8",allow_unicode=True)