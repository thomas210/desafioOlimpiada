from fastapi import APIRouter

router = APIRouter(prefix="/payment", tags=["Payment"])

@router.get("/calculate/{value}/{amount}")
def calculate(value: float, amount: int):
    installments = []
    installment_value = round(value / amount, 2)

    diff = value - installment_value * amount

    for i in range(0, amount):
        if i == amount -1:
            installment_value = installment_value + diff
        installments.append({"order": i, "value": installment_value})

    return {
        "value": value,
        "amount": amount,
        "installments": installments
    }
