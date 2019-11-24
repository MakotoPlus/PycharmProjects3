from django.contrib import admin
from applicantctl.models import M_Appl_Route, M_Work_History, M_Department, M_Judgment

# Register your models here.

#ƒNƒ‰ƒXéŒ¾
class M_Appl_RouteAdmin(admin.ModelAdmin):
	pass
class M_Work_HistoryAdmin(admin.ModelAdmin):
	pass
class M_DepartmentAdmin(admin.ModelAdmin):
	pass
class M_JudgmentAdmin(admin.ModelAdmin):
	pass

admin.site.register(M_Appl_Route, M_Appl_RouteAdmin) #Œˆ‚Ü‚Á‚½‘‚«•û
admin.site.register(M_Work_History, M_Work_HistoryAdmin) #Œˆ‚Ü‚Á‚½‘‚«•û
admin.site.register(M_Department, M_DepartmentAdmin) #Œˆ‚Ü‚Á‚½‘‚«•û
admin.site.register(M_Judgment, M_JudgmentAdmin) #Œˆ‚Ü‚Á‚½‘‚«•û

