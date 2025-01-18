import webbrowser

# List of URLs to open
urls = [
    "https://app.reclaim.ai/planner?taskSort=schedule",
    "https://calendar.google.com/calendar/u/0/r",
]

# Open each URL in the default web browser
for url in urls:
    webbrowser.open(url)
