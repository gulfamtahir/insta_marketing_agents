from typing import List
from pydantic import BaseModel, Field

class InstagramPostCopy(BaseModel):
    day: str = Field(
        ..., 
        description="The day of the week the post is scheduled for (e.g., 'Monday')."
    )
    theme: str = Field(
        ..., 
        description="The strategic theme for the post aligned with the content calendar (e.g., 'Motivation Monday')."
    )
    caption: str = Field(
        ..., 
        description="The full Instagram caption text, written in the brand's tone and optimized for engagement."
    )
    call_to_action: str = Field(
        ..., 
        description="A clear and compelling call to action to drive audience interaction (e.g., 'Visit our website today!')."
    )
    keywords: List[str] = Field(
        ..., 
        description="A list of SEO keywords integrated into the caption for visibility and reach."
    )
    hashtags: List[str] = Field(
        ..., 
        description="Relevant and trending hashtags used to increase discoverability of the post."
    )

class WeeklyCopywritingOutput(BaseModel):
    posts: List[InstagramPostCopy] = Field(
        ..., 
        description="A list of Instagram post copies for the week, each corresponding to a day and its content theme."
    )
