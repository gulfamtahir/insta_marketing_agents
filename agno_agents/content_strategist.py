from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.googlesearch import GoogleSearchTools
from textwrap import dedent
from agno.tools.thinking import ThinkingTools
from agno.utils.pprint import pprint_run_response

content_strategist = Agent(
        name="Instagram Content Strategist",
        model=Ollama(id="llama3.1:8b"),
        tools = [ThinkingTools()],
        description=dedent("""\As a master planner with a creative spirit, you have a talent for envisioning a cohesive content strategy that resonates with audiences. Your expertise in aligning content with brand voice and audience interests has consistently driven engagement and growth."""),
        instructions=dedent("""\Based on the market research findings, develop a comprehensive content calendar for a week. The calendar should specify the theme for each day of the week (from Monday to Sunday) where some content should be posted, and preliminary ideas for post content. For now, focus on a three-day content calendar, including the most relevant keywords and hashtags to use in each post."""),
        expected_output=dedent("""\A detailed week-long content calendar, formatted as markdown, that includes days of the week (from monday to friday), a brief overview of content ideas, and the most relevant keywords and hashtags to use in each post. Ensure the calendar aligns with the identified trends and audience preferences.""")
)

market_reserach = dedent("""\n
Most Relevant Topics:                                                                                                            │
│                                                                                                                                  │
│  1 Castles in Germany                                                                                                            │
│  2 Neuschwanstein Castle                                                                                                         │
│  3 Heidelberg Castle                                                                                                             │
│  4 German castles and palaces                                                                                                    │
│                                                                                                                                  │
│ Recommended Hashtags:                                                                                                            │
│                                                                                                                                  │
│  1 #CastleInGermany                                                                                                              │
│  2 #NeuschwansteinCastle                                                                                                         │
│  3 #HeidelbergCastle                                                                                                             │
│  4 #GermanCastlesAndPalaces                                                                                                      │
│  5 #Schloss (a popular hashtag for castles in Germany)                                                                           │
│  6 #TravelGermany                                                                                                                │
│  7 #GermanyTourism                                                                                                               │
│                                                                                                                                  │
│ Emerging Trends:                                                                                                                 │
│                                                                                                                                  │
│  1 Seasonal content showcasing the changing seasons at Neuschwanstein Castle.                                                    │
│  2 Food and drink-themed posts featuring German cuisine and drinks.                                                              │
│  3 Instagrammable spots and photography ideas around German castles.                                                             │
│                                                                                                                                  │
│ Competitor Analysis:                                                                                                             │
│                                                                                                                                  │
│ The most popular posts are from accounts that highlight the beauty of Neuschwanstein Castle, with a focus on photography and     │
│ seasonal content.                                                                                                                │
│                                                                                                                                  │
│ For this week's content, we recommend focusing on "Castle in Germany" as the main topic. Here's a sample post idea:              │
│                                                                                                                                  │
│ Post Idea: Share a stunning photo of Heidelberg Castle, highlighting its beautiful architecture and scenic views of the Rhine    │
│ River.                                                                                                                           │
│                                                                                                                                  │
│ Caption:                                                                                                                         │
│                                                                                                                                  │
│ "Discover the magic of castles in Germany! Heidelberg Castle is one of the most impressive and picturesque castles in the        │
│ country. #CastleInGermany #HeidelbergCastle #GermanCastlesAndPalaces"                                                            │
│                                                                                                                                  │
│ This post idea aligns with the current trends and hashtags, while also showcasing a lesser-known castle in Germany. By sharing   │
│ high-quality content that resonates with the audience, you can increase engagement and attract new followers to the Castle       │
│ account.""")

if __name__ == "__main__":
    response = content_strategist.run(f"The market research is {market_reserach} now give me the week strategy", stream=True)
    pprint_run_response(response, markdown=True)
    