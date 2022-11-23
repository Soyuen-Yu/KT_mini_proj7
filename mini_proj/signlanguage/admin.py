import json
from django.contrib import admin
from django.db.models import Count, F, FloatField, IntegerField
from django.db.models.functions import TruncDay, Cast
from django.core.serializers.json import DjangoJSONEncoder

# Register your models here.
from .models import Result, AiModel

# 관리에서 Result 객체에 대해  기본 CRUD 관리를 한다. 
admin.site.register(Result)
# admin.site.register(AiModel)

@admin.register(AiModel)
class AiModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "version", "is_using", "file", "created") # display these table columns in the list view
    ordering = ("-created",)   

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            AiModel.objects
            .values("name", "prediction_count", "answer_count")
            .annotate(x = F("name"))
            .annotate(y = Cast(Cast(F("answer_count"), FloatField()) / F("prediction_count") * 100, IntegerField() ) )
            .values("x", "y")
            .order_by("name")
        )

        line_data = (
            AiModel.objects
            .values("name",'prediction_count')
            .annotate(x=F("name"))
            .annotate(y=(Cast(F("answer_count"), IntegerField())))
            .values("x","y")
            .order_by("name")
        )
        
        print(list(chart_data))

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        as_json2 = json.dumps(list(line_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json, "line_data":as_json2}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)