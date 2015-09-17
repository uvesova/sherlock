from django.contrib import admin

from .models import Typeobj, Slv, Param

# admin.site.register(Typeobj)
admin.site.register(Slv)
admin.site.register(Param)

@admin.register(Typeobj)
class TypeobjAdmin(admin.ModelAdmin):
	list_display = ("id_typeobj", "name_typeobj", "is_obj", "id_typeobj_1", "id_typeobj_2")

	def is_obj(self, obj):
		t = obj.is_obj_or_link
		if t == True:
			return "Связь"
		elif t == False:
			return "Основной"
		elif t == 2:
			return "Порождённый"
		else:
			return "Обобщённый"
	is_obj.short_description = 'Тип'
	
