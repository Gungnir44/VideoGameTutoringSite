# 🎮 Video Game Tutoring Platform

Welcome to the **Video Game Tutoring Platform** — a full-stack Django web application where players can find and hire experienced coaches for various popular games like League of Legends, Marvel Rivals, Overwatch, Fortnite, Rocket League, Smash Bros, Pokémon, and more.

This website allows users to:
- Sign up as Players or Coaches
- Create and manage profiles
- Browse available Coaches by Game
- Book coaching sessions
- Pay for sessions securely via PayPal
- Leave Reviews for Coaches
- Manage bookings through personalized Dashboards
- (Optional) Donate to support the platform

Built with ❤️ using Django, TailwindCSS (for modern dark UI), and PayPal Integration.

---

## 🚀 Project Features

| Feature | Description |
|:---|:---|
| **User Registration** | Players and Coaches can create separate accounts |
| **Coach Profile Creation** | Coaches upload profile pictures, choose their specialty game, and set hourly rates |
| **Browse Coaches by Game** | Players filter available coaches by game with button-based navigation |
| **Booking System** | Players can book coaching sessions and chat with coaches |
| **Payment Integration** | Players can securely pay via PayPal after booking |
| **Reviews** | Players can leave reviews for Coaches after a session |
| **Dark Mode UI** | Fully mobile-responsive dark gamer-style user interface |
| **Admin Panel** | Site administrator can manage users, bookings, and reviews through Django Admin |
| **Security** | Passwords are hashed, CSRF protection enabled, login/logout properly implemented |
| **Favicon** | Custom GameCube favicon to match gaming theme |

---

## 🛠 Technologies Used

- **Backend**: Django 5.2
- **Frontend**: TailwindCSS v4.1 (custom dark theme)
- **Database**: SQLite3 (default Django db)
- **Authentication**: Django Built-in Auth
- **Payments**: PayPal Checkout Integration
- **Hosting**: Local Development Server (`127.0.0.1:8000`)

---

## 📋 How to Install and Run Locally

**1. Clone the repository:**
```bash
git clone <your-repo-url>
```

**2. Set up Python Virtual Environment:**
```bash
cd VideoGameTutoringSite
python -m venv .venv
.\.venv\Scripts\activate  # Windows
```

**3. Install project dependencies:**
```bash
pip install -r requirements.txt
```
(If requirements.txt not available, install manually: Django, django-tailwind if needed.)

**4. Install Node.js dependencies (for TailwindCSS, if modifying styles):**
```bash
cd theme
npm install
```

**5. Compile TailwindCSS (ONLY if you change styles manually):**
```bash
.\tailwindcss.exe -i .\static_src\input.css -o .\static\css\styles.css --watch
```

**6. Apply Database Migrations:**
```bash
cd ..
python manage.py makemigrations
python manage.py migrate
```

**7. Create Superuser for Admin Access:**
```bash
python manage.py createsuperuser
```

**8. Run the Development Server:**
```bash
python manage.py runserver
```

**9. Open your browser and navigate to:**
```
http://127.0.0.1:8000/
```

---

## 🧭 Walkthrough of Website Functionality

| Page | URL | What It Does |
|:---|:---|:---|
| **Home Page** | `/` | Landing page with "Become a Coach" or "Find a Coach" |
| **Player Signup** | `/signup/player/` | Create an account as a player |
| **Coach Signup** | `/signup/coach/` | Create a coach profile (choose game + rate + upload pic) |
| **Login** | `/accounts/login/` | Standard login page |
| **Browse Coaches** | `/browse/` | View game buttons and select a game |
| **Browse Specific Game** | `/browse/<game>/` | See coaches filtered by specific game |
| **Coach Profile Detail** | `/coach/<id>/` | See detailed info and book a session |
| **Booking System** | `/booking/<booking_id>/` | Message/chat with coach about session |
| **Player Dashboard** | `/player-dashboard/` | Manage your bookings |
| **Coach Dashboard** | `/coach-dashboard/` | Manage your sessions (if you're a coach) |
| **Payment** | Inside Coach Profile | PayPal integration to pay for coaching sessions |
| **Admin Panel** | `/admin/` | Full control over Users, Bookings, and Reviews |

---

## 💵 How Payment Works

- When a Player wants to finalize a coaching session, they click "Pay Now" (PayPal button).
- PayPal securely processes the transaction.
- After successful payment, booking is automatically marked as **Paid**.
- A success message appears to confirm ("Booking Paid Successfully! 🎉").

---

## 🎨 Design Choices

- **Dark theme** for gamers (gray-900 background, indigo/green action colors)
- **Responsive layout** for mobile and desktop
- **Minimalistic buttons** to reduce cognitive overload
- **Flash success messages** after booking and payment
- **Clear separation** between Player experience and Coach experience

---

## 🛡️ Security Highlights

- Password hashing via Django's built-in auth system
- CSRF protection on all forms
- Admin panel locked behind superuser login
- Proper error handling (404 pages optional)

---

## 🐛 Known Issues (Minor)

- No Stripe support (only PayPal)
- No direct video calling integration (Discord recommended after booking)
- No password reset functionality (out of scope for this project)

---

## 🙏 Acknowledgments

- Django Documentation
- TailwindCSS Framework
- PayPal Developer API Docs
- Inspiration from gaming communities

---

## 📬 Future Improvements (if time allows)

- Add real-time chat (WebSockets)
- Add rating/star system for coaches
- Add password reset email
- Add Discord OAuth for login

---

# 🏁 Final Note

This project was developed as part of a Web Development course assignment. It is **fully functional**, **tested**, and **ready to submit**.
Thank you for reviewing this project!

---

# 📂 Folder Structure Overview

```
VideoGameTutoringSite/
├── VideoGameTutoringSite/  # Project settings
├── Tutoring_Website/       # Main app (views, models, urls)
├── theme/                  # TailwindCSS static files
├── static/                 # Static assets (favicon, images)
├── templates/              # HTML templates
├── db.sqlite3              # Database
├── manage.py               # Django management
├── README.md               # (This file!)
```
