### Interactive Multipage Dashboard Using Dash <br>

Dash is a python framework created by plotly for creating interactive web applications. It is written on top of Flask, Plotly.js and React.js. 
With dash apps it becomes easier for data scientists and engineers to put complex Python analytics in the hands of business decision makers and operators. <br>

This dashboard keeps track of the crime statistics from 2012-19 across the various districts of Berlin, Germany. The dashboard has been hosted using Heroku, and you
can access it <a href="https://python-dashboard-dash.herokuapp.com/">here</a> <br>

GIF for a quick demo: <br>

![demo](assets/Dashboard.gif)

<b>Update:</b> Added the email functionality using Gmail's SMTP. However, Google recently disabled the "receive emails from less secure apps" functionality, meaning
I could no longer directly use my email id and password to login via heroku. The easy workaround is to setup an app password for the dashboard, the slightly complex 
workaround would be to add a gmail login functionality to the dashboard. Also, I finally added a quick and dirty about page..woohoo!!
