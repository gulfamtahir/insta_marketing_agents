from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools
from agno.team import Team
from agno.workflow import Workflow ,RunEvent, RunResponse
from typing import Dict, Iterator , List
from agno.utils.pprint import pprint_run_response
from agno.utils.log import logger
from textwrap import dedent
from rich.pretty import pprint
from dotenv import load_dotenv
############# GETTING PYDANTIC MODELS ################
from research_model import InstaArticles
from content_model import ContentCalendar
from copy_writer_model import WeeklyCopywritingOutput
load_dotenv()





class InstagramContentWorkflow(Workflow):
    market_researcher= Agent(
        name="Instagram Market Researcher",
        model=OpenAIChat("gpt-4o-mini"),
        tools=[GoogleSearchTools()],
        add_datetime_to_instructions=True,
        structured_outputs=True,
        show_tool_calls=True,
        description=dedent("Armed with a keen eye for digital trends and a deep understanding of the Instagram landscape, you excel at uncovering actionable insights from social media data. Your analytical skills are unmatched, providing a solid foundation for strategic decisions in content creation. You are great at identifying the latest trends and the best hashtags for a given campaign.."),
        instructions=dedent("""\ 
                            Investigate the latest trends, hashtags, and competitor activities on Instagram specific to the industry of this Instagram account. Focus on gathering data that reveals what content performs well in the current year, identifying patterns, preferences, and emerging trends. 
                            Current date: {current_date}
                                Description of the instagram account for which you are doing this research: 
                            <INSTAGRAM_ACCOUNT_DESCRIPTION>{instagram_description}</INSTAGRAM_ACCOUNT_DESCRIPTION>
                            Find the most relevant topics, hashtags and trends to use the the posts for next week. The focus of the following week is the following: 
                            <NEXT_WEEK_CONTENT>{topic_of_the_week}</NEXT_WEEK_CONTENT> """),
        expected_output=dedent("""\ A report with the most relevant information that you found, including relevant hashtags for this week's content and all other information that could be useful to the team working on content creation."""),
        # response_model=InstaArticles
    
    )
    
    content_strategist = Agent(
        name="Instagram Content Strategist",
        model=OpenAIChat("gpt-4o-mini"),
        description=dedent("""\As a master planner with a creative spirit, you have a talent for envisioning a cohesive content strategy that resonates with audiences. Your expertise in aligning content with brand voice and audience interests has consistently driven engagement and growth."""),
        instructions=dedent("""\Based on the market research findings, develop a comprehensive content calendar for a week. The calendar should specify the theme for each day of the week (from Monday to Sunday) where some content should be posted, and preliminary ideas for post content. For now, focus on a three-day content calendar, including the most relevant keywords and hashtags to use in each post."""),
        expected_output=dedent("""\A detailed week-long content calendar, formatted as markdown, that includes days of the week (from monday to friday), a brief overview of content ideas, and the most relevant keywords and hashtags to use in each post. Ensure the calendar aligns with the identified trends and audience preferences.""")
    )
    
    copywriter = Agent(
        name="Instagram Copywriter",
        model=OpenAIChat("gpt-4"),
        description=dedent("""\ With a flair for storytelling and a persuasive pen, you create narratives that captivate and engage the audience. Your words are the bridge between the brand and its followers, embodying the brand's voice in every caption and call to action. Your writing is not only engaging, but also it incorporates all the SEO techniques, such as seamlessly using top keywords given to you and adding the best hashtags that are trending at the moment."""),
        instructions=dedent("""\    Write captivating and relevant copy for each Instagram post of the week, aligning to the strategic themes of the content calendar. The copy should engage the audience, embody the brand's voice, and encourage interaction. The copy should also be SEO-friendly and incorporate the relevant keywords and hashtags contained in the content schedule. 

        Consider the following guidelines when writing the copy:
        - Keep the copy concise and engaging.
        - Include a call to action where appropriate.
        - Use relevant keywords and hashtags.
        - Ensure the copy aligns with the brand's voice and tone.

        Here are some examples of the copy that you could use:
        - "Hello everyone! :heart: We're excited to share our latest collection with you. Check out our website for more details. #newcollection #fashion #style"
        - "Happy Monday! :sunflower: Start your week right with our delicious smoothies. Visit our store today! #smoothies #healthyliving #mondaymotivation"
        - "Feeling stressed? :massage: Treat yourself to a relaxing spa day. Book now and unwind in luxury. #spaday #relaxation #selfcare"""),
        expected_output= "A document formatted as markdown, with several sections. Each section should contain the copy for a single Instagram post, along with the relevant hashtags and calls to action. The copy should be engaging, on-brand, and aligned with the content calendar."
    )
    
    visual_creator =Agent(
        name="Instagram Visual Creator",
        model=OpenAIChat("gpt-4"),
        description=dedent("""\Merging creativity with technology, you use words to bring visions to life. You are great at crafting a detailed image description that can be used as a prompt for an AI-image generator. Your descriptions are more than just images; they tell stories, evoke emotions, and capture the essence of the brand, setting the visual tone for the Instagram feed."""),
        instructions=dedent("""\Based on the content strategy for each Instagram post, create the the visual art that will be published on Instagram on each day of the week. To do that, you will need to create a detailed description of the image that you will use for each day. 
        The descriptions that you will use need to be detailed, yet concise, and should include the main elements that should be present in the image. Describe the colors, the objects, the mood, and any other relevant information that you think is important for the image to be created.

        Here are some examples of the descriptions that you could use:
        - A realistic image of a living room with a modern design. The room should have a large window with a view of a cityscape. The color palette should be neutral, with a pop of color in the form of a red sofa. The room should be well-lit, with a cozy and inviting atmosphere.
        - A minimalist image of a desk with a laptop, a notebook, and a cup of coffee. The desk should be made of light wood, and the background should be a plain white wall. The image should convey a sense of focus and productivity.
        - A vibrant image of a tropical beach at sunset. The beach should be deserted, with palm trees swaying in the wind. The sky should be a mix of warm colors, with the sun setting on the horizon. The image should evoke a sense of relaxation and tranquility."""),
        expected_output="A markdown document with detailed descriptions of the images that will be used for each Instagram post of the week. Each description should be concise and include the main elements, colors, mood, and any other relevant information that will guide the creation of the image. The descriptions should align with the content calendar and the identified trends."
    )

    def run(self, page_topic : str, weekly_topic: str , use_cache:bool)-> Iterator[RunResponse]:
        logger.info(f"Generating Instagram Report on: {page_topic}")
        logger.info(f"use cache: {use_cache}")
        return self.market_researcher.run(f"Do market reserach of this site:Instagram {page_topic}for the {weekly_topic}", stream=True)
    
    def add_report_to_cache(self , page_topic : str,  weekly_topic: str)->None:
        logger.info(f"Caching the Instagram Topic report for the topic: {page_topic}")
        self.session_state.setdefault("insta_topic", [])
        self.session_state['insta_topic']['page_topic'] = weekly_topic
        logger.info(f"Instagram report cached successfully for the topic: {page_topic}")
    
    def get_cached_insta_report(self, page_topic: str)-> str:
        logger.info(f"checking cache for the report of the topic: {page_topic}")
        cached_report = self.session_state.get('insta_topic' ,[]).get(page_topic)

        if cached_report:
            logger.info(f"Cache hit for the Insta topic: {page_topic}")
        else:
            logger.info(f"No cache blog post found for the topic: {page_topic}")
        return cached_report
    
    def _get_search_results(self, insta_topic: str) -> str:
        MAX_ATTEMPTS = 3
        for attempt in range(MAX_ATTEMPTS) :
            try:
                logger.info(f"Attempt {attempt + 1}: Searching for articles on '{insta_topic}'")
                searcher_response: RunResponse = self.market_researcher.run(insta_topic)
                if(searcher_response is not None and searcher_response.content is not None ):
                    article_count = len(searcher_response.content.articles)
                    logger.info(
                        f"Found {article_count} articles on attempt {attempt + 1}"
                    )
                    return searcher_response.content
                else:
                    logger.warning(
                        f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: Invalid response type"
                    )
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed with error: {e}")
        logger.error(f"Failed to retrieve search results for '{insta_topic}' after {MAX_ATTEMPTS} attempts") 
        return None
    def write_report(self , topic: str , search_results : List)->Iterator[RunResponse]:
        pass
# usage
workflow = InstagramContentWorkflow()
report_stream = workflow.run(page_topic="Castle", weekly_topic="Castle in Germany")
pprint_run_response(report_stream, markdown=True)
