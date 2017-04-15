from django.contrib import admin
from transactions.models import Payment


class PaymentAdmin(admin.ModelAdmin):
	list_display = ("from_account", "to_account", "amount", "direction", "initiated_by", "created_at", "updated_at")
	search_fields = ["guid"]

admin.site.register(Payment, PaymentAdmin)


