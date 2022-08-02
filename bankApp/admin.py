from django.contrib import admin, messages
from .models import Client, Bank
from django.db.models import QuerySet


# Register your models here.




class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_thirname', 'cart_balance', 'carrancy', 'bank', 'cart_number']
    list_editable = ['cart_balance', 'carrancy']
    actions = ['set_dollar', 'set_euro']
    search_fields = ['client_name']

    @admin.action(description='change to USD')
    def set_dollar(self, request, qs: QuerySet):
        qs.update(carrancy=Client.USD)

    @admin.action(description='change to EUR')
    def set_euro(self, request, qs : QuerySet):
        count_updatad = qs.update(carrancy=Client.EUR)
        self.message_user(request, f'you update {count_updatad} users', messages.SUCCESS)


admin.site.register(Client, ClientAdmin)
admin.site.register(Bank)
