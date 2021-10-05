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

    for movie in movies:
        user = mongo.db.users.find_one({'_id': movie['created_by']})
        genre = mongo.db.genres.find_one({'_id': movie['genre']})
        movie['created_by'] = user['username']
        movie['genre'] = genre['genre_name']

    return render_template("movies.html", movies=movies)


@app.route("/search", methods=["GET", "POST"])
def search():

    query = request.form.get("query")
    movies = list(mongo.db.movies.find({"$text": {"$search": query}}))
    for movie in movies:
        user = mongo.db.users.find_one({'_id': movie['created_by']})
        genre = mongo.db.genres.find_one({'_id': movie['genre']})
        movie['created_by'] = user['username']
        movie['genre'] = genre['genre_name']

    return render_template("movies.html", movies=movies)


@app.route("/register", methods=["GET", "POST"])
def register():
    password = request.form.get("password")
    confirm_password = request.form.get("passwordConfirm")

    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if password == confirm_password:
            register = {
                "username": request.form.get("username").lower(),
                "email": request.form.get("userEmail"),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(register)

            session["user"] = request.form.get("username").lower()
            user_email = mongo.db.users.find_one(
                {"username": session['user']})['email']
            flash("Registration Successful!")
            return redirect(url_for("profile", username=session["user"],
                                    user_email=user_email))
        else:
            flash("Passwords must match")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                user_email = mongo.db.users.find_one(
                    {"username": session['user']})['email']
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"],
                    user_email=user_email))
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

    movies = list(mongo.db.movies.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    # Checks if the current user has uploaded any movie
    movie_user = mongo.db.movies.find_one({'created_by': user_id})

    # ----- Look at the bottom of the page for comments -----
    for movie in movies:
        if movie['created_by'] != user_id:
            continue
        else:
            movie['created_by'] = username

    if session["user"]:
        user_email = mongo.db.users.find_one(
            {"username": session['user']})['email']
        return render_template("profile.html", username=username,
                               user_email=user_email, movies=movies,
                               movie_user=movie_user)

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
        # connect movie to genre using genre's ID
        genre = mongo.db.genres.find_one(
            {'genre_name': request.form.get("genre_name")})
        movie = {
            "title": request.form.get("title"),
            "cover_image": request.form.get("cover_image"),
            "director": request.form.get("director"),
            "genre": ObjectId(genre['_id']),
            "plot": request.form.get("plot"),
            "year": request.form.get("year_release"),
            "created_by": ObjectId(user['_id']),
            "ratings": [],
            "average": [],
            "comments": []
        }
        mongo.db.movies.insert_one(movie)
        flash("Thank you, movie successfully added!")
        return redirect(url_for("get_movies"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_movie.html", genres=genres)


@app.route("/edit_movie/<movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    if request.method == "POST":

        genre = mongo.db.genres.find_one(
            {'genre_name': request.form.get("genre_name")})
        # Variable created to prevent name of user who posted the movie from..
        # ..changing once admin edits it
        movie = mongo.db.movies.find_one(
            {'_id': ObjectId(movie_id)})["created_by"]
        user = mongo.db.users.find_one({'_id': movie})
        # Variables created to prevent ratings and comments..
        # ..from disappearing after movie is edited
        ratings = mongo.db.movies.find_one(
            {"_id": ObjectId(movie_id)})['ratings']
        average = mongo.db.movies.find_one(
            {"_id": ObjectId(movie_id)})['average']
        comments = mongo.db.movies.find_one(
            {"_id": ObjectId(movie_id)})['comments']

        edmovie = {
            "title": request.form.get("title"),
            "cover_image": request.form.get("cover_image"),
            "director": request.form.get("director"),
            "genre": ObjectId(genre['_id']),
            "plot": request.form.get("plot"),
            "year": request.form.get("year_release"),
            "created_by": ObjectId(user['_id']),
            "ratings": ratings,
            "average": average,
            "comments": comments
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
    flash("Movie sucessfully deleted")
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
        return redirect(url_for("get_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    movie_genre = mongo.db.movies.find_one({"genre": ObjectId(genre_id)})

    if movie_genre:
        flash("Remove all movies related to a genre before deleting it")
    else:
        mongo.db.genres.remove({"_id": ObjectId(genre_id)})
        flash("Genre sucessfully deleted!")

    return redirect(url_for("get_genres"))


@app.route("/rate_movie/<movie_id>/<movie_title>", methods=["GET", "POST"])
def rate_movie(movie_id, movie_title):
    rating = int(request.form.get("rating"))
    user = mongo.db.users.find_one({'username': session["user"]})
    user_id = ObjectId(user['_id'])
    # variable containing average of ratings for specific movie
    movie_rating_avg = {}

    # Check if user has already reated the movie
    existing_rating = mongo.db.movies.find_one(
        {"_id": ObjectId(movie_id), "ratings.user": user_id})

    # https://stackoverflow.com/questions/10522347/mongodb-update-objects-in-a-documents-array-nested-updating
    # If rating from user already exists, update it
    if existing_rating:
        mongo.db.movies.update({"_id": ObjectId(movie_id),
                                "ratings.user": user_id}, {
                                    "$set": {"ratings.$.rating": rating}})
        flash("Rating Updated")
    else:
        # If user has not rated the movie yet, add new rating
        mongo.db.movies.update({"_id": ObjectId(movie_id)}, {"$push": {
            "ratings": {"rating": rating, "user": user_id}}})
        flash("Rating Added")

    # https://stackoverflow.com/questions/34159487/mongodb-calculating-average-of-nested-array-of-objects-attributes
    # Calculate average of ratings for each movie
    avg_ratings = mongo.db.movies.aggregate(
        [{"$unwind": "$ratings"}, {"$group": {
            "_id": "$title", "average": {"$avg": "$ratings.rating"}}}])

    # Loop through each rating average and assign it to correct movie
    for avg in avg_ratings:
        if str(avg["_id"]) != movie_title:
            continue
        else:
            movie_rating_avg = avg

    # https://stackoverflow.com/questions/15666169/python-pymongo-how-to-insert-a-new-field-on-an-existing-document-in-mongo-fro
    # Update the field (Object) "average" in movies collection
    mongo.db.movies.update(
        {"_id": ObjectId(movie_id)}, {"$set": {"average": movie_rating_avg}})

    return redirect(url_for('get_movies'))


@app.route("/add_comment/<movie_id>", methods=["POST", "GET"])
def add_comment(movie_id):
    comment = request.form.get("comment")
    user = mongo.db.users.find_one({'username': session["user"]})['username']

    # add comment to comments array
    mongo.db.movies.update({"_id": ObjectId(movie_id)}, {"$push": {
        "comments": {"comment": comment, "user": user}}})

    flash("Thanks for you comment!")
    return redirect(url_for('get_movies'))


@app.route("/delete_comment/<movie_id>/<comment_id>/<user_id>")
def delete_comment(movie_id, comment_id, user_id):
    # https://stackoverflow.com/questions/27471439/mongodb-using-pull-to-delete-dictionary-in-an-array-sub-document/27471525
    # Remove specific comment from "comments" array
    mongo.db.movies.update({"_id": ObjectId(movie_id)}, {
        '$pull': {"comments": {"comment": comment_id, "user": user_id}}})

    flash("Comment deleted")
    return redirect(url_for("get_movies"))


# Error handlers
@app.errorhandler(404)
def error_400(e):
    return render_template('error.html'), 404


@app.errorhandler(500)
def error_500(e):
    return render_template('error.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
