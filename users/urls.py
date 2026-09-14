from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileView
from categories.views import CategoryListCreateView,CategoryDetailView
from transactions.views import TransactionListCreateView,TransactionDetailView
from reports.views import BudgetViewSet

router = DefaultRouter()

router.register('budgets', BudgetViewSet, basename='budget')

urlpatterns = [

    path('profile/',ProfileView.as_view(), name='profile'),

    path('categories/', CategoryListCreateView.as_view(),name='category-list-create'),

    path('categories/<int:pk>/',CategoryDetailView.as_view(), name='category-detail'),

    path('transactions/', TransactionListCreateView.as_view(),name='transaction-list-create'),

    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),

    path('', include(router.urls) ),

]
