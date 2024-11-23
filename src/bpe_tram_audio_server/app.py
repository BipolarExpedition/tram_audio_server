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
        lang (Optional[str]): The language of the text. Optional.
        bgTasks (BackgroundTasks): A collection of tasks to be executed in the background. Optional.

    Returns:
        dict: A dictionary containing the processed text and language.
    
    Tasks:
        TODO: #1 Validate request
        TODO: #2 Check if request is cached. If so, return cached response.
        TODO: #3 Generate TTS
        TODO: #4 Convert to WAV
        TODO: #5 Cache response
        TODO: #6 Schedule cache cleanup if needed
        TODO: #7 Return WAV
    """

    


    return {"text": text, "lang": lang}