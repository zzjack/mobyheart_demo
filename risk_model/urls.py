"""item_selection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app_mobyheart.views import view_item_selection as item_selection
from app_mobyheart.views import view_model_list as model_list
from app_mobyheart.views import view_model_running as model_running

from rest_framework import routers
from app_mobyheart.views import view_restful

router = routers.DefaultRouter()
router.register(r'users',view_restful.UserViewSet)
router.register(r'groups',view_restful.GroupViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',item_selection.index),
    url(r'^home/',item_selection.home),
    url(r'^mobyheart/regist-model/',item_selection.regist_model),
    url(r'^mobyheart/load-items/',item_selection.load_items),
    url(r'^mobyheart/is-unique-model-name/',item_selection.is_unique_model_name),
    url(r'^mobyheart/load-model-list/',model_list.load_model_list),
    url(r'^mobyheart/display-model-settings/',model_list.display_model_settings),
    url(r'^mobyheart/save-modified-model-settings/',model_list.save_modified_model_settings),
    url(r'^mobyheart/display-model-links/',model_running.display_model_links),
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework'))
    # url(r'^mobyheart/model-running/.+/$',),
]

