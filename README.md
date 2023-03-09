# Vikings View Website

## Technology Stack
* Django
* CKEditor (Rich Text Editor)

## Installation for Beginners
1. Download Python >= 3.9
2. Clone the Repository. Depending on your level of access, this may mean:
    * Fork the repository and clone it.
    * Clone from this repository and submit changes by pushing
3. Set up a virtual environment in the cloned repo
4. Install necessary packages: ```pip3 install -r requirements.txt```
5. Set up a file for environment variables.
    * The file should **NOT** be uploaded to github and should be kept confidential
    * The file should contain: ```SECRET_KEY=YOUR_SECRET_KEY```
6. Run the project via: ```python3 manage.py runserver```

## Project Structure
Here I am going to list out the most important files in the project. <br>
***NOTE***: I am fully aware that the correct practice in Django is to put your views into each individual app and then including them in the urls.py of the main app using ```include()```; however, I decided against that because I believe this file structure is a lot easier to understand for beginners, and the project is so simple there is no point in dividing responsibilities.
```
VikingsView
│   README.md
│   db.sqlite3          // Database
│   requirements.txt    // Python
|   .env                // Environment Variables
│   ...
│
└─── articles
│       admin.py        // Register models to use in the admin panel.
│       models.py       // Contains model for Article and Author table
│       ...
│
└─── team
│       admin.py        // Register models to use in the admin panel.
│       models.py       // Contains model for Member table in the DB
│       ...
│
└─── vikingsview
│       settings.py     // All the settings for the application
│       urls.py         // All the urls in the application
│       views.py        // All the views in the application
│       wsgi.py         // An essential part of deploying the application
│       ...
│
└─── static             // Self Explanatory
│     └───  css
│     └───  images
│     └───  js
│
└─── templates
        shell.html      // All the templates extend off of this one.
        ...

```

## Deployment Pipeline
Here is where I am going to have to apologize. I am not good with DevOps, and to get a Heroku Server running is too expensive (No point using GCP or AWS). Unfortuneately, the deployment pipeline is going to be 'a$$' to put it lightly. Regardless,

* Application is deployed on Apache2 via a Linode Server
* Please Request SSH Key from the club sposnor teacher
* Here is a [video tutorial](https://www.youtube.com/watch?v=Sa_kQheCnds) on deploying Django Applications