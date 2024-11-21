from django.contrib import admin
from .models import Record


class RecordAdmin(admin.ModelAdmin):
    # Указываем поля, которые должны отображаться в списке
    list_display = ('parent_fio', 'parent_phone', 'child_fio', 'child_dob', 'created_at')

    # Настроим сортировку по дате (по убыванию)
    ordering = ('-created_at',)  # '-' перед полем означает сортировку по убыванию

    # Возможность поиска по ФИО родителей и детей
    search_fields = ('parent_fio', 'child_fio')


    # Настройка поля поиска для удобства
    list_display_links = ('parent_fio',)  # Делает поле 'parent_fio' кликабельным для быстрого перехода


admin.site.register(Record, RecordAdmin)