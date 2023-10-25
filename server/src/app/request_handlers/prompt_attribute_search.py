from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ..models import Prompt
from ..serializers import PromptSerializer

class PromptSearch(APIView):

    def get(self, request: Request, format=None) -> Response:
        role = request.query_params.get("role") or ""
        phase = request.query_params.get("sdlc_phase") or ""
        
        try:
            prompts = Prompt.objects.filter(role__icontains=role, sdlc_phase__icontains=phase)
        except Prompt.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PromptSerializer(prompts, many=True)
        return Response({'prompts':serializer.data})
