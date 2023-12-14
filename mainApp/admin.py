from django.contrib import admin
from .models import Domain, Document, Account, User

# Register your models here.
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Domain)


class DocumentAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date_time',)


admin.site.register(Document, DocumentAdmin)
