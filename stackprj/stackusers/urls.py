from os import stat
from django.urls import path
from django.contrib.auth import views
from stackusers import views as view
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path("register/", view.register, name="register"),
    path("login/", views.LoginView.as_view(template_name='stackusers/login.html'), name="login"),
    path("logout/", views.LogoutView.as_view(template_name='stackusers/logout.html'), name="logout"),
    path("profile/", view.profile, name="profile"),
    path('profile/update/', view.profile_update, name = 'profile_update'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)