from django.db import models
import uuid


class Aluno(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        help_text="Valor Unico (R.A)"
    )
    aluno = models.CharField(max_length=150)
    nota1 = models.IntegerField()
    nota2 = models.IntegerField()
    nota3 = models.IntegerField()
    media = models.IntegerField(editable=False)

    def save(self):
        self.media = self.calcular_media()
        super().save()

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2 + self.nota3) / 3
        return self.media

    def mostraAluno(self):
        return self.aluno
        return self.media
