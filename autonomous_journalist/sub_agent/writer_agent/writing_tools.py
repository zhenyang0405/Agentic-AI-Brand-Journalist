import requests
import re
from bs4 import BeautifulSoup

def draft_post_from_research_brief(research_brief: str, writing_style: str) -> str:
    """
    Parses a research brief to find URLs, scrapes the content from the first
    relevant URL, and prepares a prompt for drafting a blog post.

    Args:
        research_brief: A Markdown-formatted brief with summaries and URLs.
        writing_style: The desired style (e.g., 'professional', 'casual', 'witty').

    Returns:
        The drafted blog post as a string.
    """
    # Find all URLs in the research brief
    urls = re.findall(r'https?://[^\s)]+', research_brief)
    if not urls:
        return "Error: No URLs found in the research brief to scrape."

    # For this example, we'll scrape the first URL.
    # A more advanced version could let the agent choose the best URL.
    target_url = urls[0]

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        scraped_text = "\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])

        if not scraped_text:
            return f"Error: Could not extract content from {target_url}."

        # Return a package of information for the agent to use for the final draft.
        return f"""**Research Brief:**
{research_brief}

**Scraped Content from {target_url}:**
{scraped_text[:2000]}

**Drafting Instructions:**
Using the full research brief for context and the scraped content for details, write a compelling blog post in a {writing_style} tone.
"""

    except requests.RequestException as e:
        return f"Error: Could not access the URL {target_url}. {e}"
    except Exception as e:
        return f"Error: Failed to process content from {target_url}. {e}"
