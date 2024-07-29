from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import *
from .routers import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('news/', news, name='news'),
    path('currency/', currency, name='currency'),
    path('market/', MarketplacePositionsView.as_view(), name='market'),
    path('about_us/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('forgot_password/', ForgotPassword.as_view(), name='forgot_password'),
    path('after_login/', after_login, name='after_login'),
    # path('', include(user_router.urls)),
    path('', include(position_router.urls)),
    path('nft_uranus/', nft_uranus, name='nft_uranus'),
    path('api/v1/', include(position_router.urls)),  # GET, POST req
    path('api/coinmarketcap/', CoinMarketCupAPIDataView.as_view(), name='coinmarketcap'),
    path('cmc_test/', cryptocurrency, name='cmc_test'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
