import requests

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Make the API call and fetch the data
        # response = requests.get('https://api.example.com/data')
        # data = response.json()

        # Add the fetched data to the request object
        request.client_id = "54321"

        # Process the request and response
        # response = self.get_response(request)
        response = self.get_response(request)
        return response