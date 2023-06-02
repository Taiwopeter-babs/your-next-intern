#   Your Next Intern (YNI) Project

## Content
- [Introduction](#introduction)
- [Overview of project architecture](#overview-of-project-architecture)

## Introduction

YNI is a web application built to ease the process of seeking for internship positions by undergraduates in Nigerian Universities. It aims to bridge the gap between prospective interns and organizations looking to train/equip the next generation of talents.

Users , interns and organizations, will find a welcome user experience. Organizations can activate and deactivate their application window, and they can also monitor the number of applicants on their profiles. Interns can apply to as many companies as possible, given that the application window of the company is open, and they can also apply to companies or cancel their application to companies, all with the click of a button. 

YNI was built with jQuery, a Javascript library and Flask, a Python framework.

- jQuery was used for the client-side functionality - dynamic rendering of HTML elements and AJAX (Asynchronous Javascript And XML) was used to query the API endpoints on the server.

- Flask, was used at the backend to create the routes and endpoints, while MySQL functions as the RDBMS.


## Overview of project architecture

The application design employs a Separation of Concern (SoC) method, where the APIs and the main application are run separately to increase the degree of freedom in maintainance and debugging. This helped in tracking causes of unintended results as each section of the application ran on different ports, 5000 and 5001 respectively, which would help in the long run in deployments and scaling.

SQLAlchemy, an ORM (Object Relational Mapper) was used to integrate MySQL into the application - tables in the database were mapped to different classes which represented the object-oriented form of the database tables. 

While many appreciate the abstraction of SQL statements that ORMs provide, I still found SQL queries useful during the development of the application. For instance, upon the realization that an intern profile needed an image section where avatars could be uploaded, I added a new column with ```ALTER TABLE interns ADD COLUMN `image_path` VARCHAR(512)``` query, though, adding the class attribute `image_path` would have still created the column.

The usage of jQuery as the Javascript library for the client-side, whose choice was influenced by the quick learning curve as opposed to other libraries.

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