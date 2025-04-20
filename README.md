# 📝 Flask JWT Blog API

A secure and modular **Flask-based RESTful API** that handles user registration, login, and blog post CRUD using **JWT authentication**.

---

## 🚀 Features

- ✅ User Registration & Secure Login
- 🔐 JWT Authentication with Access & Refresh Tokens
- 📝 Create, Read, Update, Delete (CRUD) for Blog Posts
- 👤 Protected routes for user-specific content
- 🗂️ Modular code with Blueprints
- 🧠 SQLite (or PostgreSQL ready)
- ☁️ GitHub integrated & ready for deployment

---

## ⚙️ Tech Stack

- Python 3.10+
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- dotenv
- SQLite (default) / PostgreSQL ready
- Thunder Client or Postman (for API testing)

---

## 🧪 API Endpoints

### 🔐 Auth
| Method | Endpoint       | Description              |
|--------|----------------|--------------------------|
| POST   | `/register`    | Register a new user      |
| POST   | `/login`       | Login and get JWT token  |
| GET    | `/profile`     | Get logged-in user data  |

### 📝 Blog Posts
| Method | Endpoint            | Auth | Description                   |
|--------|---------------------|------|-------------------------------|
| POST   | `/posts`            | ✅   | Create a new post             |
| GET    | `/posts`            | ❌   | Get all posts (public)        |
| GET    | `/myposts`          | ✅   | Get posts created by user     |
| PUT    | `/posts/<id>`       | ✅   | Update a specific post        |
| DELETE | `/posts/<id>`       | ✅   | Delete a specific post        |

---

## 🛠️ How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/Manjunathrkrishna/flask-blog-api-jwt.git
cd flask-blog-api-jwt
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt  # optional if using requirements file
```

### 4. Setup Environment
Create a `.env` file in the root:

```
JWT_SECRET_KEY=supersecret
DATABASE_URL=sqlite:///blog.db
```

### 5. Run the App
```bash
python run.py
```

---

## 📦 Folder Structure

```
flask-blog-api-jwt/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── auth.py
│   └── blog.py
├── run.py
├── config.py
├── .env
├── .gitignore
```

---

## 🙌 Author

Built with ❤️ by **Manjunath R**  
📧 [mrkrishna6325@gmail.com](mailto:mrkrishna6325@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/manjunath-ramakrishna-14266915a)

---

## 💡 Want to Add Next?
- React frontend
- Unit tests with Pytest
- Deployment with Render or AWS

Let's gooo! 🚀
