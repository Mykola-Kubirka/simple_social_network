from django.utils import timezone


class UserRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # write user request time
        user = request.user
        if user.pk:
            user.last_request = timezone.now()
            user.save()
        return response
