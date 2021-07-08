from __future__ import absolute_import
import os
import celery
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
app = Celery('setup')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)#TODO refatorar esse codigo e melhorar
def validator(*args, **kwargs):
    Emprestimo = importa_models()

    print(f'request_id: {celery.current_task.request.id}')
    valor = float(kwargs['valor'])
    idade = int(kwargs['idade'])
    id_cliente = int(kwargs['id_cliente'])
    emprestimo = Emprestimo.objects.filter(cliente__id=id_cliente, valor=valor).last()
    emprestimo.ticket = celery.current_task.request.id

    if valor <= 100000.00 and idade >= 18:
        emprestimo.aprovado = True

    emprestimo.save()
    return 'Rotina assincrona finalizada'

def importa_models():#TODO Jogar para um utils.py
    from api.models import Cliente, Emprestimo
    return Emprestimo