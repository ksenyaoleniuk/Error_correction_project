from flask import Flask, render_template, request
import random
from Error_correction import ErrorCorrection
from Error_correction import main

app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def get_index():
     try:
         if request.method == "POST":
             message = request.form['input']
             print(message)
             wrong, right, error_bits, bin_str = main(message)
             return render_template('error.html', message=message, wr_solution=wrong, r_solution=right)
         else:
             return render_template('error.html')
     except:
         return render_template('error.html', error_message="This data type is incorrect.", message=message)


if __name__ == "__main__":
    app.run(debug=True)