from django.contrib import admin
from .models import User, MedicalImageUpload, Item

# Admin para o modelo User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "nome", "setor", "is_active", "is_admin")
    list_filter = ("is_active", "is_admin")
    search_fields = ("email", "nome")
    ordering = ("email",)


# Admin para o modelo de upload
@admin.register(MedicalImageUpload)
class MedicalImageUploadAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "file", "file_type", "upload_date")
    list_filter = ("file_type", "upload_date")
    search_fields = ("user__email", "file")
    ordering = ("-upload_date",)


# Admin opcional para o modelo Item (se ainda usa)
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao")
