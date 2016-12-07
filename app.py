from flask import Flask, render_template, request
import random
from Error_correction import ErrorCorrection

app = Flask(__name__)

#deleted to_string()

@app.route('/', methods=["GET", "POST"])
def get_index():
     try:
         if request.method == "POST":
             message = request.form['input']
             print(message)
             correction = ErrorCorrection(message)
             return render_template('error.html', message=message, solution=correction.correct_errors(message))
         else:
             return render_template('error.html')
     except:
         return render_template('error.html', error_message="This data type is incorrect.")


if __name__ == "__main__":
    app.run(debug=True)