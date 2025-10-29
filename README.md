# METTLE
#### Video Demo:  <https://youtu.be/S0yhV934mv8>
#### Description:

My web app is a type of prodictivity tracker. I wanted to make something that could potentially help people keep track of thier daily activities. This is different from a more traditional work prodictivity tracker. I wanted a tracker specifically to help me keep track of the time I spend on activities in my free time away from work. I enjoy challenging myself and learning new skills but found it difficult to keep track of how much time and effort I spend on certian activities. This also made holding myseld accountable difficult. I wanted a aid in keeping track not only of the time spent but also how I felt during the activity. So I decided to make a sort of hobby productivity and accountability app. The app at its core is very simple in that it provides the user with simple tools to track and sort their time spent on projects or any activity they choose to add.

The main idea of the app is that users can input any activities they choose to track. If that includes work, that is fine but I meant this more to help a user hold themselves accountable for thier time spent outside of work. For example if a user were to add TV and nap breaks to their database and be honest about how much time they spend engaging in these activities as well as how much time they spend doing thigs they actually care about such as exercise or learning a new skill then this app could help them be more accountable. No app can replace a users willingness to be accountable and actually engange in healthier persuits, this app is meant to be used as a tool for those already willing to be accountable so that they can assess their progress and committment. I essentially made this app for me as this is something I struggle with. I have so many skills I would like to learn outside of my full time job but I overexagerate how much time I spend learning and under estimate how much time I spend taking breaks or watching tv. The timer elements is also something I would benifit from in that I need to be reminded/ask myself what have I been doing for the last x min or hours. I also wanted to expand this into reminding the user of certian activities if they havent engaged in those activities for a certian time but I did not get around to that.

Lastly I would love to allow users to connect with each other based on their similar intrests in hobbies/skills because I do not think that this type of technology should exsit in a attempt to replace humans/support system but used as a tool to connect people with a potential support system. My vision is that for example if I connected with a person that is trying to exercise regularly that when that person is not feeling motivated I would help them by setting up a time that we could exercise together (in person or just at the same time or even through video chat, I understand that this type of connectivity comes with other challenges outside of just functionality) and discuss our progress after the session and then that poerson would do the same for me when I need it. In my experience people supporting people is the only way to ensure stable commitment to healthy activity. personal trianers still exsit no matter how much information there is about how to exercise and eat healthly. So perhaps what I wanted is a app that is a more intimate and hobby/skills learning/healthy lifestyle social networking and accountablility app not with the purpose of having internet friends that you never talk to but to truly connect with people in a win win situation. Perhaps a user can use the app to keep in touch with a friend or family member that has moved etc keeping the support system strong dispite not being able to see the person, that was the original untainted goal of all this technology when social media started, in my opnion anyway.

The main idea is to connect people that have similar intrests and help them hold each other accountable based on those intrests.

# Index:

There is a timer for the user to input a amount of minutes in which they can be reminded to input a acticity. I meant for this functionality almost to 'ask the user what they have been doing for the past x minutes'. I struggle to keep track of how long I am spending on certian tasks which leads to underestimating or over exagerating the amount of time spent working etc..I could have made the timer part of the database and in this way it would have been persistent but in my search for how to comminicate with the database and client side in order to get input from the user and not only store that input in the databse but to use the value of the varibale in javascript. I did not know what a AJAX request was which lead me to aquiring some new knowledge and different ways of doing what I wanted. I ended up leaving the timer to be handled serverside. The timer has to be set each time a user inputs a new activity. I am not sure if this is the right way to do this but its the first method I found before I found out about making AJAX requests. I also like the idea that the user has more control over the timer at any time they can effectivley cancell the timer and reset it by reloading the page. I also thoutht that if I didnt need another colomn in my database then just leave it as is but I can also see the arguement for having the timer be a variable in the database that is persistant. Having the timer persist may have also been irritating at times. I do think that if I understood AJAX requests and how to use them in javascript at the time of implementing the timer, it would have been much easier and quicker to implement the timer but I am happy that the misunderstanding led to a lot of searching and trying to understand server side and client side functionality and communication.

The timer is implemented as such:

First the user is asked for permission to send notifications.
The currentTimeout variable is set to keep track of the timer variable.

An event listener is added to the "Confirm" button. This function is called when the user clicks the button to trigger the notification timer.

The intervalTime variable is set to the users timer input.

Ny exsisting timer is clearded with the clearTimeout method in javascript. This is done to prevent multiple notifications from being created if the user changes the interval time before the timeout expires.

The displayNotification() function is defined. This function creates a new notification using the Notification API and sets an event listener for the "click" event. This event listener redirects the user to the input page so that they can input the activity that they were just working on.

A timeout is set using javacript built in finction of setTimeout. This calls the displayNotification() function after the specified interval time has elapsed.

