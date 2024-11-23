from typing import Optional
from fastapi import FastAPI, BackgroundTasks


app = FastAPI()

# {urserver}/?text={text}&?lang={lang}

@app.get("/")
async def get_root(text: str, lang: Optional[str] = None, bgTasks: BackgroundTasks = None):
    """
    Route for GET requests to the root path.

    Args:
        text (str): The text to be processed.
        lang (str): The language of the text.
        bgTasks (BackgroundTasks): A collection of tasks to be executed in the background.

    Returns:
        dict: A dictionary containing the processed text and language.
    
    Tasks:
        TODO: Validate request
        TODO: Check if request is cached. If so, return cached response.
        TODO: Generate TTS
        TODO: Convert to WAV
        TODO: Cache response
        TODO: Schedule cache cleanup if needed
        TODO: Return WAV
    """

    


    return {"text": text, "lang": lang}