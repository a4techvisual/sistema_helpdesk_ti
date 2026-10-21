# DeskFlow: Helpdesk de TI (Django)

Sistema de abertura e acompanhamento de chamados de TI, construído sobre a mesma
estrutura do projeto `sistema_django_noturno` (apps `login` e `crud`, views
baseadas em função, `ModelForm` com widgets, máscaras em JavaScript).

## O que mudou em relação ao projeto original

| Original (Pacientes)        | DeskFlow (Chamados)                                    |
|-----------------------------|--------------------------------------------------------|
| `Paciente`                  | `Chamado` (título, solicitante, setor, patrimônio, categoria, prioridade, status, descrição, datas) |
| `PacienteForm`              | `ChamadoForm` (prioridade em cartões clicáveis)        |
| `novo_paciente`, `alterar_paciente`, `excluir_paciente`, `buscar_paciente` | `novo_chamado`, `alterar_chamado`, `excluir_chamado`, `buscar_chamado` |
| Máscara de CPF e telefone   | Máscara de patrimônio (`PAT-000000`) e telefone        |
| Lista simples `<ul>`        | Painel com cards de resumo, filtros por status e tabela responsiva |
| `alert()` de sucesso        | Tela com o protocolo do chamado aberto                 |

Melhorias de segurança e robustez:
- Exclusão só via **POST**, com modal de confirmação (antes era um link GET).
- `get_object_or_404` em vez de `.get()` (evita erro 500 em ID inexistente).
- Busca protegida por `@login_required`, pesquisando título, solicitante, setor, patrimônio ou `#protocolo`.
- Links do menu com `{% url %}` (antes eram caminhos relativos que quebravam fora da home).
- `LANGUAGE_CODE = 'pt-br'` e `TIME_ZONE = 'America/Sao_Paulo'`.

## Como rodar

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # opcional, para acessar /admin
python manage.py runserver
```

Acesse http://localhost:8000/login/ e clique em **Cadastre-se** para criar o primeiro usuário.

## Estrutura

```
config/                 settings, urls
apps/login/             login, cadastro e logout
apps/crud/
  models.py             Chamado
  forms.py              ChamadoForm
  views.py              index, novo_chamado, alterar_chamado, excluir_chamado, buscar_chamado
  static/css/style.css  todo o visual
  static/js/script.js   máscaras e contador de caracteres
  templates/            páginas + includes (header = barra lateral, form, footer)
```

Atalho: aperte **/** em qualquer página para ir direto à busca.
