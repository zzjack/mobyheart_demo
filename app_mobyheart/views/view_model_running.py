from django.http import JsonResponse

from app_mobyheart.controls import control_model_running
from risk_model.settings import logger

def display_model_links(request):
    data = []
    msg = 'function display_model_links {}'
    try:
        data = control_model_running.extarct_data()
        status = 'success'
        logger.info(msg.format(status))
    except:
        status = 'failed'
        logger.error(msg.format(status),exc_info = True)
    return JsonResponse(data, safe=False)

def run_model(request):
    try:
        pass
    except:
        pass