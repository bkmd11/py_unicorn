import webbrowser


def uni_launch(word):
    """I launch a google search with a givne word for unicorns"""
    webbrowser.open(f'https://www.google.com/search?q={word} unicorn&hl=en&tbm=isch')
