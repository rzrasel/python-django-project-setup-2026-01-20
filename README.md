# 🚀 Django REST API Project Setup Guide

Welcome! 👋  
This guide walks you through setting up a **Django project with Virtual Environment and Django REST Framework** step by step.

---

## 🧰 1. Git Commands

```bash
git init
git remote add origin https://github.com/rzrasel/python-django-project-setup-2026-01-20.git
git remote -v
git fetch && git checkout master
git add .
git commit -m "Add Readme & Git Commit File"
git pull
git push --all
git status
```
---

## 📁 Go to Project Directory

```bash
cd your-project-folder
```
---

## 🧪 Create Virtual Environment

```bash
python -m venv env
```

✨ Or (Alternative)

```bash
python -m venv venv
```
📌 Run this inside your Django project directory

---

## ▶️ Activate Virtual Environment (Windows)

```bash
cd env/Scripts
activate
```

Go back to project root:
```bash
cd ..
cd ..
```

---

## 📦 Install Django

```bash
pip install django
django-admin --version
```

---

## 🏗️ Create Django Project

```bash
django-admin startproject pythondjangoproject1
cd pythondjangoproject1
```

✨ Or (Alternative)

```bash
django-admin startproject python_django_project_1
cd python_django_project_1
```

---

## ▶️ Run Development Server

```bash
python manage.py runserver
```
🛑 Stop server: `Ctrl + C`

---

## 👑 Create Django Admin (Superuser)

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Login URL:
```
http://127.0.0.1:8000/admin/
```

Reset password:
```bash
python manage.py changepassword admin
```

---

## 🔌 Install Django REST Framework

```bash
pip install djangorestframework
pip list

or

python -m pip install djangorestframework
pip list
```

---

## ⚙️ Configure Django REST Framework

### settings.py
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### urls.py
```python
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
]
```

---

## 📱 Create Django App

```bash
python manage.py startapp useraccount
```

✨ Or (Alternative)

```bash
python manage.py startapp user_account
```

### 📄 settings.py
Add REST Framework to INSTALLED_APPS:

```python
INSTALLED_APPS = [
    ...
    'user_account',
]
```

---

## 🗄️ Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🧯 Common venv Fix (Guaranteed)

```bash
where python
env\Scripts\activate
python -m pip install django djangorestframework
python manage.py runserver
```

---

## 🧩 Git Rebase Squash (Interactive)

```bash
git rebase -i HEAD~2
i
[delete word: pick [make it] squash/s]
esc:wq↵

i
[change commit comment by #]
esc:wq↵

------------------------------------

git rebase -i 4daac6b7
i
esc:wq↵

i
[change commit comment by #]
esc:wq↵

git push --force
//git push -f --set-upstream origin master

------------------------------------

git rebase -i --root
i
esc:wq↵

i
[change commit comment by #]
esc:wq↵

git push --force

//git push -f --set-upstream origin master
```

---

## ⏰ PHP Date Example

```php
echo date("D", (time() + 6 * 60 * 60)) . "day " . date("F j, Y, G:i:s", (time() + 6 * 60 * 60));
```

---

## 📚 Learn More

👉 https://youtu.be/V5KrD7CmO4o

---

## ✅ Done!

🎉 Your Django REST API project is ready!
