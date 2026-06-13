from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults


@tool
def search_web_tool(query: str) -> str:
    """
    Search the web using DuckDuckGo and return results.
    """

    search = DuckDuckGoSearchResults(
        num_results=10,
        verbose=True
    )

    return search.run(query)