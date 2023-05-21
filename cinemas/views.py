from cinemas.serializers import CinemasSerializer, SeatsSerializer, RoomDetailSerializer, ShowtimeSerializer, TicketSerializer
from rest_framework.viewsets import ModelViewSet
from cinemas.models import Cinema, Room, Seat, Showtime, Ticket

class CinemasViewSet(ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemasSerializer

class RoomsViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

    # def get_serializer_class(self):
    #     if self.action = 'list':
    #         return RoomSerializer
    # return RoomDetailSerializer

class SeatsViewSet(ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatsSerializer

class ShowtimeViewSet(ModelViewSet):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer