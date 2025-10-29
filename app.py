import os
from typing import cast
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import json
from flask import jsonify
import sqlite3
from helpers import apology, login_required
from flask_session import Session
from flask import Flask, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def get_db_connection():
    conn = sqlite3.connect("project.db")
    conn.row_factory = sqlite3.Row  # Makes results behave like dicts
    return conn


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Set current user in session to a variable
    user_id = session["user_id"]
    # Execute SQL query
    conn = get_db_connection()
    query_result = conn.execute("SELECT activity, scale, duration, mood, focus, strftime('%Y', time) AS year, strftime('%m', time) AS month, strftime('%d', time) AS day FROM productivity WHERE user_id = ?", (user_id,)).fetchall()
    year_only = conn.execute("SELECT strftime('%Y', time) AS year_only FROM productivity WHERE user_id = ? GROUP BY year_only", (user_id,)).fetchall()
    month = conn.execute("SELECT strftime('%m', time) AS month_only FROM productivity WHERE user_id = ? GROUP BY month_only", (user_id,)).fetchall()
    day = conn.execute("SELECT strftime('%d', time) AS day_only FROM productivity WHERE user_id = ? GROUP BY day_only", (user_id,)).fetchall()
    conn.close()
    return render_template("index.html", year_only = year_only, month = month, day = day, query_result = query_result)



@app.route("/input", methods=["GET", "POST"])
@login_required
def input():
    """User productivity input"""
    # Check method
    if request.method == "POST":
        # Set current user in session to a variable
        user_id = session["user_id"]
        # Store value of user input in variable
        activity = request.form.get("activity")
        if not request.form.get("activity"):
            return apology("Please enter a completed activity")
        focus = request.form.get("focus")
        if not request.form.get("focus"):
            return apology("Please enter a completed your focus level for the activity")
        mood = request.form.get("mood")
        if not request.form.get("focus"):
            return apology("Please enter a completed your focus level for the activity")
        now = datetime.datetime.now()
        duration = request.form.get("duration")
        if not request.form.get("duration"):
            return apology("Please enter a completed duration for the activity")
        scale = request.form.get("scale")
        if not request.form.get("scale"):
            return apology("Please enter a completed productivity scale for the activity")
        conn = get_db_connection()
        conn.execute("INSERT INTO productivity (user_id, activity, focus, mood, time, duration, scale) VALUES(?, ?, ?, ?, ?, ?, ?)", (user_id, activity, focus, mood, now, duration, scale))
        conn.commit()
        conn.close()
        return redirect("/")

    else:
        user_id = session["user_id"]
        # Activity page
        conn = get_db_connection()
        activity = conn.execute("SELECT * FROM productivity WHERE user_id = ? GROUP BY activity", (user_id,)).fetchall()
        focus = conn.execute("SELECT * FROM productivity WHERE user_id = ? GROUP BY focus", (user_id,)).fetchall()
        mood = conn.execute("SELECT * FROM productivity WHERE user_id = ? GROUP BY mood", (user_id,)).fetchall()
        duration = conn.execute("SELECT * FROM productivity WHERE user_id = ? GROUP BY duration", (user_id,)).fetchall()
        scale = conn.execute("SELECT * FROM productivity WHERE user_id = ? GROUP BY scale", (user_id,)).fetchall()
        conn.close()
        return render_template("input.html", activity = activity, focus = focus, mood = mood, duration = duration, scale = scale)



