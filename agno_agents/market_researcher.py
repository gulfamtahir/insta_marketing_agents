from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.googlesearch import GoogleSearchTools
from textwrap import dedent
from agno.utils.pprint import pprint_run_response
# from models_pyd.research_model import InstaArticles
# from pydantic_models.research_model import InstaArticles

market_researcher= Agent(
        name="Instagram Market Researcher",
        model=Ollama(id="llama3.1:8b"),
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
        
    
    )
