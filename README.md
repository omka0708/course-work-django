# course-work-django
The project completed for the course work on the subject "Development of server parts of Internet resources".
The course project is made using the Django 4.0 framework in Python.

# The project consists of:

- Virtual environment
- Customized files that Django creates by default
- The only application "tickets" that stores customized .puy files with models, views, etc.
- A series of templates, broken into separate parts using the technology of the Django template language
- Customized Django admin panel
- Database working by Open Server Panel
- Ability to send letters using the SMTP protocol

The idea of the project is a web service for booking tickets. The user selects an event from the list on the main page, and then fills out a ticket reservation form, where he indicates his mail. A letter is sent to the user's mail using the SMTP protocol, notifying that the user has revoked the ticket for the event.