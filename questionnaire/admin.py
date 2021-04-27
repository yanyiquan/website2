from django.contrib import admin
from .models import Client, QuestionSLR, QuestionTolerance, QuestionInvtype, QuestionESG, QuestionTrends, Answer, Result, ResultSLR, Discount
# Register your models here.

admin.site.site_header = 'Administration Page'
admin.site.site_title = 'Administration'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'password')
    list_display_links = ['id']
    search_fields = ['id']
    list_filter = ['id']


@admin.register(QuestionSLR)
class SLRAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'optionA', 'optionB', 'optionC', 'optionD', 'optionE', 'textbox')


@admin.register(QuestionTolerance)
class ToleranceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'optionA', 'optionB', 'optionC', 'optionD')


@admin.register(QuestionInvtype)
class InvtypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'optionA', 'optionB', 'optionC', 'optionD')


@admin.register(QuestionESG)
class ESGAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'optionA', 'optionB', 'optionC', 'optionD', 'optiononly')


@admin.register(QuestionTrends)
class TrendsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('cid', 'pid', 'qid', 'answer')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('cid', 'result')


@admin.register(ResultSLR)
class ResultSLRAdmin(admin.ModelAdmin):
    list_display = ('cid', 'slr')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('income_growth', 'expense_growth', 'discounting_factor')
