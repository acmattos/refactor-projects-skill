import repositories.pedido_repository as pedido_repository


def calcular_desconto(faturamento):
    if faturamento > 10000:
        return round(faturamento * 0.1, 2)
    elif faturamento > 5000:
        return round(faturamento * 0.05, 2)
    elif faturamento > 1000:
        return round(faturamento * 0.02, 2)
    return 0.0


def relatorio_vendas():
    stats = pedido_repository.get_stats()
    faturamento = round(stats["faturamento"], 2)
    desconto = calcular_desconto(faturamento)
    total = stats["total"]
    return {
        "total_pedidos": total,
        "faturamento_bruto": faturamento,
        "desconto_aplicavel": desconto,
        "faturamento_liquido": round(faturamento - desconto, 2),
        "pedidos_pendentes": stats["pendentes"],
        "pedidos_aprovados": stats["aprovados"],
        "pedidos_cancelados": stats["cancelados"],
        "ticket_medio": round(faturamento / total, 2) if total > 0 else 0,
    }
