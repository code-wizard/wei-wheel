from rest_framework.views import APIView
from accounts import serializers
from rest_framework.response import Response


class LtRegisterView(APIView):
    serializer_class = serializers.LtRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
