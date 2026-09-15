from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, ProfileView, RegisterView
from categories.views import CategoryListCreateView,CategoryDetailView
from transactions.views import TransactionListCreateView,TransactionDetailView
from reports.views import BudgetViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

router = DefaultRouter()

router.register('budgets', BudgetViewSet, basename='budget')

urlpatterns = [

    path('profile/',ProfileView.as_view(), name='profile'),

    path('categories/', CategoryListCreateView.as_view(),name='category-list-create'),

    path('categories/<int:pk>/',CategoryDetailView.as_view(), name='category-detail'),

    path('transactions/', TransactionListCreateView.as_view(),name='transaction-list-create'),

    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),

    path('', include(router.urls) ),

    path("register/", RegisterView.as_view(), name="register"),
    
    path("login/", LoginView.as_view(), name="login"),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
