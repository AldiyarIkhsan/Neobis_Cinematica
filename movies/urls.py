from rest_framework.routers import SimpleRouter
from movies.views import MoviesViewSet

router = SimpleRouter()
router.register('', MoviesViewSet)
urlpatterns = router.urls