@app.route("/history", methods=["GET", "POST"])
@login_required
def history():
    """Show history of transactions"""
    if request.method == "POST":
        year = request.form.get('year')
        month = request.form.get("month")
        day = request.form.get("day")
        user_id = session["user_id"]
        conn = get_db_connection()
        year_plot = conn.execute("SELECT activity, mood, focus, strftime('%Y', time) AS year, strftime('%m', time) AS month, strftime('%d', time) AS day, strftime('%H:%M:%S', time) AS time, ROUND(AVG(scale)) AS scale FROM productivity WHERE user_id = ? AND year = ? GROUP BY year, month", (user_id, year)).fetchall()
        month_plot = conn.execute("SELECT activity, mood, focus, strftime('%Y', time) AS year, strftime('%m', time) AS month, strftime('%d', time) AS day, strftime('%H:%M:%S', time) AS time, ROUND(AVG(scale)) AS scale FROM productivity WHERE user_id = ? AND year = ? AND month = ? GROUP BY month, day", (user_id, year, month)).fetchall()
        day_plot = conn.execute("SELECT activity, mood, focus, strftime('%Y', time) AS year, strftime('%m', time) AS month, strftime('%d', time) AS day, strftime('%H:%M:%S', time) AS time, scale FROM productivity WHERE user_id = ? AND year = ? AND month = ? AND day = ?", (user_id, year, month, day)).fetchall()
        conn.close()
        # Combine the data from both queries into a single dictionary
        data = {'year_plot': year_plot, 'month_plot': month_plot, 'day_plot': day_plot}

        # Return a JSON response if this is an AJAX request
        return jsonify(data)
    else:
        user_id = session["user_id"]


        # Display activity history
        conn = get_db_connection()
        history = conn.execute("SELECT * FROM productivity WHERE user_id = ?", (user_id,)).fetchall()
        graph_value = conn.execute("SELECT COUNT(activity) AS total, SUM(duration) AS duration, activity FROM productivity WHERE user_id = ? GROUP BY activity", (user_id,)).fetchall()
        scale_plot = conn.execute("SELECT activity, mood, focus, strftime('%Y', time) AS year, strftime('%m', time) AS month, strftime('%d', time) AS day, strftime('%H:%M:%S', time) AS time, scale FROM productivity WHERE user_id = ?", (user_id,)).fetchall()
        year_only =  conn.execute("SELECT strftime('%Y', time) AS year_only FROM productivity WHERE user_id = ? GROUP BY year_only", (user_id,)).fetchall()
        month_only = conn.execute("SELECT strftime('%m', time) AS month_only FROM productivity WHERE user_id = ? GROUP BY month_only", (user_id,)).fetchall()
        day_only = conn.execute("SELECT strftime('%d', time) AS day_only FROM productivity WHERE user_id = ? GROUP BY day_only", (user_id,)).fetchall()
        conn.close()
        return render_template("history.html", history = history, graph_value = graph_value, scale_plot = scale_plot, year_only = year_only, month_only = month_only, day_only = day_only)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        
        conn = get_db_connection()
        # Query database for username
        rows_cur = conn.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),))
        rows = rows_cur.fetchall()
        conn.close()
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password") or ""):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Check submission
    if request.method == "POST":
        # Check fields
        if not request.form.get("username"):
            return apology("must provide username", 400)

        elif not request.form.get("password"):
            return apology("must provide password", 400)

        else:
            # Storing fields data
            username = request.form.get("username")
            # Check if the user exsists
            conn = get_db_connection()
            existing_users = conn.execute("SELECT username FROM users").fetchall()
            conn.close()
            for user in existing_users:
                if user["username"] == username:
                    return apology("username already exists", 400)
            # Check if the password and password confirmation fields match, hash the password and store the hash with the username
            password = cast(str, request.form.get("password"))
            password_confirmation = request.form.get("confirmation")
            if password != password_confirmation:
                return apology("password does not match", 400)
            password_hash = generate_password_hash(password)
            conn = get_db_connection()
            conn.execute("INSERT INTO users (username, hash) VALUES(?, ?)", (username, password_hash))
            conn.commit()
            conn.close()
            # Log in
            return redirect("/")

    else:
        return render_template("register.html")

@app.route("/analytics", methods=["GET", "POST"])
@login_required
def analytics():
    """Show history of transactions"""
    if request.method == "POST":
        user_id = session["user_id"]
        year = request.form.get('yearPie')
        month = request.form.get("monthPie")
        day = request.form.get("dayPie")
        conn = get_db_connection()
        if year and not month and not day:
            pie_chart = conn.execute("SELECT activity, COUNT(activity) AS total, mood, focus, SUM(duration) AS duration, strftime('%Y', time) AS year FROM productivity WHERE user_id = ? AND year = ? GROUP BY activity", (user_id, year)).fetchall()
        elif year and month and not day:
            pie_chart = conn.execute("SELECT activity, COUNT(activity) AS total, mood, focus, SUM(duration) AS duration, strftime('%Y', time) AS year, strftime('%m', time) AS month FROM productivity WHERE user_id = ? AND year = ? AND month = ? GROUP BY activity", (user_id, year, month)).fetchall()
        else:
            pie_chart = conn.execute("SELECT activity, COUNT(activity) AS total, mood, focus, SUM(duration) AS duration, strftime('%Y', time) AS year, strftime('%m', time) AS month, strftime('%d', time) AS day, strftime('%H:%M:%S', time) AS time, ROUND(AVG(scale)) AS scale FROM productivity WHERE user_id = ? AND year = ? AND month = ? AND day = ? GROUP BY activity", (user_id, year, month, day)).fetchall()
        conn.close()
        results = [dict(row) for row in pie_chart]

# Convert the list of dictionaries to a JSON object
        json_pie_chart = json.dumps(results)

# Return the JSON response
        return jsonify(json_pie_chart)
        # Return a JSON response if this is an AJAX request

    else:
        user_id = session["user_id"]

        # Display anyalitics with ploty
        conn = get_db_connection()
        history = conn.execute("SELECT * FROM productivity WHERE user_id = ?", (user_id,)).fetchall()
        pie_chart = conn.execute("SELECT COUNT(activity) AS total, SUM(duration) AS duration, activity FROM productivity WHERE user_id = ? GROUP BY activity", (user_id,)).fetchall()
        year_only = conn.execute("SELECT strftime('%Y', time) AS year_only FROM productivity WHERE user_id = ? GROUP BY year_only", (user_id,)).fetchall()
        month_only = conn.execute("SELECT strftime('%m', time) AS month_only FROM productivity WHERE user_id = ? GROUP BY month_only", (user_id,)).fetchall()
        day_only = conn.execute("SELECT strftime('%d', time) AS day_only FROM productivity WHERE user_id = ? GROUP BY day_only", (user_id,)).fetchall()
        conn.close()
        return render_template("analytics.html", history = history, pie_chart = pie_chart, year_only = year_only, month_only = month_only, day_only = day_only)