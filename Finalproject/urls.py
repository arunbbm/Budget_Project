"""Finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from Finalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.login_view,name='login'),
    url(r'^home/$',views.function,name='home'),
    url(r'^budget/$',views.budget_view,name='budget'),
    url(r'^expenses/$',views.expenses_view,name='expenses'),
    url(r'^collection/$',views.collection_view,name='collection'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^budgetadd/$',views.bud_add_page,name='budgetadd'),
    url(r'^budgetsearch/$',views.bud_search_page,name='budgetsearch'),
    url(r'^budgetupdate/$',views.bud_update_page,name='budgetupdate'),
    url(r'^expensesadd/$',views.exp_add_page,name='expensesadd'),
    url(r'^expensessearch/$',views.exp_search_page,name='expensessearch'),
    url(r'^expensesupdate/$',views.exp_update_page,name='expensesupdate'),
    url(r'^collectionadd/$',views.collection_add_page,name='collectionadd'),
    url(r'^collectionsearch/$',views.collection_search_page,name='collectionsearch'),
    url(r'^collectionupdate/$',views.collection_update_page,name='collectionupdate'),

]
