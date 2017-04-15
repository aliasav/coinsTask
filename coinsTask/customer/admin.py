from django.contrib import admin
from customer.models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
	list_display = ("user", "user_account_id", "currency", "balance", "created_at", "updated_at")
	search_fields = ["user_account_id"]

admin.site.register(UserAccount, UserAccountAdmin)


