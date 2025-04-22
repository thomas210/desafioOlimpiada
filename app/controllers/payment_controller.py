from fastapi import APIRouter

router = APIRouter(prefix="/payment", tags=["Payment"])

@router.get("/calculate/{value}/{amount}")
def calculate(value: float, amount: int):
    installments = []
    installment_value = round(value / amount, 2)

    # BUG N2 - Erro nas parcelas
    # difference = round(value - (installment_value * amount), 2)
    # first_installment = installment_value + difference

    for i in range(1, amount + 1):
        # val = first_installment if i == 1 else installment_value
        # installments.append({"order": i, "value": round(val, 2)})

        installments.append({"order": i, "value": installment_value})

    return {
        "value": value,
        "amount": amount,
        "installments": installments
    }