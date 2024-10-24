from datetime import datetime, timedelta
from typing import Optional

import bcrypt
import jwt
from sqlalchemy.orm import Session
from schema.payment import UserLogin, Token
from models.payment import User

# JWT 로그인 처리
def userlogin(login: UserLogin, db: Session):
    loginuser = db.query(User)\
        .filter(User.userid == login.userid).first()
    print(loginuser)

    if loginuser is None:   # 아이디가 일치하지 않으면
        token = None
    elif not bcrypt.checkpw(login.passwd.encode('utf-8'), loginuser.passwd):
        token = None
    else:
        access_token = generate_access_token(login.userid)
        token = Token(access_token=access_token, token_type='bearer')

    return token


def hashed_password(passwd):
    SALT = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(passwd.encode('utf-8'), SALT)
    print(hashed_password)

    return hashed_password


def generate_access_token(userid: str,
                          expire_delta: Optional[datetime]=None):
    # 토큰 생성 시 사용할 비밀키
    SECRETKEY = 'Hello, World!! 13579'


    # 토큰 유효기간 설정
    if expire_delta:
        expire = datetime.now() + expire_delta
    else:
        expire = datetime.now() + timedelta(minutes=30)


    # 토큰 발급
    to_encode = {'iss': 'http://127.0.0.1:3000', 'sub': userid, 'exp': expire, 'aud': 'http://127.0.0.1:3000'}  # jwt 페이로드
    encode_jwt = jwt.encode(to_encode, SECRETKEY, algorithm='HS256')

    return encode_jwt
