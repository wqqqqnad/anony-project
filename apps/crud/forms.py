#  118p 코드
# ekstns

from flask_wtf import FlaskForm # 이걸 상속해서 너만의 폼을 만들어봐라
from wtforms import PasswordField, StringField, SubmitField #안보이는비번 ,텍스트필드, 
from wtforms.validators import DataRequired, Email, Length 
# wtforms.validators : 유효성 검증 관련 모듈
# DateRequired : 이 필드는 반드시 값을 써야 하는 필드임
# Email : 이메일 형식을 반드시 지켜야하는 필드
# length : 입력한 값을 길이 관련

class UserForm(FlaskForm):
    username = StringField(
        "사용자명",
        validators=[
            DataRequired(message="사용자명은 필수입니다"),
            Length(max=30, message="30문자 이내로 입력해 주세요"),
        ],
    )

    email = StringField(
        "메일 주소",
        validators=[
            DataRequired(message="메일 주소는 필수입니다"),
            Email(message="30문자 이내로 입력해 주세요"),
        ],
    )

    password = PasswordField(
        "비밀번호",
        validators=[DataRequired(message="비밀번호는 필수입니다")]
    )

    submit = SubmitField("신규 등록")