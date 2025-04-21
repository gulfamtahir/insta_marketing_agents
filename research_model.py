# models.py
from typing import List
from pydantic import BaseModel, Field


class Trend(BaseModel):
    title: str = Field(..., description="Title of the trend or topic")
    description: List[str] = Field(..., description="List of descriptions explaining the trend")


class HashtagCategory(BaseModel):
    category_name: str = Field(..., description="Category of hashtags")
    hashtags: List[str] = Field(..., description="List of hashtags")


class CompetitorPost(BaseModel):
    description: str = Field(..., description="Competitor post description")


class CompetitorActivity(BaseModel):
    posts: List[CompetitorPost] = Field(..., description="List of competitor posts")
    features: List[str] = Field(..., description="Instagram features used")
    content_variation: List[str] = Field(..., description="Different content formats used")


class StrategyItem(BaseModel):
    title: str = Field(..., description="Strategy item title")
    details: List[str] = Field(..., description="Details of the strategy")


class InstaArticles(BaseModel):
    latest_trends_topics: List[Trend] = Field(
        ..., 
        alias="Latest Trends and Topic name", 
        description="List of trending topics and descriptions"
    )
    recommended_hashtags: List[HashtagCategory] = Field(
        ..., 
        description="Hashtags organized by category"
    )
    competitor_activities: CompetitorActivity = Field(
        ..., 
        description="Insights from successful competitors"
    )
    strategic_recommendations: List[StrategyItem] = Field(
        ..., 
        description="Recommendations for upcoming content strategy"
    )
