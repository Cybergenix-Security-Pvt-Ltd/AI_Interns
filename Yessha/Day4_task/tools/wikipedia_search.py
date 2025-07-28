# tools/wikipedia_search.py

import wikipedia

def search_wikipedia(query: str) -> str:
    try:
        summary = wikipedia.summary(query, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is too broad. Try one of these: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for that query."
    except Exception as e:
        return f"An error occurred: {str(e)}"
