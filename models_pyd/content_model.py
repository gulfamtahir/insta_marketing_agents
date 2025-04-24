from typing import List
from pydantic import BaseModel, Field

class DailyContent(BaseModel):
    day: str = Field(
        ..., 
        description="The day of the week the content is scheduled for (e.g., 'Monday')."
    )
    theme: str = Field(
        ..., 
        description="The strategic content theme for the day (e.g., 'Motivation Monday')."
    )
    content_idea: str = Field(
        ..., 
        description="A brief description or idea for the content to be posted (e.g., 'Share a client transformation story')."
    )
    keywords: List[str] = Field(
        ..., 
        description="A list of relevant SEO keywords to include in the content for better visibility."
    )
    hashtags: List[str] = Field(
        ..., 
        description="A list of hashtags to include with the post for increased discoverability (e.g., ['#MotivationMonday', '#GrowthMindset'])."
    )

class ContentCalendar(BaseModel):
    calendar: List[DailyContent] = Field(
        ..., 
        description="A list of daily content entries for the week. Each entry contains the theme, content idea, keywords, and hashtags."
    )
