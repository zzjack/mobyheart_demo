import json
from app_mobyheart.models import RegisterModel
from app_mobyheart.models import ModelDetailsConfig,CreatedModels
from risk_model.settings import logger
from app_mobyheart.controls.control_manager import manager

class control_model_list:
    def __init__(self,url):
        self.url = url

    def extract_model_id(self)->str:
        splited = self.url.split("/")
        if self.url[-1] == "/":
            model_id = splited[-2]
        else:
            model_id = splited[-1]
        return model_id

    def extracted_is_int(self,model_id)->bool:
        try:
            model_id = int(model_id)
            return True
        except:
            logger.error(f"function display_details_config model_id {model_id} is not int that is illgeal")
            return False

    def select_from_created_models(self,created)->list:
        details_config = []
        for c in created:
            details_config.append(
                {
                    "item_num": c.item_num,
                    "item_detail_num": c.item_detail_num,
                    "item_content": c.item_content,
                    "config_date": c.config_date,
                    "config_basic": c.config_basic,
                    "config_min": c.config_min,
                    "config_max": c.config_max,
                    "score": c.score,
                }
            )
        return details_config

    def select_from_register_model(self,reg_model)->list:
        details_config = []
        item_nums = reg_model[0].relation_nums
        jsoned = json.loads(item_nums)
        for num in jsoned:
            filtered = ModelDetailsConfig.objects.filter(item_num=num)
            if len(filtered) == 0:
                raise Exception("function display_details_config is empty")
            for f in filtered:
                details_config.append(
                    {
                        "item_num": f.item_num,
                        "item_detail_num": f.item_detail_num,
                        "item_content": f.item_content,
                        "config_date": f.config_date,
                        "config_basic": f.config_basic,
                        "config_min": f.config_min,
                        "config_max": f.config_max,
                        "score": f.score,
                    }
                )
        return details_config

    def display_details_config(self)->list:
        details_config = []
        model_id = self.extract_model_id()
        if self.extracted_is_int(model_id) == False:
            return details_config

        reg_model = RegisterModel.objects.filter(id=model_id)
        if len(reg_model) == 0:
            logger.error("function display_details_config len(reg_model) == 0")
            return details_config

        model_name = reg_model[0].model_name
        created = CreatedModels.objects.filter(model_name=model_name)
        if len(created) > 0:
            details_config = self.select_from_created_models(created)
        else:
            details_config = self.select_from_register_model(reg_model)
        return details_config

    @staticmethod
    def query_models():
        obj = manager.make_obj()
        models = RegisterModel.objects.all()
        for m in models:
            obj['arr_dict'].append({'id': m.id, 'model_name': m.model_name, 'auth': m.auth})
            obj['arr_arr'].append([m.id,m.model_name,m.auth])
        return obj


