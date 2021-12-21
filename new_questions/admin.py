from django.contrib import admin
from .models import NewQuestions


@admin.register(NewQuestions)
class NewQuestionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
