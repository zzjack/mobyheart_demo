from app_mobyheart.controls.control_manager import manager
from app_mobyheart.models import RegisterModel,CreatedModels

def extarct_data()->dict:
    obj = manager.make_obj()
    data = RegisterModel.objects.exclude(created_link='')
    for d in data:
        obj['arr_dict'].append(
            {
                'model_name':d.model_name,
                'id':d.id,
                'created_link':d.created_link,
                'status':d.status,
                'start':d.start,
                'stop':d.stop,
            }
        )
        obj['arr_arr'].append([d.id,d.model_name,d.created_link,d.status,d.start,d.stop])
    return obj


class model_runner:

    def __init__(self,request):
        self.request = request

    def get_model_name(self)->str:
        splited = self.request.path.splite('/')
        model_name = splited[-1] if splited[-1] not in ['/',' ',''] else splited[-2]
        return model_name

    def load_model_config(self)->CreatedModels:
        n = self.get_model_name()
        conf =  CreatedModels.objects.filter(model_name=n)
        if len(conf) == 0:
            raise Exception(f'This model{n} do not have config;Check table CreatedModels more details')
        return conf





