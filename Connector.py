# # import os
# # import subprocess
# # import sys
# #
# # import openai
# # from flask import Flask, render_template, request
# #
# # app = Flask(__name__)
# #
# #
# # @app.route("/", methods=["GET", "POST"])
# # def index():
# #     if request.method == "POST":
# #         prompt = request.form["prompt"]
# #         print(prompt)
# #         script_path = os.path.join(os.path.dirname(__file__), "main.py")
# #         subprocess.run([sys.executable, script_path])
# #     return render_template("index.html",)
# #
# #
# # if __name__ == "__main__":
# #     app.run(debug=True)
# import os
# import subprocess
# import sys
# import cv2
#
# from flask import Flask, request
#
# app = Flask(__name__)
#
#
# @app.route('/run_script', methods=['POST'])
# def run_script():
#     print("Hello")
#     # Add the code to run your desired Python script here
#     script_path = os.path.join(os.path.dirname(__file__), "main.py")
#     subprocess.run([sys.executable, script_path])
#     result = "HELLO WORLD"
#     return result
#
#
# @app.route('/terminate', methods=['POST'])
# def stop_script():
#     print("Hello")  # This line will execute
#     result = "HELLO WORLD"  # Assign the value to result
#     cv2.destroyAllWindows()
#     return result
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
import os
import subprocess
import sys
import cv2

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/run_script', methods=['POST'])
def run_script():
    print("Hello")
    # Add the code to run your desired Python script here
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    subprocess.run([sys.executable, script_path])
    result = "HELLO WORLD"
    return render_template('result.html', result=result)  # Render the template with the result

@app.route('/terminate', methods=['POST'])
def stop_script():
    print("Hello")
    result = "HELLO WORLD"
    cv2.destroyAllWindows()
    return render_template('result.html', result=result)  # Render the template with the result

if __name__ == '__main__':
    app.run(debug=True)

