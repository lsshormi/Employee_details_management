from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile', 'date_of_birth')
    list_filter = ('date_of_birth',)
    search_fields = ('first_name', 'last_name', 'email', 'mobile')
    ordering = ('last_name', 'first_name')

    fieldsets = (
        (None, {
            'fields': ('photo', 'first_name', 'last_name', 'email', 'mobile', 'date_of_birth')
        }),
    )

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Full Name'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.order_by('last_name', 'first_name')
        return queryset