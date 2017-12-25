import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from risk_model.settings import logger
from app_mobyheart.models_about import model_item_selection
from app_mobyheart.models import ModelAllItems

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request:str):
    return render(request,'home.html')

def regist_model(request):
    if request.method == "POST":
        try:
            loaded = json.loads(request.body)
            model_item_selection.regist_model(loaded)
            logger.info(f"create_model success")
            return HttpResponse("success")
        except:
            logger.error("function create_model:",exc_info=True)
            return HttpResponse("failed")

def load_items(request):
    t = []
    try:
        items = ModelAllItems.objects.all()
        for i in items:
            t.append([i.num,i.item])
        logger.info("load_model_all_items success")
    except:
        logger.error("function load_model_all_items failed",exc_info=True)
    return JsonResponse(t, safe=False)

def is_unique_model_name(request):
    t = ""
    if request.method == "POST":
        try:
            loaded = json.loads(request.body)
            t = json.dumps(model_item_selection.is_unique(loaded))
        except:
            logger.error("function is_unique_model_name",exc_info=True)
    return JsonResponse(t,safe=False)




