#!/usr/bin/env python

# Project: tram_audio_server
# Package: bpe_tram_audio_server
# Description: This is an example of a server for providing TTS services; taking text and returning audio. Intended for the Minecraft mod Create Tram Additions.
# Author: BipolarExpedition(Doc1979)
# Email: lastdoc39@gmail.com
# License: MIT
# Repository (if exists): "https://github.com/BipolarExpedition/tram_audio_server"

import uvicorn
#from bpe_tram_audio_server.app import app

"""
A CLI interface for tram_audio_server.

File is bpe_tram_audio_server.cli.py
"""

# Main function for CLI handling
def main():
    # Run the webapp 'app' with uvicorn
    uvicorn.run("bpe_tram_audio_server.app:app", host="0.0.0.0", port=8013, log_level="debug", reload=True)

if __name__ == "__main__":
    main()
