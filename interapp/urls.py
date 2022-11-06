# from django.conf import settings
from django.urls import path

from interapp import views
# from django.conf.urls.static import static
#
# urlpatterns += static(settings.MEDIA_URL,
#                       document_root=settings.MEDIA_ROOT)

urlpatterns = [

    path('',views.index,name='index'),
    path('LOGIN',views.LOGIN,name='LOGIN'),
    path('REG',views.REG,name='REG'),
    path('login/',views.login,name='login'),
    path('register', views.register, name='register'),
    path('Home',views.Home,name='Home'),
    # path('home/',views.home,name='home'),
    path('courses/',views.courses,name='courses'),
    path('course-details/',views.course_details,name='course_details'),

]