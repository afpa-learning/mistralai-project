from dotenv import load_dotenv
from mistralai import Mistral
import os
import re
import webbrowser
from pathlib import Path
import base64

def get_response_output_text(input: str, image_path: str):
    
    load_dotenv()

    encoded_image = encode_image(image_path)
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": input
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{encoded_image}"
                }
            ]
        }
    ]

    mistralai_api_key = os.getenv("MISTRAL_API_KEY")

    with Mistral(
        api_key=os.getenv("MISTRAL_API_KEY", mistralai_api_key),
    ) as mistral:

        res = mistral.chat.complete(model="mistral-small-latest", messages=messages
        , stream=False)
        
        print(res.choices[0].message.content)
        
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


def extract_css_from_text(text: str):
    """Extract an CSS code block from text; fallback to first code block, else full text."""
    css_block = re.search(r"```css\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    
    if css_block:
        result = css_block.group(1)
        return result
    any_block = re.search(r"```\s*(.*?)\s*```", text, re.DOTALL)
    if any_block:
        result = any_block.group(1)
        return result
    return text


def save(content: str, filename: str) -> Path:
    """Save content to outputs/ directory and return the path."""
    try:
        base_dir = Path(__file__).parent
    except NameError:
        base_dir = Path.cwd()

    folder = "outputs"
    outputs_dir = base_dir / folder
    outputs_dir.mkdir(parents=True, exist_ok=True)

    output_path = outputs_dir / filename
    output_path.write_text(content, encoding="utf-8")
    return output_path

def open_in_browser(path: Path) -> None:
    """Open a file in the default browser (macOS compatible)."""
    try:
        webbrowser.open(path.as_uri())
    except Exception:
        os.system(f'open "{path}"')

# Function to encode the image
def encode_image(image_path: str):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
        
def make_website_and_open_in_browser(*, website_input: str, image_path: str, filename: str = "website.html"):
    response_text = get_response_output_text(website_input,image_path)
    css = extract_css_from_text(response_text)
    output_path = save(css, "styles.css")
    html = extract_html_from_text(response_text)
    output_path = save(html, filename)
    open_in_browser(output_path)


make_website_and_open_in_browser(
    website_input="Can you make a login page for this website that maintains the same theme of this image",
    image_path="input_image.png",
    filename="login_page.html",
)