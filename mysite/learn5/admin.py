from django.contrib import admin

#Register your models here.

# from learn5.models import Member,Material,Running,Running_Member,Running_Material


class DocumentAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass 

# admin.site.register(Member,DocumentAdmin)
# admin.site.register(Material,DocumentAdmin)
# admin.site.register(Running,DocumentAdmin)
# admin.site.register(Running_Member,DocumentAdmin)
# admin.site.register(Running_Material,DocumentAdmin)


