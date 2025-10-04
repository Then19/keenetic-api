from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', extra='allow', env_file_encoding='utf-8',
    )


class KeeneticConfig(BaseConfig):
    ip: str = Field(..., validation_alias='KEENETIC_IP')
    user: str = Field(..., validation_alias='KEENETIC_USER')
    password: str = Field(..., validation_alias='KEENETIC_PASSWORD')


class Config(BaseConfig):
    keenetic: KeeneticConfig = KeeneticConfig()  # type: ignore[call-arg]


config = Config()