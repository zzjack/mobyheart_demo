import json
from django.db import transaction
from django.http import JsonResponse,HttpResponse

from app_mobyheart.models_about.model_model_list import models
from app_mobyheart.controls.control_model_list import control_model_list
from risk_model.settings import logger


def load_model_list(request):
    data = {}
    try:
        data = control_model_list.query_models()
        logger.info("function load_model_list success")
    except:
        logger.error("function load_model_list failed",exc_info=True)
    return JsonResponse(data, safe=False)

def display_model_settings(request):
    res = []
    msg = 'function display_model_setting {}'
    try:
        url = request.path
        control = control_model_list(url)
        res = control.display_details_config()
        status = 'success'
        logger.info(msg.format(status))
    except:
        status = 'failed'
        logger.error(msg.format(status),exc_info=True)
    return JsonResponse(res,safe=False)

def save_modified_model_settings(request):
    if request.method == 'POST':
        msg = "function modified_model {}"
        try:
            dumped = json.loads(request.body)
            model_name,model_data = [(k,v) for k,v in dumped.items()][0]
            m = models(model_name,model_data)
            with transaction.atomic():
                if m.has_existed_modified_table():
                    m.delete_old_data()
                    logger.info(f"delete old data of {model_name}")
                else:
                    m.update_register_model()
                    logger.info(msg.format('update register model success!'))
                m.insert_data()
            status = "success"
            logger.info(msg.format(status))
        except:
            status = "failed"
            logger.error(msg.format(status),exc_info = True)
        return HttpResponse(status)