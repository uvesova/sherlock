from django.db import models
from django.db import connections

from collections import namedtuple

TABLESPACE = "k_0680"

# def namedtuplefetchall(cursor):
#     "Return all rows from a cursor as a namedtuple"
#     desc = cursor.description
#     nt_result = namedtuple('Result', [col[0] for col in desc])
#     return [nt_result(*row) for row in cursor.fetchall()]


# def get_types():
# 	with connections['cascade'].cursor() as c:
# 		c.execute("SELECT * FROM K_0680.TypeObj")
# 		return namedtuplefetchall(c)

"Объект учёта"
class Typeobj(models.Model):
    id_typeobj = models.IntegerField('№ объекта', primary_key=True)
    name_typeobj = models.CharField('Название', max_length=100)
    # is_obj_or_link = models.BooleanField('Тип')
    is_obj_or_link = models.IntegerField('Тип')
    id_levelaccess = models.IntegerField('Уровень доступа', blank=True, null=True)
    id_typeobj_1 = models.IntegerField('Связь из', blank=True, null=True)
    id_typeobj_2 = models.IntegerField('Связь в', blank=True, null=True)
    class Meta:
        managed = False
        db_table = '"K_0680"."TYPEOBJ"'
        verbose_name = "объект учёта или связь"
        verbose_name_plural = "объекты учёта и их связи"

    def __str__(self):
        return self.name_typeobj
"Словарь"
class Slv(models.Model):
    id_slv = models.FloatField(primary_key=True)
    name_slv = models.CharField(max_length=100)
    modified = models.BooleanField()
    class Meta:
        managed = False
        db_table = '"K_0680"."slv"'
        verbose_name = "словарь"
        verbose_name_plural = "словари"
    def __str__(self):
        return self.name_slv

"Параметр"
class Param(models.Model):
    id_param = models.IntegerField(primary_key=True)
    id_typeobj = models.IntegerField()
    #id_slv = models.FloatField(blank=True, null=True)
    id_slv = models.ForeignKey(Slv, db_column='id_slv', related_name='+', blank=True, null=True)
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=1)
    id_len = models.IntegerField(blank=True, null=True)
    mult = models.BooleanField()
    main = models.IntegerField(blank=True, null=True)
    id_group_param = models.IntegerField(blank=True, null=True)
    visible = models.BooleanField()
    id_levelaccess = models.IntegerField(blank=True, null=True)
    ord_main = models.IntegerField(blank=True, null=True)
    unical = models.BooleanField()
    analog = models.BooleanField()
    search = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = '"K_0680"."param"'
        verbose_name = "параметр"
        verbose_name_plural = "параметры"
    def __str__(self):
        # return "%d %s (тип %s)" % (self.id_param, self.name, self.type)
        return self.name