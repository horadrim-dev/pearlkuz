from django.contrib import admin

# Register your models here.
from .forms import AdminMenuForm
from .models import Menu


# @admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    # }
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            kwargs['form'] = AdminMenuForm
        return super().get_form(request, obj, **kwargs)

admin.site.register(Menu, MenuAdmin)