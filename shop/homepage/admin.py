from django.contrib import admin
from .models import HotDeal,Slider
from datetime import datetime, timezone

from django.utils.timezone import now
# Register your models here.

class PageAdminHotDeal(admin.ModelAdmin):
    def timedeal_display(self, obj):
        #c = datetime.(obj.end_deal-datetime.now(timezone.utc))
        if obj.end_deal > obj.start_deal:
            return obj.end_deal - datetime.now(timezone.utc)
        else:
            return 0
    list_display= ('product','available','timedeal_display')
admin.site.register(HotDeal,PageAdminHotDeal)
admin.site.register(Slider)