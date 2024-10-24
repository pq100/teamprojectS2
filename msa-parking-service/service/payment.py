from sqlalchemy.orm import Session

from schema.payment import PaymentBase
from models.payment import Payment
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.payment import Payment



def register(db: Session, payment: PaymentBase):

    # Payment 모델 생성
    payment_data = Payment(**payment.model_dump())
    db.add(payment_data)
    db.commit()
    db.refresh(payment_data)
    print(payment_data)

    return payment_data


# 주차 목록 조회
def paymentlist(db: Session):
    return db.query(Payment.mno, Payment.carnum, Payment.payid, Payment.payment, Payment.paydate).all()


def payment_history(db: Session):
    payments = db.query(Payment).all()  # 전체 결제 내역 조회
    return payments