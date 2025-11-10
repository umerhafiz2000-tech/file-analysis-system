def split_text(text, chunk_size=500):
    """Split text into chunks of approx. `chunk_size` characters"""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