When the user clicks on the notification, the click event listener inside the displayNotification() function is called. This event listener redirects the user to the specified URL using window.location.href = notification.data.url + "/input"; and closes the notification using notification.close(). The input page allows the user to input the activity they just are/were busy with when the timer went off.

This code creates a self-contained timer that uses the Notification API to display notifications and setTimeout() to set up the timer. It does not require any server-side interaction and can run entirely on the client-side.


The second part of the index page allows the user to display their activity history data in a table based on their selection of date. The table is filtered by rows in an HTML table based on the user's selection of year, month, and day using three drop-down menus.

First the values of the drop-down menu are stored in variables.

The `filterTableRows()` function is defined on lines 6-26. This function is called whenever the user selects a new option in any of the three drop-down menus. The function first gets the current selected values from each of the three drop-down menus using the `value` property.

The function then iterates through each row of the table using the `forEach()` method on the `tableRows` array. Within each iteration, the function checks the content of the relative rows in the table namely columns 4, 5, and 6 of the table. This checks if they match the user selected values. I tried to use the names of the columns here but that did not work I think due to differnces in the HTML names, I did not exactly figure out why I had to use child elements of the table to get the cell values.

So essentially the function displays the entire table by default and then hides and displays table rows based on the users selection. I did not want the table to be displayed initailly so event listeners were added to check if the default values were selected and hide the tables if all three values are the default. This was quite the dive into javascript for me and I strated to learn about the power of javascript(was not easy).

## Input

The input page is very simple. It displays inputs for the user to add thier recently completed/busy with activity to the databse. The relavent databse columns are iterated through using Jinja to display the options as well as to display previously enterd options as a faster way to add repeated options. I had to use a datalist tag here to display the previously entered options in a way that is more preferable.

Once the user inputs an activity, it is entered into their databasse and they are redirected to the index page where they can set a new timer as well as view thier history if they would like to.

## /History:

The hsitory page displays the full unedited database for the user. This page also allows the user to select a certian year, month, and day to view from the database. These selections are displayed with a scatter plot(I used Plotly CDN for this). The scatter plots are initailly hidden and displayed once the user selects a year to view. The scatter plots display data for the users overall productivity scale so they can see how thier percevied productivity varries from month to month, day to day, and hour to hour. This is meant to help the user better understand when they are most productive and hopefully utilize this information to make decisions surrounding when they should engage in priority activities. I can also expand this to include which activity elicits the most positive scores for productivity and when but I did not have time to add anymore to the app.

The code is implemented as such:

This is where I had to learn about AJAX calls and JSON(similar to a STRUCT in c I think) and how I can use data from the database as variables in javascript.


The interactive scatter plots are generated and updated based on the users input with regards to the year, month, and day options. The plots are initially set to be hidden so that the history table is visible as the users loads the page. There is a gap left between the table and the space where the plots would appear which I didnt want and I tried a few different ways of removing the gap but this was the easiest, I think I could have generated the plots individually for a better effect and maybe added some animations.

The AJAX calls are made to the /history route in order to get the data for the users selection and plug that data into the x and y axis of the scatter plots in javascript. IN hindsight maybe I could have done this process in python and removed the need for AJAX calls and overcomplicating it for myself but I didnt know until recently that Plotly has options for multiple languages(I didint look into it further so I am not sure how it works in python).

In summary, the code creates an interactive dashboard that allows the user to select a specific year, month, or day, and view the average productivity scale for that period in a scatter plot format. It uses AJAX calls to retrieve data from the server and Plotly library to generate the scatter plots.

Using the for loop inside the scatter plot was something very new and intresting for me. The JSON data from the AJAX call is extraced and added to the end of an array each iteration. These values are sued to plot the scatter plot.

## /Analytics:

This page is very similar to other parts of the app. Similar javascript, AJAX, JSON, is used to display pie charts based on the users input for date. These charts initially display a percentage breakdown of activity and duration for the entire database. When the user selects a specific date those initial charts are hidden and the dynamic charts are displayed based on the users viewing preference. The code used to display the charts is very similar to the scatter plots. These charts will hopefully be helpful to the user in that they can see how much time is they spend on certian activities and which activities they priotize.

The learning points here for me was using JSON and trying to understand that python objects need to be converted to JSON objects using jsonify before using the values in javascript with a AJAX call to the server. I think I have a rudementary understanding now but it took some trial and error to get everything working as it is now.


The rest of the functionality/structure for the app was taken from the structure of the the finance app that was provided by the cs50 staff.

I wrote some of the functionality in a seperate JS file but as I progressed it seemed easier to follow if I wrote the JS in the HTML with script tags for the different pages. I am not sure as to the best practice but I would assume that the seperate file is only neccessary if that JS applies to multiple pages.

## Possible future additions

* Adding intresting CSS
* Adding more ways to view the data
* Adding functionality that improves the user experience
* Adding networking/ online features such as connecting with friends/accountability partners etc


