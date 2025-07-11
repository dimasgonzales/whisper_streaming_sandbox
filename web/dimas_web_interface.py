import logging
# import importlib.resources as resources

logger = logging.getLogger(__name__)

def get_web_interface_html():
    """Loads the HTML for the web interface using importlib.resources."""
    try:
        with open('/Users/dimas/source/sandbox/whisper_streaming_sandbox/web/live_transcription.html', 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error loading web interface HTML: {e}")
        return "<html><body><h1>Error loading interface</h1></body></html>"