from django.urls import path
from .views import CopyList

urlpatterns = [path("copies/", CopyList.as_view())]
