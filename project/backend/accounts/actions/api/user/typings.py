from typing import TypedDict


class CreateUserRequestBodyType(TypedDict):
    username: str | None
    password: str | None
    confirm_password: str | None


class CreateUserValidatedDataType(TypedDict):
    username: str
    password: str


class ChangeEmailValidatedDataType(TypedDict):
    email: str


class ChangePasswordRequestBodyType(TypedDict):
    password: str | None
    current_password: str | None

class ChangePasswordValidatedDataType(TypedDict):
    password: str