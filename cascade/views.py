from django.http import HttpResponse
from django.views.generic import View
from django.template import Template, RequestContext
from django.shortcuts import render
from django.db.models import Q

from django import forms

from .models import Typeobj, Param

def home(request):
    "Отображает список основных объектов учёта"
    main = Typeobj.objects.filter(is_obj_or_link=0)
    sibling = Typeobj.objects.filter(is_obj_or_link=2)
    context = RequestContext(request, {
        'main': main, 'sibling': sibling
        })
    return render(request, "index.html", context)

def params(request, obj):
    "Список параметров объекта учёта `obj`"
    params = Param.objects.filter(id_typeobj=obj).order_by('id_param')
    context = RequestContext(request, {
        'params': params,
        })
    return render(request, "params.html", context)


class QueryForm(forms.Form):
    def __init__(self, typeobj_id, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        params = Param.objects.filter(id_typeobj=typeobj_id).order_by('id_param')
        # self.fields['last_name'] = forms.CharField(max_length=20)
        for p in params:
            name = "p_%d" % p.id_param
            field = forms.CharField(max_length=20)
            if p.type == "T":
                field = forms.CharField(max_length=20)
            elif p.type == "I":
                field = forms.IntegerField()
            elif p.type == "D":
                field = forms.DateField()
            elif p.type == "S":
                field = forms.ChoiceField()
            elif p.type == "P":
                field = forms.FileField()
            field.label = p.name
            # field.widget_attrs({"class": "!!!!!!!!!!!!"})
            self.fields[name] = field

def query(request, obj):
    "Форма запроса на выбранный объект учёта `obj`"
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QueryForm(request.POST, {"typeobj_id":obj})
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QueryForm(typeobj_id=obj)

    return render(request, 'query.html', {'form': form})