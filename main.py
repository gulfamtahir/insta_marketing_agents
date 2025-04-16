from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools
from agno.team import Team
from agno.workflow import Workflow ,RunEvent, RunResponse
from typing import Dict, Iterator
from agno.utils.pprint import pprint_run_response
from textwrap import dedent
from textwrap import dedent
from rich.pretty import pprint
from dotenv import load_dotenv

load_dotenv()
class InstagramContentWorkflow(Workflow):
    market_researcher= Agent(
        name="Instagram Market Researcher",
        model=OpenAIChat("gpt-4o-mini"),
        tools=[GoogleSearchTools()],
        description=dedent("Armed with a keen eye for digital trends and a deep understanding of the Instagram landscape, you excel at uncovering actionable insights from social media data. Your analytical skills are unmatched, providing a solid foundation for strategic decisions in content creation. You are great at identifying the latest trends and the best hashtags for a given campaign.."),
        instructions=dedent("""\ 
                            Investigate the latest trends, hashtags, and competitor activities on Instagram specific to the industry of this Instagram account. Focus on gathering data that reveals what content performs well in the current year, identifying patterns, preferences, and emerging trends. 
                            Current date: {current_date}
                                Description of the instagram account for which you are doing this research: 
                            <INSTAGRAM_ACCOUNT_DESCRIPTION>{instagram_description}</INSTAGRAM_ACCOUNT_DESCRIPTION>
                            Find the most relevant topics, hashtags and trends to use the the posts for next week. The focus of the following week is the following: 
                            <NEXT_WEEK_CONTENT>{topic_of_the_week}</NEXT_WEEK_CONTENT> """),
                            expected_output=dedent("""\ A report with the most relevant information that you found, including relevant hashtags for this week's content and all other information that could be useful to the team working on content creation.""")
    
    )
    def run(self, page_topic, weekly_topic)-> Iterator[RunResponse]:
        return self.market_researcher.run(f"Do market reserach of this site:Instagram {page_topic}for the {weekly_topic}", stream=True)
    
    # research_team = Team(
    #     name="Research Team",
    #     members=[
    #         Agent(name="Trend Researcher", model=OpenAIChat("gpt-4")),
    #         Agent(name="Hashtag Analyst", model=OpenAIChat("gpt-4")),
    #         Agent(name="Timing Optimizer", model=OpenAIChat("gpt-4"))
    #     ],
    #     mode="collaborate"
    # )
    
    # strategy_generator = Agent(
    #     name="Content Strategy Generator",
    #     model=OpenAIChat("gpt-4"),
    #     instructions="Create content calendar with hashtags, titles, and publishing times."
    # )
    
    # caption_writer = Agent(
    #     name="Caption Writer",
    #     model=OpenAIChat("gpt-4"),
    #     instructions="Write SEO-optimized captions incorporating research findings."
    # )
    
    # image_describer = Agent(
    #     name="Image Description Generator",
    #     model=OpenAIChat("gpt-4"),
    #     instructions="Generate detailed, vivid image descriptions for AI generation."
    # )
    
    # report_compiler = Agent(
    #     name="Report Compiler",
    #     model=OpenAIChat("gpt-4"),
    #     instructions="Compile all information into a comprehensive report."
    # )



# Usage
workflow = InstagramContentWorkflow()
report_stream = workflow.run(page_topic="Castle", weekly_topic="Castle in Germany")
pprint_run_response(report_stream, markdown=True)
