from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    #Isso exibe os nomes assim como o método __str__ faria em models
    list_display="firstname","lastname","country"

admin.site.register(Member,MemberAdmin)