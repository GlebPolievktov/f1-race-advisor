from pydantic import BaseModel,Field,model_validator,field_validator
from typing import Literal,Self
from datetime import date

class RacePreferences(BaseModel):
    driver:str | None = None
    weather:Literal["dry","wet","rain"] | None = None
    year_from: int | None = Field(default=None,ge=1950)
    year_to: int | None = Field(default=None,ge=1950)
    spoiler_free: bool = True

    limit: int = Field(default=3,ge=1,le=5
    )
    @field_validator("year_from","year_to")
    @classmethod
    def check_year(cls,value:int|None)->int|None:
        if value is not None and value > date.today().year:
            raise ValueError("Year cannot be in the future")

        return value
    @model_validator(mode='after')
    def check_year_range(self):
        if (self.year_to is not None and self.year_from is not None and self.year_to < self.year_from):
            raise ValueError(
                "year_from cannot be greater than year_to"
            )

        return self