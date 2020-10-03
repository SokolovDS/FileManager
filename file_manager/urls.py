from django.urls import path

from file_manager.views import SaveFileView, AllFilesView

urlpatterns = [
    path('upload/', SaveFileView.as_view()),
    path('', AllFilesView.as_view()),
]
