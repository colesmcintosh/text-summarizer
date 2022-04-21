import os
from dotenv import load_dotenv
from transformers import pipeline


load_dotenv()

# Create Flask app
from flask import Flask, render_template, request

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

summerizer = pipeline("summarization")

@app.route("/", methods=["GET", "POST"])
def index():
    nlt_input = ''
    output = ''
    if request.method == "POST":
        statement = request.form.get("statement")

        summerized_text = summerizer(
        f'''{statement}''',
        min_length=len(statement.split()) // 4,
        max_length = len(statement.split()) // 2,
        do_sample=False
        )

        # Break the response into lines
        output = summerized_text[0]['summary_text']

        # Remove leading and trailing whitespace
        output = output.strip()

        nlt_input = statement.strip()


    
    return render_template("index.html", output=output, nlt_input=nlt_input)

if __name__ == "__main__":
    app.run()