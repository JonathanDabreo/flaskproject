from flask import Flask, request, render_template

app = Flask(_name_)


@app.route("/")
def add():
    return render_template('palin.html')


@app.route("/result", methods=['POST', 'GET'])
def calc():
    if request.method == 'POST':
        result = request.form
        st = result['pal']

        if st == st[::-1]:
            res = "String is palindrome"

        else:
            res = "String is not palindrome"

        return render_template("result.html", res=res)


if __name__ == '__main__':
    app.run(debug=True)