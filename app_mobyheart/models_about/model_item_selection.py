import json
from app_mobyheart.models import RegisterModel

def regist_model(loaded:dict):
    name = ""
    for n in loaded:
        name = n
    r = RegisterModel()
    r.model_name = name
    r.relation_nums = json.dumps(loaded[name])
    r.auth = loaded.get("auth","foo")
    r.save()

def is_unique(loaded:str)->bool:
    b = RegisterModel.objects.filter(model_name=loaded)
    if len(b) == 0:
        return True
    return False















