from agno.workflow import Workflow ,RunEvent, RunResponse
from agno.agent import Agent
from typing import Dict, Iterator , List
from agno.utils.pprint import pprint_run_response
from agno.utils.log import logger
from dotenv import load_dotenv
from agno.playground import Playground , serve_playground_app
############# GETTING Agno MODELS ################
from agno_agents.market_researcher import market_researcher
from agno_agents.content_strategist import content_strategist
from agno_agents.copywriter import copywriter
from agno_agents.visual_creator import visual_creator
from agno_agents.insta_team import insta_team_agent
# from agno_agents.insta_team import insta_team
load_dotenv()


class InstagramContentWorkflow(Workflow):
    market_researcher : Agent =  market_researcher

    insta_market_researcher = market_researcher
    insta_content_strategist = content_strategist
    insta_copy_writer = copywriter
    insta_visual_writer =  visual_creator
    report_agent = insta_team_agent
################ CREATING THE TEAM AGENT #######################
    # insta_marketing_team = insta_team
# ################ MAIN RUN METHOD ###############################
    def run(self, page_topic : str, weekly_topic: str)->Iterator[RunResponse]:
        logger.info(f"Generating Instagram Report on Insta topic: {page_topic} for the week {weekly_topic}")
        # logger.info(f"use cache: {use_cache}")
        searcher_response = self.insta_market_researcher.run(f"The instagram topic is {page_topic} follow by the weekly topic {weekly_topic}")
        content_response = self.insta_content_strategist.run(f"The market research findings are {searcher_response.content} create the weekly strategist on this findings.")
        copywriter =  self.insta_copy_writer.run(f"Here is the weekly content calendar {content_response.content}")
        visual_reponse = self.insta_visual_writer.run(f"Here is the weekly content calendar {content_response.content}")
        response = self.report_agent.run(f"Give me the final Instagram weekly content report based on,"
                                        f"Instagram Researcher:{searcher_response.content},"
                                        f"Instagram Content Strategist:{content_response.content},"
                                        f"Instagram Copy Write:{copywriter.content},"
                                        f"Instagram Visual Creator:{visual_reponse.content},")
        yield RunResponse(content=response.content , event=RunEvent.workflow_completed)

    # Initialize workflow
workflow = InstagramContentWorkflow(
    name="Instagram Weekly Content Report",
    workflow_id=f'generate_weekly_content_report'
)
    
app =  Playground(
    agents=[
        market_researcher,
        content_strategist,
        copywriter,
        visual_creator,
        insta_team_agent

    ],
    workflows=[
        workflow
    ]
).get_app()

################ RUNNING THE CODE ##############################

if __name__ == "__main__":
    # serve_playground_app('main:app' ,reload=True)

    try:
        # Define the page and topic
        page_topic = "Castle"  # Instagram page topic
        weekly_topic = "Castle in Germany"  # Content focus for the week
        
        # Run the workflow
        report:RunResponse= workflow.run(
            page_topic=page_topic, 
            weekly_topic=weekly_topic
        )

        # Print the results
        pprint_run_response(report, markdown=True, show_time=True)
        
    except Exception as e:
        logger.warning(e)

