# Django E-Commerce Backend

A backend-focused e-commerce application built with pure Django, designed to practice and demonstrate core backend concepts such as authentication, relational data modeling, business logic for cart and orders, and admin-side management.

## 🚀 Features

### 👤 User Features
User authentication using Django’s built-in AbstractUser
Browse products
Add products to cart
Update and remove cart items
Place orders from cart
View order details (order amount calculated)

### 🛠 Admin Features
Full product management via Django Admin
Order management
User management
Enhanced admin experience using:
list_display
search_fields
filters across all apps

### 📦 Business Logic
Cart → Order flow implemented
Order amount calculation
Stock quantity reduced after order placement
Proper relational modeling between users, products, cart, and orders

## 🧱 Project Structure
The project is organized into multiple Django apps for separation of concerns:

**products** – product catalog and stock
**cart** – cart and cart item logic
**orders** – order creation and management
**users** – custom user model and authentication

##**🛠 Tech Stack**
**Backend**: Django (MVT)
**Authentication**: Django AbstractUser
**Database**: PostgreSQL
**Admin Panel**: Django Admin (customized)
**Language**: Python
