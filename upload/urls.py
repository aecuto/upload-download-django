from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.UploadPage.as_view()), name='upload'),
    path('<slug:pk>', views.Download.as_view(), name='download'),
    path('delete/<slug:pk>', login_required(views.Delete.as_view()), name='delete'),
]