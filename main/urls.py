from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from . import views
from .views import signup, login, submit_expense, submit_income, view_status


urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('expense/', submit_expense, name='submit_expense'),
    path('income/', submit_income, name='submit_income'),
    path('status/', view_status, name="view_status")
]
