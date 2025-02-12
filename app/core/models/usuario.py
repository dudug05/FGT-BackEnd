from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)  # Email deve ser único
    senha = models.CharField(max_length=128)  # Senha armazenada como hash

    def save(self, *args, **kwargs):
        # Garante que a senha seja armazenada como hash
        if not self.senha.startswith('pbkdf2_'):  # Evita re-hash desnecessário
            self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

    def verificar_senha(self, senha_plana):
        """
        Verifica se a senha fornecida corresponde ao hash armazenado.
        """
        return check_password(senha_plana, self.senha)

    def __str__(self):
        return self.nome