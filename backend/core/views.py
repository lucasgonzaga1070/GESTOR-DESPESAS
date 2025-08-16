from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Categoria, Transacao
from .serializers import CategoriaSerializer, TransacaoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        data_inicio = self.request.query_params.get('data_inicio')
        data_fim = self.request.query_params.get('data_fim')
        categoria_tipo = self.request.query_params.get('categoria_tipo')  # exemplo filtro categoria

        if data_inicio:
            queryset = queryset.filter(data__gte=data_inicio)
        if data_fim:
            queryset = queryset.filter(data__lte=data_fim)
        if categoria_tipo:
            queryset = queryset.filter(categoria__tipo=categoria_tipo)

        return queryset

    @action(detail=False, methods=['get'])
    def resumo(self, request):
        # Captura parâmetros opcionais
        data_inicio = request.query_params.get('data_inicio')
        data_fim = request.query_params.get('data_fim')

        queryset = Transacao.objects.all()

        # Filtra por intervalo de datas se vierem os parâmetros
        if data_inicio:
            queryset = queryset.filter(data__gte=data_inicio)
        if data_fim:
            queryset = queryset.filter(data__lte=data_fim)

        total_receitas = queryset.filter(categoria__tipo='receita').aggregate(total=Sum('valor'))['total'] or 0
        total_despesas = queryset.filter(categoria__tipo='despesa').aggregate(total=Sum('valor'))['total'] or 0
        saldo = total_receitas - total_despesas

        return Response({
            'total_receitas': total_receitas,
            'total_despesas': total_despesas,
            'saldo': saldo
        })  
    
    @action(detail=False, methods=['get'])
    def por_categoria(self, request):
        data_inicio = request.query_params.get('data_inicio')
        data_fim = request.query_params.get('data_fim')

        queryset = Transacao.objects.filter(categoria__tipo='despesa')

        if data_inicio:
            queryset = queryset.filter(data__gte=data_inicio)
        if data_fim:
            queryset = queryset.filter(data__lte=data_fim)

        dados = (
            queryset.values('categoria__nome')
                    .annotate(total=Sum('valor'))
                    .order_by('-total')
        )
        return Response(dados)
