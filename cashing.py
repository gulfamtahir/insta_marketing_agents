# FUTURE IMPLEMENTATION

# if team_response is not None and team_response.content:
        #     yield RunResponse(
        #     run_id=self.run_id,
        #     content=team_response.content,
        #     event=RunEvent.workflow_completed
        # )
        # else:
        #     yield RunResponse(
        #     run_id=self.run_id,
        #     content="Failed to generate Instagram report",
        #     event=RunEvent.workflow_failed)

        # yield from self.insta_marketing_team.run(f"Do market reserach of this site:Instagram {page_topic}for the {weekly_topic}", stream=True) 
################ CACHING MECHANISM #############################
#     def add_report_to_cache(self , page_topic : str,  weekly_topic: str)->None:
#         logger.info(f"Caching the Instagram Topic report for the topic: {page_topic}")
#         self.session_state.setdefault("insta_topic", [])
#         self.session_state['insta_topic']['page_topic'] = weekly_topic
#         logger.info(f"Instagram report cached successfully for the topic: {page_topic}")
    
#     def get_cached_insta_report(self, page_topic: str)-> str:
#         logger.info(f"checking cache for the report of the topic: {page_topic}")
#         cached_report = self.session_state.get('insta_topic' ,[]).get(page_topic)

#         if cached_report:
#             logger.info(f"Cache hit for the Insta topic: {page_topic}")
#         else:
#             logger.info(f"No cache blog post found for the topic: {page_topic}")
#         return cached_report
    
#     def _get_search_results(self, insta_topic: str) -> str:
#         MAX_ATTEMPTS = 3
#         for attempt in range(MAX_ATTEMPTS) :
#             try:
#                 logger.info(f"Attempt {attempt + 1}: Searching for articles on '{insta_topic}'")
#                 searcher_response: RunResponse = self.market_researcher.run(insta_topic)
#                 if(searcher_response is not None and searcher_response.content is not None ):
#                     article_count = len(searcher_response.content.articles)
#                     logger.info(
#                         f"Found {article_count} articles on attempt {attempt + 1}"
#                     )
#                     return searcher_response.content
#                 else:
#                     logger.warning(
#                         f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: Invalid response type"
#                     )
#             except Exception as e:
#                 logger.warning(f"Attempt {attempt + 1} failed with error: {e}")
#         logger.error(f"Failed to retrieve search results for '{insta_topic}' after {MAX_ATTEMPTS} attempts") 
#         return None
#     def write_report(self , topic: str , search_results : List)->Iterator[RunResponse]:
#         pass