import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_movies")
def get_movies():
    movies = list(mongo.db.movies.find())

    avg_rating = mongo.db.movies.aggregate([{"$unwind": "$ratings"}, 
        {"$group": {"_id": "$title", "average": {"$avg": "$ratings.rating"}}}])
    for avg in avg_rating:
        print(avg)

    for movie in movies:
        # convert user and genre's ID to username and genre_name for display
        user = mongo.db.users.find_one({'_id': movie['created_by']})
        genre = mongo.db.genres.find_one({'_id': movie['genre']})
        movie['created_by'] = user['username']
        movie['genre'] = genre['genre_name']

        #for avg in avg_rating:
           # if str(avg['_id']) == movie['title']:
            #    movie['ratings'] = avg['average']

    return render_template("movies.html", movies=movies)


@app.route("/search", methods=["GET", "POST"])
def search():

    query = request.form.get("query")
    movies = list(mongo.db.movies.find({"$text": {"$search": query}}))
    return render_template("movies.html", movies=movies)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
            
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        # username doesn't exist
        else:
            flash("Incorrect Username and/or Password")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        # connect movie to user who posted it through user's ID
        user = mongo.db.users.find_one({'username': session["user"]})
        # connect movie to genre through genre's ID
        genre = mongo.db.genres.find_one(
            {'genre_name': request.form.get("genre_name")})
        movie = {
            "title": request.form.get("title"),
            "cover_image": request.form.get("cover_image"),
            "director": request.form.get("director"),
            "genre": ObjectId(genre['_id']),
            "plot": request.form.get("plot"),
            "year": request.form.get("year_release"),
            "created_by": ObjectId(user['_id'])
        }
        mongo.db.movies.insert_one(movie)
        flash("Thank you, movie successfully added!")
        return redirect(url_for("get_movies"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_movie.html", genres=genres)


@app.route("/edit_movie/<movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({'username': session["user"]})
        genre = mongo.db.genres.find_one(
            {'genre_name': request.form.get("genre_name")})
        edmovie = {
            "title": request.form.get("title"),
            "cover_image": request.form.get("cover_image"),
            "director": request.form.get("director"),
            "genre": ObjectId(genre['_id']),
            "plot": request.form.get("plot"),
            "year": request.form.get("year_release"),
            "created_by": ObjectId(user['_id'])
        }
        mongo.db.movies.update({"_id": ObjectId(movie_id)}, edmovie)
        flash("Thank you, movie successfully updated!")
        return redirect(url_for("get_movies"))

    movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_movie.html", movie=movie, genres=genres)


@app.route("/delete_movie/<movie_id>")
def delete_movie(movie_id):
    mongo.db.movies.remove({"_id": ObjectId(movie_id)})
    flash("Movie sucessfully deleted!")
    return redirect(url_for("get_movies"))


@app.route("/get_genres")
def get_genres():
    genres = list(mongo.db.genres.find().sort("category_name", 1))
    return render_template("genres.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        genre_upd = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, genre_upd)
        flash("Genre Updated")
        return redirect(url_for("get_genres")),

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre sucessfully deleted!")
    return redirect(url_for("get_genres"))


@app.route("/rate_movie/<movie_id>/<movie_title>", methods=["GET", "POST"])
def rate_movie(movie_id, movie_title):
    rating = int(request.form.get("rating"))
    user = mongo.db.users.find_one({'username': session["user"]})
    user_id = ObjectId(user['_id'])
    existing_rating = mongo.db.movies.find_one(
        {"_id": ObjectId(movie_id), "ratings.user": user_id})

    # https://stackoverflow.com/questions/10522347/mongodb-update-objects-in-a-documents-array-nested-updating
    if existing_rating:
        mongo.db.movies.update({"_id": ObjectId(movie_id),
            "ratings.user": user_id}, {"$set": {"ratings.$.rating": rating}})
        flash("Rating Updated")
    else:
        mongo.db.movies.update({"_id": ObjectId(movie_id)}, {"$push": {
            "ratings": {"rating": rating, "user": user_id}}})
        flash("Rating Added")

    avg_rating = mongo.db.movies.aggregate([{"$unwind": "$ratings"}, {"$group": {"_id": "$title", "average": {"$avg": "$ratings.rating"}}}])
    avg_var = {}
    for avg in avg_rating:
        if str(avg["_id"]) == movie_title:
            avg_var = avg
            print(avg_var)
    mongo.db.movies.update({"_id": ObjectId(movie_id)}, {"$set": {"average": avg_var}})

    return redirect(url_for('get_movies'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
