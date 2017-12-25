from app_mobyheart.models import CreatedModels,RegisterModel


class models:

    def __init__(self,model_name,model_data):
        self.model_name = model_name
        self.model_data = model_data

    def has_existed_modified_table(self)->bool:
        query = CreatedModels.objects.filter(model_name = self.model_name)
        if len(query) == 0:
            return False
        else:
            return True

    def insert_data(self):
        cm = []
        for model in self.model_data:
            cm.append(
                CreatedModels(
                    model_name= self.model_name,
                    item_num = model.get('item_num','empty'),
                    item_detail_num = model.get('item_detail_num','empty'),
                    item_content = model.get('item_content','empty'),
                    config_date = model.get('config_date','empty'),
                    config_basic = model.get('config_basic','empty'),
                    config_min = model.get('config_min','empty'),
                    config_max = model.get('config_max','empty'),
                    item_level = '2',
                    score = model.get('score','empty'),
                    status = '1',
                    )
            )
        CreatedModels.objects.bulk_create(cm)

    def delete_old_data(self):
        c = CreatedModels.objects.filter(model_name=self.model_name)
        c.delete()

    def update_register_model(self):
        link = '/mobyheart/model-running/' + self.model_name + '/'
        RegisterModel.objects.filter(model_name = self.model_name).update(created_table = self.model_name,created_link=link)

