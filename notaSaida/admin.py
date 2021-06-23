from django.contrib import admin
from .models import NotaSaida


class NotaSaidaAdmin(admin.ModelAdmin):
    list_display = ['produto', 'numero_nota', 'quantidade', 'valor']


admin.site.register(NotaSaida, NotaSaidaAdmin)