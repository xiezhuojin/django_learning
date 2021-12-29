from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import Question, Choice


class ChoiceInline(TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # split the form up into fieldsets
    fieldsets = [
        (None, {"fields": ["question_text",]}),
        ("Date information", {"fields": ["pub_date",]}),
    ]
    # display inline for choice
    inlines = [ChoiceInline,]
    # display field
    list_display = ("question_text", "pub_date", "was_published_recently",)
    # field filter
    list_filter = ["pub_date",]
    # search field
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
