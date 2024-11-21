from django.db import models

class Record(models.Model):
    parent_fio = models.CharField(max_length=255)
    parent_phone = models.CharField(max_length=20)
    child_fio = models.CharField(max_length=255, blank=True, null=True)  # Сделать поле необязательным
    child_dob = models.DateField(blank=True, null=True)  # Сделать поле необязательным
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматическая фиксация времени при создании записи

    def __str__(self):
        return f'{self.parent_fio} - {self.child_fio}'
