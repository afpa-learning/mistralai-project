from dotenv import load_dotenv
from mistralai import Mistral
import os
import re
import webbrowser
from pathlib import Path

def get_response_output_text(input: str):
    
    load_dotenv()

    mistralai_api_key = os.getenv("MISTRAL_API_KEY")

    with Mistral(
        api_key=os.getenv("MISTRAL_API_KEY", mistralai_api_key),
    ) as mistral:

        res = mistral.chat.complete(model="mistral-small-latest", messages=[
            {
                "content": input,
                "role": "user",
            },
        ], stream=False)

        # Handle response
        return res.choices[0].message.content


def extract_html_from_text(text: str):
    """Extract an HTML code block from text; fallback to first code block, else full text."""
    html_block = re.search(r"```html\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    
    if html_block:
        result = html_block.group(1)
        return result
    any_block = re.search(r"```\s*(.*?)\s*```", text, re.DOTALL)
    if any_block:
        result = any_block.group(1)
        return result
    return text


def save_html(html: str, filename: str) -> Path:
    """Save HTML to outputs/ directory and return the path."""
    try:
        base_dir = Path(__file__).parent
    except NameError:
        base_dir = Path.cwd()

    folder = "outputs"
    outputs_dir = base_dir / folder
    outputs_dir.mkdir(parents=True, exist_ok=True)

    output_path = outputs_dir / filename
    output_path.write_text(html, encoding="utf-8")
    return output_path

def open_in_browser(path: Path) -> None:
    """Open a file in the default browser (macOS compatible)."""
    try:
        webbrowser.open(path.as_uri())
    except Exception:
        os.system(f'open "{path}"')

def make_website_and_open_in_browser(*, website_input: str, filename: str = "website.html"):
    response_text = get_response_output_text(website_input)
    html = extract_html_from_text(response_text)
    output_path = save_html(html, filename)
    open_in_browser(output_path)


make_website_and_open_in_browser(
    website_input="Make me landing page for a retro-games store. Retro-arcade noir some might say",
    filename="retro_dark.html",
)