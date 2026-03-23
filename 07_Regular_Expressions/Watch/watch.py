import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    Extracts a YouTube ID from an <iframe> tag and converts it to a short link.
    Ensures the link is within <iframe>...</iframe> and supports
    different URL formats (http, https, www, or direct).
    """
    if matches := re.search(
        r'<iframe.*src="https?://(?:www\.)?youtube\.com/embed/([^"]+)".*></iframe>', s
    ):
        video_id = matches.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None


if __name__ == "__main__":
    main()
