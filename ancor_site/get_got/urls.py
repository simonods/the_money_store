from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *


user_router = DefaultRouter()
user_router.register(r'users', UserViewSet)

position_router = SimpleRouter()
position_router.register(r'positions', PositionViewSet)

urlpatterns = [
    path('', main_page, name='main_page'),
    path('news/', news, name='news'),
    path('currency/', currency, name='currency'),
    path('about_us/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('forgot_password/', ForgotPassword.as_view(), name='forgot_password'),
    path('after_login/', after_login, name='after_login'),
    path('', include(user_router.urls)),
    path('nft_uranus/', nft_uranus, name='nft_uranus'),
    path('api/v1/', include(position_router.urls)),  # GET, POST req
    # path('api/v1/positionlist/', PositionViewSet.as_view({'get': 'list'})),
    # path('api/v1/positionlist/<int:pk>/', PositionViewSet.as_view({'put': 'update'})),

]
