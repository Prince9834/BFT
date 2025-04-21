from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
  <head>
    <title>Best Friend Test</title>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7442843163769118"
     crossorigin="anonymous"></script>
  </head>
  <body>
    <h2>Best Friend Test</h2>
    <form method="post">
      <label>Q1: What is your name?</label><br>
      <input type="text" name="name"><br><br>

      <label>Q2: What is your age?</label><br>
      <input type="number" name="age"><br><br>

      <label>Q3: Do you like movies? (Yes/No)</label><br>
      <input type="text" name="movies"><br><br>

      <label>Q4: Do you like music? (Yes/No)</label><br>
      <input type="text" name="music"><br><br>

      <label>Q5: Do you like me as a friend? (Yes/No)</label><br>
      <input type="text" name="friend"><br><br>

      <input type="submit" value="Submit">
    </form>
    <br>
    <div>{{ result }}</div>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def quiz():
    result = ""
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        movies = request.form.get('movies')
        music = request.form.get('music')
        friend = request.form.get('friend')

        result += f"Hello {name}<br>"
        result += "Correct name!<br>" if name == "Tejas Khandelwal" else "Kuch bhi...<br>"
        result += "Hope you are not lying<br>" if age < 18 else "Liar<br>"
        result += "Good<br>" if movies == "Yes" else "You don’t deserve to be<br>"
        result += "Good, keep going<br>" if music == "Yes" else "I did not know that<br>"

        if friend == "Yes":
            result += "CONGRATULATIONS! You are my best friend. Transfer your 80% wealth to my account<br>"
        else:
            result += "You broke my heart. Never talk to me again.<br>"

        result += "<br>Thank you for taking the test!<br>This is just a joke."

    return render_template_string(html, result=result)

if __name__ == '__main__':
    app.run(debug=True)
