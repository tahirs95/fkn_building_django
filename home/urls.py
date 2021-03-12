from django.urls import path
from . views import HomeReviewCreateView, HomeReviewDetailView, HomeReviewUpdateView
from . import views


urlpatterns = [
    #path('', HomeReviewListView.as_view(), name='Home'),
    path('', views.home, name='Home'),
    path('contact', views.contact, name='contact'),
    path('review/<int:pk>/', HomeReviewDetailView.as_view(), name='Review-Detail'),
    path('review/<int:pk>/update', HomeReviewUpdateView.as_view(), name='Review-Update'),
    path('review/new', HomeReviewCreateView.as_view(), name='Review'),
]