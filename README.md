
# **Hello Python App**

A simple Python Flask app that says **"Hello, World!"** on the homepage. This app is hosted on Render and can be deployed easily using Docker or directly with Python.

---

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)
- [License](#license)

---

## **Description**

This project is a basic **Python Flask** web application that listens on port `5000` (or Render-assigned port when deployed). It serves a simple homepage with the message **"Hello, World from Flask App!"**.

This app serves as a great starting point for learning about Flask, continuous integration with GitHub Actions, and deployment on platforms like **Render**.

---

## **Features**

- **Python Flask Web App**: Lightweight and fast web framework.
- **CI/CD with GitHub Actions**: Automatically runs tests and deploys changes.
- **Docker Support**: Easily containerize and run your app with Docker.
- **Easy Deployment to Render**: Push and deploy your app with minimal effort.
- **Testing with Pytest**: Ensure app reliability with simple unit tests.

---

## **Getting Started**

### **Prerequisites**

Before you begin, make sure you have these installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python's package installer (should be installed with Python).
- **Git**: [Download Git](https://git-scm.com/downloads).
- **Docker** (optional, if you're using Docker for containerization): [Download Docker](https://www.docker.com/get-started).

### **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/hello-python-app.git
   cd hello-python-app
   ```

2. **Create a virtual environment (optional, but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app locally:**

   ```bash
   python app.py
   ```

   Your app will now be accessible at `http://127.0.0.1:5000`.

---

## **Usage**

Once the app is running, navigate to `http://127.0.0.1:5000` in your browser, and you will see:

```
Hello, World from Flask App!
```

This is a basic starting point. You can expand the app by adding new routes, features, or connecting it to a database.

---

## **Testing**

This app uses **Pytest** for automated testing. To run the tests:

1. **Install pytest (if not installed):**

   ```bash
   pip install pytest
   ```

2. **Run the tests:**

   ```bash
   pytest
   ```

3. **You should see something like this:**

   ```
   ========================= test session starts =========================
   ...
   1 passed in 0.03 seconds
   ```

---

## **Deployment**

You can deploy this app easily on platforms like **Render** or **Docker**. Here are the instructions for each.

### **Render**

1. **Go to Render** and sign up: [Render](https://render.com).
2. **Create a new web service** and connect it to your GitHub repo.
3. Select the **Python** environment.
4. Render will automatically detect and deploy your app.

### **Docker (Optional)**

1. **Build the Docker image:**

   ```bash
   docker build -t hello-python-app .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 5000:5000 hello-python-app
   ```

   Your app will be available at `http://localhost:5000`.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contributing**

Feel free to submit pull requests, report issues, or suggest features! Here's how you can help:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Create a new Pull Request.

---

## **Additional Resources**

- [Flask Documentation](https://flask.palletsprojects.com/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Docker Documentation](https://docs.docker.com/)
- [Render Docs](https://render.com/docs)
