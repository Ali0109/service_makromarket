from rest_framework.exceptions import APIException


class DateErrorException(APIException):
    status_code = 400
    default_detail = "Incorrect date"
    default_code = "date_error"
