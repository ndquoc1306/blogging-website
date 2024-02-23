from pydantic import BaseModel, root_validator
from typing import Optional


class CreateBlog(BaseModel):
    TITLE: str
    SLUG: str
    CONTENT: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if 'TITLE' in values:
            values["SLUG"] = values.get("TITLE").replace(" ", "-").lower()
        return values
