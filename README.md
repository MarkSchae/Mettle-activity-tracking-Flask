# METTLE
#### Video Demo:  <https://youtu.be/S0yhV934mv8>

# Hobby Productivity Tracker

A personal productivity and accountability web app designed to help users track the time they spend on hobbies, learning, and leisure activities outside of work. This app encourages self-reflection, accountability, and insight into how time is spent on meaningful pursuits.

## Overview

Unlike traditional work productivity trackers, this app focuses on **tracking free-time activities**. Users can log any activity, from learning a new skill or exercising to watching TV or taking naps. The app allows users to:

* Record activities along with time spent, focus level, and mood.
* Track and visualize patterns in their productivity and habits.
* Reflect on the balance between leisure and meaningful activities.
* Hold themselves accountable to their personal goals.

The core purpose is to **support users in staying accountable** for the time they dedicate to activities they care about, rather than replacing human motivation or support systems.

## Features

### Index Page

* **Timer**: Users can set a custom timer to remind them to log their recent activity. The timer asks, *"What have I been doing for the last X minutes?"*.

  * Implemented client-side using JavaScript `setTimeout()` and the Notification API.
  * Allows users to cancel or reset the timer easily by reloading the page.
  * Future improvements may include storing timer state in the database or adding recurring notifications.

* **Activity History Table**: Displays user activities filtered by year, month, and day using drop-down menus.

  * Rows are dynamically shown/hidden via JavaScript based on user selections.
  * Enables users to analyze their time allocation patterns quickly.

### Input Page

* Users can **log new activities**, including duration, focus, mood, and productivity scale.
* Previously entered values are shown in a `datalist` for faster input.
* Activity data is stored in the database and immediately reflected on the index page.

### History Page

* Shows the **full activity history** for the user.
* Users can filter by year, month, or day.
* Interactive scatter plots (using Plotly) visualize productivity trends over time.
* AJAX calls are used to dynamically fetch filtered data without page reloads.

### Analytics Page

* Displays **pie charts** showing breakdowns of activity time, mood, and focus.
* Charts update dynamically based on user-selected dates.
* Helps users understand how time is distributed across different activities.

### Future Vision

* **Social Accountability**: Connect users with others who have similar hobbies or goals. For example, exercise partners could motivate each other or schedule joint activities.
* **Enhanced Timer & Notifications**: Persistent timers and reminders stored in the database.
* **Expanded Data Visualization**: More insights, such as activity correlations, trends over weeks, and top productive hours.
* **Improved UX & Styling**: Aesthetic improvements and interactive dashboards.
* **Community Features**: Ability to share progress, form accountability groups, and support each other.

## Technical Details

* **Stack**: Flask (Python), SQLite, Jinja2, JavaScript, AJAX, Plotly.
* **Database**: SQLite stores users and productivity entries.
* **Session Management**: Server-side sessions via Flask-Session.
* **Front-End**: Jinja2 templates with embedded JavaScript for interactivity.
* **AJAX**: Used for dynamically updating scatter plots and pie charts without page reloads.
* **Notifications**: Client-side notifications alert users when the timer ends.

## Motivation

I created this app to **hold myself accountable** for my hobbies, learning, and self-improvement. I noticed that I often overestimate time spent on productive activities and underestimate leisure time. This tool provides:

* Self-reflection: Insight into how my time is spent.
* Accountability: Encouragement to stay consistent with activities I care about.
* Motivation: A way to track progress over time.

Ultimately, the app is intended to **support users who already want to be accountable**, helping them organize, visualize, and reflect on their personal time management.

## Installation & Usage

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd <project-folder>
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:

   ```bash
   flask run
   ```
4. Open your browser at `http://127.0.0.1:5000` and start tracking your activities.

---

## Acknowledgements

* Inspired by CS50’s finance app structure.
* Learning from hands-on experimentation with AJAX, Plotly, and Jinja2 templates.
* Emphasis on human-centered design for hobby and skill accountability.



