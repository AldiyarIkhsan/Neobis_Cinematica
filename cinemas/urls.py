from rest_framework.routers import SimpleRouter
from cinemas.views import CinemasViewSet, RoomsViewSet, ShowtimeViewSet

router = SimpleRouter()
router.register('cinemas', CinemasViewSet)
router.register('rooms', RoomsViewSet)
router.register('showtime', ShowtimeViewSet)
urlpatterns = router.urls
