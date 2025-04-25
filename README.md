# 🛡️ Flask Blog API with JWT Authentication

This is the backend API for a Full Stack Blog Application built using **Flask**, secured with **JWT Authentication**. It provides RESTful endpoints for user registration, login, and blog post management (CRUD).

### 🌐 Live API: [Render Deployment](https://flask-blog-api-jmhz.onrender.com)

---

## 🚀 Features
- User Registration & Login with JWT
- Protected Routes using Bearer Token
- CRUD Operations on Blog Posts
- SQLAlchemy ORM with SQLite
- CORS Enabled for Frontend Integration
- Deployed on Render (Free Tier)

---

## ⚙️ Tech Stack
- **Backend**: Python, Flask, Flask-JWT-Extended, SQLAlchemy
- **Database**: SQLite
- **Deployment**: Render
- **Others**: CORS, REST API, GitHub

---

## 🛠️ Running Locally
```bash
git clone https://github.com/Manjunathrkrishna/flask-blog-api-jwt.git
cd flask-blog-api-jwt
pip install -r requirements.txt
python run.py
```

---

## 📄 API Endpoints
- `POST /register` - Register User
- `POST /login` - Login & Receive JWT Token
- `GET /myposts` - Get User's Posts (Requires Token)
- `POST /posts` - Create New Post (Requires Token)
