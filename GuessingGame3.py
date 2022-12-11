from flask import Flask, request

app = Flask(__name__)

HTML_FIRST = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>Imagine number between 0 and 1000</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}">
    <input type="hidden" name="max" value="{}">
    <input type="submit" value="OK">
</form>
</body>
</html>
"""

HTML_MAIN = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>It is number {guess}</h1>
<form action="" method="POST">
    <input type="submit" name="user_answer" value="too big">
    <input type="submit" name="user_answer" value="too small">
    <input type="submit" name="user_answer" value="you won">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
"""

HTML_THIRD = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>

<h1>Hurra! I guess! Your number is {guess}</h1>
</body>
</html>

"""

@app.route("/guessinggame", methods=['GET', 'POST'])
def guess_number():
    if request.method == 'GET':
        return HTML_FIRST.format(0, 1000)

    else:
        min_num = int(request.form.get("min"))
        max_num = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 600))

        if user_answer == "too big":
            max_num = guess
        elif user_answer == "too small":
            min_num = guess
        elif user_answer == "you won":
            return HTML_THIRD.format(guess=guess)

        guess = (max_num - min_num) // 2 + min_num

        return HTML_MAIN.format(guess=guess, min=min_num, max=max_num)

if __name__ == '__main__':

    app.run()
