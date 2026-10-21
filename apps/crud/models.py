from django.db import models

# Create your models here.
class Chamado(models.Model):
    CATEGORIAS = [
        ('hardware', 'Hardware'),
        ('software', 'Software'),
        ('rede', 'Rede / Internet'),
        ('acesso', 'Acesso / Senha'),
        ('email', 'E-mail'),
        ('impressora', 'Impressora'),
        ('outros', 'Outros'),
    ]
    PRIORIDADES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    ]
    STATUS = [
        ('aberto', 'Aberto'),
        ('andamento', 'Em andamento'),
        ('aguardando', 'Aguardando usuário'),
        ('resolvido', 'Resolvido'),
    ]

    codigo_chamado = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=120, null=False, blank=False)
    solicitante = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    setor = models.CharField(max_length=60, null=False, blank=False)
    patrimonio = models.CharField(max_length=10, unique=True, null=True, blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='outros')
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    status = models.CharField(max_length=12, choices=STATUS, default='aberto')
    descricao = models.TextField(null=False, blank=False)
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-codigo_chamado']

    @property
    def protocolo(self):
        return f"#{self.codigo_chamado:05d}"

    @property
    def icone(self):
        return {
            'hardware': 'bi-pc-display',
            'software': 'bi-window-stack',
            'rede': 'bi-wifi',
            'acesso': 'bi-key',
            'email': 'bi-envelope',
            'impressora': 'bi-printer',
        }.get(self.categoria, 'bi-three-dots')

    def __str__(self):
        return f"{self.protocolo} - {self.titulo}"
