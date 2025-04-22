from fastapi import APIRouter

router = APIRouter(prefix="/payment", tags=["Payment"])

@router.get("/calculate/{value}/{amount}")
def calculate(value: float, amount: int):
    installments = []
    installment_value = round(value / amount, 2)

    for i in range(1, amount + 1):

        installments.append({"order": i, "value": installment_value})

    return {
        "value": value,
        "amount": amount,
        "installments": installments
    }