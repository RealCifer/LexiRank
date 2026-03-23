from django.urls import path
from .views import ParagraphUploadView, SearchWordView

urlpatterns = [
    path('upload/', ParagraphUploadView.as_view()),
    path('search/', SearchWordView.as_view()),
]  