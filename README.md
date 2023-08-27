# Assignment Submission Portal
This is an assignment submission portal made using the Django framework. The portal allows students to submit their assignments to their respective instructors. This README file provides instructions on how to use the portal and a list of its features.

# Getting Started
To use the assignment submission portal, you must have Python and Django installed on your machine.

* Clone the repository: git clone https://github.com/arpan-khanna/Submission
* Install the dependencies: pip install -r requirement.txt

To use the sql database, run the following commands:
* python manage.py makemigrations
* python manage.py migrate

To use the portal, follow these steps:
* Run the server: python manage.py runserver
* Access the portal in your web browser at http://localhost:8000/

Alternatively if you want to access the portal over the intranet then run the server as follows:
* python manage.py runsslserver 0.0.0.0:8000
* Access the portal in your web browser at https://your-ip-address:8000/
* Mske sure to change the callback url in Azure according to your ip address.

Also it is safe to install a virtual environment and then install the dependencies in it.
To use the virtual environment and install the dependencies run the following command:
* pip install virtualenv
* virtualenv venv
* venv\Scripts\activate
* pip install -r requirement.txt

Note: The above commands are for Windows. For Linux and Mac OS, please refer to the official documentation.


# Features
The assignment submission portal has the following features:

1. User Authentication: The portal requires students to log in using their university or college credentials to access the portal. This ensures that only registered students can submit assignments.
2. Assignment Creation: Faculty members can create assignments and upload relevant documents or files, including assignment instructions, rubrics, and examples.
3. Submission Form: Students can submit their assignments through a submission form provided on the portal. This form has fields for students to enter their name, student ID, course name, assignment title, and the file they want to submit.
4. Submission Deadline: The portal has a feature for setting a submission deadline for each assignment. This allows students to submit their assignments before the deadline and prevents them from submitting assignments after the deadline.
5. Grading and Feedback: After the submission deadline has passed, faculty members can access submitted assignments, grade them, and provide feedback to students. Students can also view their grades and feedback on the portal.
6. Notifications: The portal has a notification feature that alerts students and faculty members of upcoming assignment deadlines, grades, and feedback.

# Contributing

To contribute to the assignment submission portal, follow these steps:

* Fork the repository.
* Create a new branch for your feature: git checkout -b feature-name
* Make your changes and commit them: git commit -m "Add feature"
* Push your changes to your fork: git push origin feature-name
* Submit a pull request.
