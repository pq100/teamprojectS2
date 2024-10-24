from typing import List

from schema.payment import Payment, PaymentList, PaymentBase
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from service.database import get_db
from service.payment import register

router = APIRouter()

@router.post('/index/payment', response_model=Payment)
async def Parking_payment(payment: PaymentBase, db: Session = Depends(get_db)):
    try:
        return register(db, payment)
    except Exception as e:
        # 적절한 에러 처리 로직 추가
        print(f"Error occurred: {e}")
        return {"error": "현재 창에 오류가 발생하였습니다.."}



@router.get('/payment/history', response_model=List[PaymentList])  # 엔드포인트 추가
async def payment_history(db: Session = Depends(get_db)):
    return payment_history(db)


