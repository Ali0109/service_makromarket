from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from . import models, helpers


class AnalysisAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    # DEVICE
    def device_users_count(self, request):
        android = models.FCMDevice.objects.filter(type='android').values('user_id').distinct().count()
        ios = models.FCMDevice.objects.filter(type='ios').values('user_id').distinct().count()
        users = models.FCMDevice.objects.values('user_id').distinct().count()
        return Response({"ios": ios, 'android': android, 'users': users})

    def device_users_date_count(self, request, *args, **kwargs):
        date_created = helpers.get_start_end_month_by_year_month(kwargs['year'], kwargs['month'])
        filter_queryset = models.FCMDevice.objects.filter(date_created__gte=date_created['start'], date_created__lte=date_created['end'])
        android = filter_queryset.filter(type='android').values('user_id').distinct().count()
        ios = filter_queryset.filter(type='ios').values('user_id').distinct().count()
        users = filter_queryset.values('user_id').distinct().count()
        return Response({"ios": ios, 'android': android, 'users': users, 'date': f"{kwargs['year']}-{kwargs['month']}"})

    # CARD
    def card_users_count(self, request):
        users = models.Card.objects.filter(user_id__isnull=False).count()
        return Response({'users': users})

    # USER
    def users_count(self, request):
        users = models.LoyaltyUser.objects.all().count()
        return Response({'users': users})

    def users_date_count(self, request, *args, **kwargs):
        created_at = helpers.get_start_end_month_by_year_month(kwargs['year'], kwargs['month'])
        users = models.LoyaltyUser.objects.filter(created_at__gte=created_at['start'], created_at__lte=created_at['end']).count()
        return Response({'users': users})

    def users_named_count(self, request):
        users = models.LoyaltyUser.objects.filter(last_name__isnull=False, first_name__isnull=False).count()
        return Response({"users": users})

    def users_birthday_count(self, request):
        users = models.LoyaltyUser.objects.filter(birthday__isnull=False).count()
        return Response({"users": users})
