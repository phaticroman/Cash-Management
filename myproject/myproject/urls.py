from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myproject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',signupPage,name="signupPage"),
    path("signInPage/", signInPage, name="signInPage"),
    path("homePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("ProfilePage/", profilePage, name="profilePage"),
    path('add_cash/', add_cash_view, name='add_cash'),
    path('add_expense/', add_expense, name='add_expense'),
    path('cash_dashboard/', cash_dashboard, name='cash_dashboard'),
    path('update_cashview/<int:cash_id>/', update_cash_view, name='update_cash'),
    path('delete_cash_view/<int:cash_id>/', delete_cash_view, name='delete_cash_view'),
    path('update_expense/<int:expense_id>/', update_expense_view, name='update_expense'),
    path('delete_expense/<int:expense_id>/', delete_expense_view, name='delete_expense'),
    path('editcash/',editcash,name='editcash'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

