import requests
from bs4 import BeautifulSoup

def fetch_puzzle_text(day, session_token):
    url = f"https://adventofcode.com/2024/day/{day}"
    cookies = {"session": session_token}
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()

    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")
    # The puzzle description is inside one or two <article class="day-desc"> elements
    articles = soup.find_all("article", class_="day-desc")

    # Extract text from each article and concatenate
    puzzle_text = "\n".join(article.get_text() for article in articles)

    return puzzle_text

if __name__ == "__main__":
    SESSION_TOKEN = ""
    day = 1
    text = fetch_puzzle_text(day, SESSION_TOKEN)
    print(text)
    with open(f"/puzzles/puzzle_day{day:02}.txt", "w", encoding="utf-8") as f:
        f.write(text)