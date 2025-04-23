import httpx
from datetime import date
from datetime import datetime
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/crypto", tags=["Crypto"])

@router.post("/{crypto}")
async def get_crypto_profit(crypto: str, data: dict):
    quantidade = data["quantidade"]
    data_compra = datetime.fromisoformat(data["dataCompra"])
    data_venda = datetime.fromisoformat(data["dataVenda"])

    if not is_float(quantidade):
        raise HTTPException(status_code=422)

    if data_venda < data_compra:
        raise HTTPException(status_code=422)

    dias = abs((data_venda - data_compra).days)

    async with httpx.AsyncClient() as client:
        compra = await client.get(f"https://www.mercadobitcoin.net/api/{crypto}/day-summary/{data_compra.year}/{data_compra.month}/{data_compra.day}/")
        venda = await client.get(f"https://www.mercadobitcoin.net/api/{crypto}/day-summary/{data_venda.year}/{data_venda.month}/{data_venda.day}/")

    avg_compra = compra.json()["avg_price"]
    avg_venda = venda.json()["avg_price"]
    valor_compra = avg_compra * quantidade
    valor_venda = avg_venda * quantidade
    lucro = valor_venda - valor_compra
    lucro_percentual = (lucro / valor_compra) * 100

    return {
        "valor_da_compra": round(valor_compra, 2),
        "valor_da_venda": round(valor_venda, 2),
        "lucro": round(lucro, 2),
        "lucro_percentual": round(lucro_percentual, 2),
        "intervalo_em_dias": dias
    }

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
