from pydantic import BaseModel, constr


class PaymentBase(BaseModel):
    carnum: constr(max_length=15)
    payid: constr(max_length=30)
    payment: constr(max_length=50)
    paydate: constr(max_length=50)  # 날짜 형식에 대한 검증 추가 가능

class Payment(PaymentBase):
    mno: int

    # ORM 맵핑을 위한 설정
    # 데이터베이스 테이블 각 행 <-> pydantic
    class Config:
        from_attributes=True

class PaymentList(BaseModel):
    carnum: str
    payid: str
    mno: int

    class Config:
        from_attributes=True


class PaymentLogin(BaseModel):
    carnum: str
    payid: str
