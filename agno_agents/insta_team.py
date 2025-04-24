from agno.team.team import Team
from agno.models.ollama import Ollama
from agno.agent import Agent
from textwrap import dedent
from agno.tools.thinking import ThinkingTools
insta_team_agent = Agent(
   name = "Instagram Report Creation Agent",
   model=Ollama(id="llama3.1:8b"),
   description=dedent("""\You are an intelligent agent tasked with accurately 
                      merging the responses,ensuring no details from their responses are altered"""),
   instructions=dedent("""\you need to give a complete report in this manner:
                       1) Instagram Researcher:{searcher_response}
                       2) Instagram Content Strategist:{content_response}
                       3) Instagram Copy Write:{copywriter}
                       4) Instagram Visual Creator:{visual_reponse}""")

)

# insta_team = Team(
#      name="Instagram Content Creation Team",
#     description=dedent("""
#         A specialized team of Instagram content experts working together to create engaging, 
#         trend-aware, and strategically optimized content for Instagram accounts. The team 
#         combines market research, content strategy, copywriting, and visual design to produce 
#         comprehensive content packages.
#     """),
#  instructions=dedent("""
#         Coordinate the creation of Instagram content through the following structured process:

#         1. Market Research Phase (Market Researcher):
#            - Analyze current Instagram trends for {page_topic}
#            - Research competitor content and strategies
#            - Identify trending hashtags and engagement patterns
#            - Find viral content formats and styles
#            - Focus on content relevant to: {weekly_topic}

#         2. Content Strategy Development (Content Strategist):
#            - Create whole week content plan based on research findings
#            - Define content themes and visual style guidelines
#            - Plan content mix (posts, stories, reels)
#            - Incorporate trending hashtags strategically
#            - Ensure content aligns with brand voice

#         3. Copywriting Creation (Copywriter):
#            - Develop engaging captions for each planned post
#            - Incorporate researched hashtags naturally
#            - Create compelling calls-to-action
#            - Maintain brand voice consistency
#            - Optimize for engagement

#         4. Visual Content Planning (Visual Creator):
#            - Design detailed image descriptions for each post
#            - Specify color schemes and visual elements
#            - Create cohesive visual storytelling
#            - Align visuals with brand aesthetics
#            - Include trending visual elements

#         Success Criteria:
#         - Complete content package for whole week days
#         - Strategic hashtag integration
#         - Engaging captions with calls-to-action
#         - Detailed visual guidelines
#         - Alignment with current trends
#     """),
#      model=Ollama(id="llama3.1:8b"), 
#      tools = [ThinkingTools()],
#      members=[market_researcher , content_strategist , copywriter , visual_creator],
#      show_tool_calls=True,
#      mode="collaborate",
#      success_criteria="The team has reached a consensus.",
#      enable_agentic_context=True,
#      show_members_responses=True,
#      )
