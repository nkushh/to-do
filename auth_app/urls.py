from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
	path('user-login/', views.user_login, name='user_login'),
	path('user-signup/', views.user_signup, name='user_signup'),
	path('login/', views.LoginView.as_view(), name='login_user'),
	path('signup/', views.SignupUserView.as_view(), name='signup_user'),
	path('logout/', views.LogoutView.as_view(), name='logout_user'),
]