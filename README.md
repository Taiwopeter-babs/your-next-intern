#   Your Next Intern (YNI) Project

## Content
- [Introduction](#introduction)
- [Overview of project architecture](#overview-of-project-architecture)
- [Technologies](#technology)
- [Routes and APIs](#routes-and-apis)
- [Screenshots](#application-screenshots)
- [Quick Links](#quick-links)
- [Authors](#authors)
- [Reach Out](#reach-out)


## Introduction

YNI is a web application built to ease the process of seeking for internship positions by undergraduates in Nigerian Universities. It aims to bridge the gap between prospective interns and organizations looking to train/equip the next generation of talents.

Users , interns and organizations, will find a welcome user experience. Organizations can activate and deactivate their application window, and they can also monitor the number of applicants on their profiles. Interns can apply to as many companies as possible, given that the application window of the company is open, and they can also apply to companies or cancel their application to companies, all with the click of a button. 

YNI was built with jQuery, a Javascript library and Flask, a Python framework.

- jQuery was used for the client-side functionality - dynamic rendering of HTML elements and AJAX (Asynchronous Javascript And XML) was used to query the API endpoints on the server.

- Flask, was used at the backend to create the routes and endpoints, while MySQL functions as the RDBMS.
[Back to content](#content)


## Overview of project architecture

The application design employs a Separation of Concern (SoC) method, where the APIs and the main application are run separately to increase the degree of freedom in maintainance and debugging. This helped in tracking causes of unintended results as each section of the application ran on different ports, 5000 and 5001 respectively, which would help in the long run in deployments and scaling.

SQLAlchemy, an ORM (Object Relational Mapper) was used to integrate MySQL into the application - tables in the database were mapped to different classes which represented the object-oriented form of the database tables. 

While many appreciate the abstraction of SQL statements that ORMs provide, I still found SQL queries useful during the development of the application. For instance, upon the realization that an intern profile needed an image section where avatars could be uploaded, I added a new column with ```ALTER TABLE interns ADD COLUMN `image_path` VARCHAR(512)``` query, though, adding the class attribute `image_path` would have still created the column.

The usage of jQuery as the Javascript library for the client-side, whose choice was influenced by the quick learning curve as opposed to other libraries.

The jinja templating engine enabled the rendering of the HTML templates(click [here](./web_app/templates/)).

Two bash scripts were used to start the servers for the API and the main application
- For the main app: [start_app](./start_app)

```
$ ./start_app web_app.main_app
* Serving Flask app 'main_app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.0.135:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ***-****-****
```

- For the API: [start_api](./start_api)
```
$ ./start_api api.v1.app
* Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://192.168.0.135:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ***-***-***
```
[Back to content](#content)

## Technology

This section lists the programming langauages, libraries, and frameworks used in the development of the application
- jQuery
- Flask
- Bootstrap
- HTML
- CSS3
[Back to content](#content)


## Routes and APIs

### Routes
- Authentication endpoints - [link here](./web_app/auth/auth_user.py)

GET /login - renders the login page
POST /login - authentication of registered users to login

GET /intern_signup - renders the intern registration page
POST /intern_signup - interns registration

GET /org_signup - renders the organization registration page
POST /org_signup - organizations registration

- Endpoints for views - profile, image upload [link here](./web_app/views/views.py)

GET /intern_profile/<intern_id> - renders an intern profile page
GET /org_profile/<org_id> - renders an organization profile page
GET /all_companies/open - renders a template for companies an intern can apply to
GET /all_interns - renders a template that lists all interns
POST /intern_profile/<intern_id> - provides a URL to render an uploaded image

### APIs

GET /interns - retrieves all interns
GET /interns/<intern_id> - retrieves an intern

GET /companies/<company_id> - retrieves a company
PUT /companies/<company_id> - updates a company's application window status (open or closed)

POST /companies/<company_id>/interns/<intern_id> - links a company and an intern, and updates their relationship in the storage

DELETE /companies/<company_id>/interns/<intern_id> - unlinks a company and an intern, and updates their relationship in the storage

GET /all_companies - retrieves all companies/organizations

[Back to content](#content)



## Application Screenshots

 - Home Page
 ![Your Next Intern Home page](./project_images/yni_home.PNG?raw=true "Home page")

 - Organization's profile page
 ![Profile page of an organization on YNI](./project_images/yni_com.PNG?raw=true "profile page")

 - Intern's profile page
 ![Profile page of an intern on YNI](./project_images/int_profile.jpeg?raw=true "Intern profile page")

 - Page listing companies on the platform
 ![All companies on YNI](./project_images/yni_coms.PNG?raw=true "All companies on YNI")

[Back to content](#content)



## Quick links

| Section | Link |
|-------- | -----|
| APIs    | [api dir](./api/v1) |
| HTML templates | [html templates](./web_app/templates/) |
| Main application | [Application](./web_app/) |
| Main application factory | [app factory](./web_app/main_app.py) |
| Main application configuration | [app config](./web_app/config.py) |

## Authors
- Taiwo Babalola [Linkedin](www.linkedin.com/in/taiwo-babalola) [Twitter](https://twitter.com/realtaiwo_peter)
- Henry Oworu [Linkedin] (www.linkedin.com/in/femi-oworu-6481801b) [Twitter] (twitter.com/phemsie)


## Reach Out
Please reach out to me if you'd like to contribute to this project.

[Back to content](#content)
