from pydantic import BaseModel, Field
from typing import List, Optional

class VisualDescription(BaseModel):
    day: str = Field(
        ..., 
        description="The day of the week the visual is intended for (e.g., 'Monday')."
    )
    theme: str = Field(
        ..., 
        description="The strategic theme of the post, aligned with the content calendar (e.g., 'Motivation Monday')."
    )
    description: str = Field(
        ..., 
        description="A detailed prompt-style image description used for AI-image generation. Should capture the core visual idea, mood, and composition."
    )
    main_elements: List[str] = Field(
        ..., 
        description="A list of core objects or components that should appear in the image (e.g., ['cityscape', 'red sofa', 'large window'])."
    )
    color_palette: List[str] = Field(
        ..., 
        description="A list of key colors or tones to be represented in the visual (e.g., ['neutral tones', 'pop of red'])."
    )
    mood: str = Field(
        ..., 
        description="The emotional or atmospheric tone of the image (e.g., 'cozy and inviting')."
    )
    style: Optional[str] = Field(
        None, 
        description="The artistic style or aesthetic to be followed (e.g., 'realistic', 'minimalist', 'vibrant')."
    )

class WeeklyVisualPlan(BaseModel):
    visuals: List[VisualDescription] = Field(
        ..., 
        description="A list of visual descriptions, one for each Instagram post of the week, aligned with the overall content strategy."
    )
