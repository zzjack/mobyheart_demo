from django.db import models

# Create your models here.

class ModelAllItems(models.Model):
    num = models.IntegerField("num")
    item = models.CharField(db_column="item",max_length=500)
    status = models.CharField(db_column="status",max_length=10)
    class Meta:
        db_table = "riskmodel_model_all_items"

class RegisterModel(models.Model):
    model_name = models.CharField(db_column="model_name",max_length=50)
    relation_nums = models.CharField(db_column="relation_nums",max_length=500)
    created_table = models.CharField(db_column='created_table',max_length=100)
    created_link = models.CharField(db_column='created_link',max_length=50)
    auth = models.CharField(db_column="auth",max_length=50)
    status = models.CharField(db_column="status", max_length=10)
    start = models.CharField(db_column='start',max_length=20)
    stop = models.CharField(db_column='stop', max_length=20)
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "riskmodel_rigister_model"

class ModelDetailsConfig(models.Model):
    item_num = models.CharField(db_column="item_num",max_length=30)
    # 1_0 1_1 / boolean
    item_detail_num = models.CharField(db_column="item_detail_num",max_length=30)
    item_content = models.CharField(db_column="item_content",max_length=300)
    # date/basic/min/max
    config_date = models.CharField(db_column="config_date",max_length=20)
    config_basic = models.CharField(db_column="config_basic",max_length=20)
    config_min = models.CharField(db_column="config_min",max_length=20)
    config_max = models.CharField(db_column="config_max",max_length=20)
    # the number of digit in item_num
    item_level = models.CharField(db_column="item_level",max_length=30)
    score = models.CharField(db_column="score",max_length=20)
    status = models.CharField(db_column="status", max_length=10)
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "riskmodel_model_details_config"


class CreatedModels(models.Model):
    model_name = models.CharField(db_column="model_name", max_length=50)
    item_num = models.CharField(db_column="item_num", max_length=30)
    # 1_0 1_1 / boolean
    item_detail_num = models.CharField(db_column="item_detail_num", max_length=30)
    item_content = models.CharField(db_column="item_content", max_length=300)
    # date/basic/min/max
    config_date = models.CharField(db_column="config_date", max_length=20)
    config_basic = models.CharField(db_column="config_basic", max_length=20)
    config_min = models.CharField(db_column="config_min", max_length=20)
    config_max = models.CharField(db_column="config_max", max_length=20)
    # the number of digit in item_num
    item_level = models.CharField(db_column="item_level", max_length=30)
    score = models.CharField(db_column="score", max_length=20)
    status = models.CharField(db_column="status", max_length=10)
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "riskmodel_created_models"
