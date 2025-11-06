import threading
from collections import deque
from django.utils import timezone

class EntradaLog:
    def __init__(self, nivel: str, mensagem: str, instante):
        self.nivel = nivel
        self.mensagem = mensagem
        self.instante = instante

    def para_dict(self):
        return {
            "instante": self.instante.isoformat(),
            "nivel": self.nivel,
            "mensagem": self.mensagem,
        }

class ServicoLog:
    _instancia = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = super(ServicoLog, cls).__new__(cls)
                    cls._instancia._iniciar()
        return cls._instancia

    def _iniciar(self):
        self._max_logs = 100
        self._logs = deque(maxlen=self._max_logs)

    def info(self, mensagem: str):
        self._adicionar("info", mensagem)

    def aviso(self, mensagem: str):
        self._adicionar("warn", mensagem)

    def erro(self, mensagem: str):
        self._adicionar("error", mensagem)

    def _adicionar(self, nivel: str, mensagem: str):
        entrada = EntradaLog(nivel, mensagem, timezone.now())
        self._logs.append(entrada)

    def obter_recentes(self, quantidade: int = None):
        entradas = list(self._logs)
        if quantidade is not None:
            entradas = entradas[-quantidade:]
        return [e.para_dict() for e in entradas]


'''
Esse serviço pode ser chamado dessa forma::

from logging_service.services import ServicoLog

logger = ServicoLog()
logger.info("Mensagem informativa")
logger.aviso("Aviso relevante")
logger.erro("Erro crítico ocorreu")
'''