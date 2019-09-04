from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return """
    <h1>Hello user</h1>
    <img src="https://image.flaticon.com/icons/svg/817/817397.svg" height="250" width="250">
    <h1> Hi my name is Lorraine, click the tabs to know what I like and for more logos :) enjoy.
    <p><a href="/sida2"title ="Síða 2">Síða 2</a> | <a href="/sida3"title ="Síða 3">Síða 3</a></p>
    """

@app.route("/sida2")
def sida2():
    return"""
    <h1>Hello user</h1>
    <img src="https://image.flaticon.com/icons/svg/2033/2033324.svg" height="250" width="250">
    <h1> I really love ice cream. Click the tabs to see more logo :)
    <p><a href="/"title ="Síða 1">Síða 1</a> | <a href="/sida3"title ="Síða 3">Síða 3</a></p>
    """
@app.route("/sida3")
def sida3():
    return"""
    <h1>Hello user</h1>
    <img src="https://image.flaticon.com/icons/svg/2056/2056060.svg" height="250" width="250">
    <h1> I love strawberry shake
    <p> Thanks for checking out my website ;)
    <p><a href="/"title ="Síða 1">Síða 1</a> | <a href="/sida2"title ="Síða 2">Síða 2</a></p>
    """

if __name__ == "__main__":
	app.run()
