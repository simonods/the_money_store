from rest_framework.routers import SimpleRouter

from .views import *

position_router = SimpleRouter()
position_router.register(r'positions', PositionViewSet)

# user_router = DefaultRouter()
# user_router.register(r'users', UserViewSet)
