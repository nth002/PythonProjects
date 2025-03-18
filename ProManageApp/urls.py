from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name="index"),
    path('login-or-signup/', views.login, name="login"),
    path('manager-dashboard/', views.managerDashboard, name="manager_dashboard"),
    path('add-project/', views.addProject, name="add_project"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)