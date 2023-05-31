from rest_framework.exceptions import APIException


class DateErrorException(APIException):
    status_code = 400
    default_detail = "Month must be min 1 and max 12"
    default_code = 'date_error'
