from rest_framework.response import Response


class ApiResponse:
    """
    Standard API response helper for Django REST Framework.
    """

    @staticmethod
    def success(data=None, message="Success", status=200, log=None):
        return Response(
            {
                "response": True,
                "message": message,
                "data": data,
                "errors": None,
                "log": log,
            },
            status=status,
        )

    @staticmethod
    def error(errors=None, message="Error", status=400, log=None):
        return Response(
            {
                "response": False,
                "message": message,
                "data": None,
                "errors": errors,
                "log": log,
            },
            status=status,
        )

