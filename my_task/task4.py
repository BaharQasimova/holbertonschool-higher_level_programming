from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

def fetch_api_data():
    api_url = "https://api.example.com/v1/articles"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def style_to_html(text_fragment):
    text = text_fragment["text"]
    style = text_fragment.get("style", "normal")
    if style == "bold":
        return f"<strong>{text}</strong>"
    elif style == "italic":
        return f"<em>{text}</em>"
    elif style == "subscript":
        return f"<sub>{text}</sub>"
    elif style == "superscript":
        return f"<sup>{text}</sup>"
    elif style == "deleted":
        return f"<del>{text}</del>"
    elif style == "inserted":
        return f"<ins>{text}</ins>"
    else:
        return text

def json_to_html(data):
    html = f"<h1>{data['title']}</h1>\n"
    for paragraph in data["content"]:
        if paragraph["type"] == "paragraph":
            paragraph_html = ""
            for fragment in paragraph["text"]:
                paragraph_html += style_to_html(fragment)
            html += f"<p>{paragraph_html}</p>\n"
    return html

@app.route("/")
def index():
    try:
        data = fetch_api_data()
        html_content = json_to_html(data)
    except requests.RequestException as e:
        html_content = f"<p>Xəta baş verdi: {e}</p>"

    return render_template("index.html", content=html_content) 

if __name__ == "__main__":
    app.run(debug = True)

