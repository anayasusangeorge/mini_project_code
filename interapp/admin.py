from django.contrib import admin
from interapp.models import  user_reg,user_course,user_logins,course_detail,duration

# Register your models here.
admin.site.register(user_reg)
admin.site.register(user_course)
admin.site.register(user_logins)
admin.site.register(course_detail)
admin.site.register(duration)
# admin.site.register(assignment)
# Register your models here.
