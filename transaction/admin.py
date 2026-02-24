from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_ref', 'sender_name', 'receiver_name', 
                   'formatted_amount', 'created_at', 'view_receipt_link']
    list_filter = ['created_at', 'sender_country', 'receiver_country']
    search_fields = ['transaction_ref', 'sender_name', 'receiver_name', 
                    'sender_account', 'receiver_account', 'receiver_email']
    readonly_fields = ['transaction_ref', 'created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Transaction Reference', {
            'fields': ('transaction_ref',)
        }),
        ('Sender Information', {
            'fields': ('sender_name', 'sender_account', 'sender_country')
        }),
        ('Receiver Information', {
            'fields': ('receiver_name', 'receiver_account', 'receiver_country', 'receiver_email','receiver_bank')
        }),
        ('Transaction Details', {
            'fields': ('amount', 'created_at')
        }),
    )
    
    def formatted_amount(self, obj):
        return format_html('<strong style="color: #28a745;">₦{}</strong>', 
                          f"{obj.amount:,.2f}")
    formatted_amount.short_description = 'Amount'
    formatted_amount.admin_order_field = 'amount'
    
    def view_receipt_link(self, obj):
        url = reverse('transaction_receipt', args=[obj.transaction_ref])
        return format_html('<a class="button" href="{}" target="_blank" style="background: #1a237e; color: white; padding: 5px 10px; border-radius: 5px; text-decoration: none;">View Receipt</a>', url)
    view_receipt_link.short_description = 'Receipt'
    
    # Customize admin template
    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }