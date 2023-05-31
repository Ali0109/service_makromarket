from django.db import models


class LoyaltyManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).using('db2')


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    objects = LoyaltyManager()

    class Meta:
        managed = False
        db_table = 'loyalty_app_language'


class Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    objects = LoyaltyManager()

    class Meta:
        managed = False
        db_table = 'loyalty_app_status'


class LoyaltyUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sms = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=255)
    birthday = models.DateField(blank=True, null=True)
    is_staff = models.IntegerField()
    is_superuser = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    gender = models.CharField(max_length=255, blank=True, null=True)
    lang = models.ForeignKey("Language", models.DO_NOTHING, blank=True, null=True)
    family_members = models.PositiveIntegerField(blank=True, null=True)
    family_status = models.IntegerField(blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    objects = LoyaltyManager()

    class Meta:
        managed = False
        db_table = 'loyalty_app_user'


class FCMDevice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    registration_id = models.TextField()
    type = models.CharField(max_length=10)
    user = models.ForeignKey("LoyaltyUser", models.DO_NOTHING, blank=True, null=True)

    objects = LoyaltyManager()

    class Meta:
        managed = False
        db_table = 'fcm_django_fcmdevice'


class Card(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.PositiveBigIntegerField(blank=True, null=True)
    balance = models.BigIntegerField()
    is_reserved = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    status = models.ForeignKey("Status", models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey("LoyaltyUser", models.DO_NOTHING, blank=True, null=True)
    is_blocked = models.IntegerField()

    objects = LoyaltyManager()

    class Meta:
        managed = False
        db_table = 'loyalty_app_card'
