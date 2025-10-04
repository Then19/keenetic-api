from pydantic import BaseModel


class PolicyInfo(BaseModel):
    mac: str
    policy: str
