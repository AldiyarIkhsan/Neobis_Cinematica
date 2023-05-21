from rest_framework import serializers
from cinemas.models import Cinema, Room, Seat, Showtime, Ticket
# from rest_framework.serializers import HyperlinkedModelSerializer
# from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'number', 'room']

class RoomDetailSerializer(serializers.ModelSerializer):
    seats = SeatsSerializer(many=True)
    class Meta:
        model = Room
        fields = ['id', 'name', 'cinema', 'seats']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'cinema']

class CinemasSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True)
    class Meta:
        model = Cinema
        fields = ['id', 'name', 'address', 'contacts', 'rooms']

class ShowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showtime
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showtime
        fields = ['id', 'showtime']