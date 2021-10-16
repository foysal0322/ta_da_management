from django.contrib import admin
from django.urls import path,include
from TADA import views
urlpatterns = [
    path('',views.index,name='TADA'),
    path('index',views.index,name='index'),
    path('tada_history',views.tada_history,name='tada_histoy'),
    path('tada_update/<str:pk>',views.tada_update,name='tada_update'),

    path('render_pdf_view', views.render_pdf_view, name="render_pdf_view"),
]