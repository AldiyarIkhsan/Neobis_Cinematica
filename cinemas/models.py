from django.db import models
from movies.models import Movies


# Create your models here.
class Cinema(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.TextField(max_length=200, null=False)
    contacts = models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name: "cinema"
        verbose_name_plural: "cinemas"

    def __str__(self):
        return f'Кинотеатр: {self.name}'

class Room(models.Model):
    name = models.CharField(max_length=50, null=False)
    cinema = models.ForeignKey(to=Cinema, on_delete=models.CASCADE, related_name='rooms')

    class Meta:
        verbose_name: "room"
        verbose_name_plural: "rooms"

    def __str__(self):
        return f'Кинотеатр: {self.cinema} |комната : {self.name}'

class Seat(models.Model):
    number = models.PositiveIntegerField(default=0)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE, related_name='seats')

    class Meta:
        verbose_name: "seat"
        verbose_name_plural: "seats"

    def __str__(self):
        return f'Комната: {self.room} |место : {self.number}'

class Showtime(models.Model):
    date = models.DateTimeField()
    price = models.PositiveIntegerField(default=0)
    movie = models.ForeignKey(to=Movies, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'Сеанс: {self.movie} |место : {self.date}'

class Ticket(models.Model):
    seat = models.ForeignKey(to=Seat, on_delete=models.CASCADE)
    showtime = models.ForeignKey(to=Showtime, on_delete=models.CASCADE)

    def __str__(self):
        return f'Билет: {self.showtime} |место : {self.seat}'


class Reservation(models.Model):
    seats = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    showtime = models.ForeignKey(to=Showtime, on_delete=models.CASCADE)


