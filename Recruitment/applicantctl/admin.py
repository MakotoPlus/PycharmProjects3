from django.contrib import admin
from applicantctl.models import M_Appl_Route, M_Work_History, M_Department, M_Judgment

# Register your models here.

#�N���X�錾
class M_Appl_RouteAdmin(admin.ModelAdmin):
	pass
class M_Work_HistoryAdmin(admin.ModelAdmin):
	pass
class M_DepartmentAdmin(admin.ModelAdmin):
	pass
class M_JudgmentAdmin(admin.ModelAdmin):
	pass

admin.site.register(M_Appl_Route, M_Appl_RouteAdmin) #���܂���������
admin.site.register(M_Work_History, M_Work_HistoryAdmin) #���܂���������
admin.site.register(M_Department, M_DepartmentAdmin) #���܂���������
admin.site.register(M_Judgment, M_JudgmentAdmin) #���܂���������

