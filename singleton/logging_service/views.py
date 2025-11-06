from django.http import JsonResponse
from .services import ServicoLog

def logs_recentes(request):
    '''
    Essa view retorna os logs recentes em formato JSON.
    Aceita um parâmetro GET opcional 'quantidade' para limitar o número de logs que serão retornados.
    Pode ser chamada dessa forma no navegador: http://localhost:8000/logs/recentes/?quantidade=10
    '''
    qtd = request.GET.get('quantidade')
    try:
        quantidade = int(qtd) if qtd is not None else None
    except ValueError:
        return JsonResponse({"erro": "Parâmetro 'quantidade' inválido"}, status=400)

    servico = ServicoLog()
    logs = servico.obter_recentes(quantidade)
    return JsonResponse({"logs": logs})

