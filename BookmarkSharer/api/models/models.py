# This is an auto-generated Django models module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each models has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'label'


class Site(models.Model):
    name = models.CharField(max_length=255)
    base_url = models.CharField(max_length=255)
    click_num = models.IntegerField()
    status = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'site'


class SiteLabelRef(models.Model):
    site = models.ForeignKey(Site, models.DO_NOTHING)
    label = models.ForeignKey(Label, models.DO_NOTHING)
    create_time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'site_label_ref'


class User(models.Model):
    nick_name = models.CharField(max_length=64)
    avatar = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class UserClickLog(models.Model):
    site = models.ForeignKey(Site, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_click_log'


class UserLabelRef(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    label = models.ForeignKey(Label, models.DO_NOTHING)
    create_time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_label_ref'
