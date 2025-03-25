import os
from django.conf import settings
from passageidentity import Passage, PassageError
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        passage = Passage(app_id=os.getenv("IclX9qqvHi0pXtt4yUuPyHg4"))  # App ID do Passage
        token = request.headers.get("Authorization")  # Pega o token do cabeçalho

        if not token:
            return None  # Sem token, segue o fluxo normal

        try:
            user = passage.authenticate_request(request)  # Verifica o usuário
        except PassageError:
            raise AuthenticationFailed("Token inválido ou expirado")

        return (user, None)  # Retorna o usuário autenticado
