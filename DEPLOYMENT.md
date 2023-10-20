# Deployment

- The app was deployed to [Render](https://render.com/).
- The database was deployed to [ElephantSQL](https://www.elephantsql.com/).

- The app can be reached by the [link](https://restaurant-booking-system-4pt5.onrender.com/).

## Local deployment

*Note:*
  - This project requires to install all the requirements:
  - Open the terminal window and type:
  - `pip3 install -r requirements.txt`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/NikolettaGr/Restaurant-Booking-App).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/NikolettaGr/Restaurant-Booking-App.git`


---

1. Install the dependencies:

    - Open the terminal window and type:
    - `pip3 install -r requirements.txt`


1. Create a `.gitignore` file in the root directory of the project where you should add env.py and __pycache__ files to prevent the privacy of your secret data.

1. Create a `.env` file. This will contain the following environment variables:

    ```python
    import os

      os.environ['SECRET_KEY'] = 'Add a secret key'
      os.environ['DATABASE_URL'] = 'will be used to connect to the database'
      os.environ['DEBUG'] = 'True'
    ```

    *During the development stage DEBUG is set to True, but it is vital to change it to False.*

1. Run the following commands in a terminal to make migrations: 
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
1. Create a superuser to get access to the admin environment.
    - `python3 manage.py createsuperuser`
    - Enter the required information (your username, email and password).
1. Run the app with the following command in the terminal:
    - `python3 manage.py runserver`
1. Open the link provided in a browser to see the app.

1. If you need to access the admin page:
    - Add /admin/ to the link provided.
    - Enter your username and password (for the superuser that you have created before).
    - You will be redirected to the admin page.


## Render Deployment

### Create Database on ElephantSQL

1. Go to [ElephantSQL](https://www.elephantsql.com/) and create a new account.

2. Create a new instance of the database.

    - ![ElephantSQL. Create a new instance](documentation/screenshot_images/create_new_instance.png)

3. Select a name for your database and select the free plan.

    - ![ElephantSQL. Select a name for your database](documentation/screenshot_images/render-plan.png)

4. Click "Select Region"

    - ![ElephantSQL. Select a region](documentation/screenshot_images/select_region.png)

5. Select a region close to you.

    - ![ElephantSQL. Select a region](documentation/screenshot_images/select_region1.png)

6. Click "Review"

    - ![ElephantSQL. Review](documentation/screenshot_images/click_review.png)

7. Click "Create Instance"

    - ![ElephantSQL. Create Instance](documentation/screenshot_images/render-instances.png)

8. Click on the name of your database to open the dashboard.

    - ![ElephantSQL. Open dashboard](documentation/screenshot_images/render-namee.png)

9. You will see the dashboard of your database. You will need the URL of your database to connect it to your Django project.

    - ![ElephantSQL. DB](documentation/screenshot_images/render-bulidhish.png)

### Create a new app on Render

1. Create a new Render account if you don't already have one here [Render](https://render.com/).

2. Create a new application on the following page here [New Render App](https://dashboard.render.com/), choose **Webserver**:

    - ![New Render App](documentation/screenshot_images/1.render.png)

3. Select the GitHub option and connect the application to the repository you created.

    - ![GitHub Option](documentation/screenshot_images/2.render.png)

4. Search for the repository you created and click "Connect."

    - ![Connect to GitHub](documentation/screenshot_images/3.render.png)

    - ![Connect to GitHub](documentation/screenshot_images/3.1.render.png)

5. Create name for the application

    - ![Create Application Name](documentation/screenshot_images/4.render.png)

6. Select the region where you want to deploy the application.

    - ![Select Region](documentation/screenshot_images/5.render.png)

7. Select branch to deploy.

    - ![Select Branch](documentation/screenshot_images/6.render.png)

8. Select environment.

    - ![Select Environment Variables](documentation/screenshot_images/7.render.png)

9. Render build command: `./build.sh`

    - ![Render Build Command](documentation/screenshot_images/8.click_name.png)

10. Render start command: `gunicorn <NAME OF YOUR APP>.wsgi:application` + You can delete `Procfile` from your repository.

    - ![Render Start Command](documentation/screenshot_images/9.render.png)

11. Select Free plan.

    - ![Select Free Plan](documentation/screenshot_images/10.render.png)

12. Click on "Advanced" settings.

    - ![Advanced Settings](documentation/screenshot_images/11.render.png)

13. Add the following environment variables:

    - Key: WEB_CONCURRENCY Value: 4
    - Key: DATABASE_URL Value: *************
    - Key: SECRET_KEY Value: *************
    - Key: DEBUG Value: False
    - Key: EMAIL_HOST_USER Value: *************
    - Key: EMAIL_HOST_PASSWORD Value: *************

    *DATABASE_URL value is takes from ElephantSQL dashboard, SECRET_KEY value is takes from your local env.py file, DEBUG value is set to False, EMAIL_HOST_USER and EMAIL_HOST_PASSWORD values are takes from your Gmail account.*


14. Open VS Code and create a new file called `build.sh` in the root directory of your project.


15. Copy the following code into the `build.sh` file:

    ```bash
      set -o errexit
      pip install -r requirements.txt
      python manage.py collectstatic --noinput
      python manage.py makemigrations && python manage.py migrate
    ```

    -*pip install -r requirements.txt installs the packages detailed in your requirements.txt file.*
    - *python manage.py collectstatic collects all static files to allow them to be served in the production environment.*
    - *The –noinput flag allows the command to run with no additional input from the deploying developer.*
    - *python manage.py makemigrations && python manage.py migrate are run to ensure all migrations are made to your production database.*

16. Save the file `build.sh`.

17. Go to `settings.py` file and add the following code to add Render.com to allowed hosts:

    ```python
        RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
        if RENDER_EXTERNAL_HOSTNAME:
          ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    ```

   *If you have heroku in your allowed hosts, delete it*

18. Save the file `settings.py`.

19. Go to `env.py` and change to DATEBASE_URL value to the one you got from ElephantSQL.

    ```python
        os.environ["DATABASE_URL"] = '*************'
    ```

20. Create a superuser for your database.

    ```bash
        python manage.py createsuperuser
    ```

21. Commit and push the changes to GitHub.

22. Go back to Render and click "Create Web Service."

    - ![Save Web Service](documentation/screenshot_images/12.render.png)

23. Wait for the completion of the deployment.

24. Go to admin panel and change the settings for the admin by assigning a role of `Boss` to allow the full control of the website including role assignment.

---
