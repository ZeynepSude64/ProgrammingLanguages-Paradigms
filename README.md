# 🎬 Movie Recommendation System

This project is a simple movie recommendation system built with Python. It simulates the basic logic behind recommendation systems used in platforms like Netflix in a simplified way.

The main goal of the project is to suggest movies to users based on their watch history and the ratings they give. The system analyzes user preferences and recommends movies that match their interests.

---

## 🚀 Features

- Add watched movies with rating
- Get personalized movie recommendations
- Random movie suggestion
- Search movies by title
- User statistics (average rating, most watched genres)
- Prevents recommending already watched movies

---

## 🧠 Project Structure

The project is built using Object Oriented Programming (OOP) and contains three main classes:

### 🎥 Movie
Stores basic movie information:
- Title
- Genre
- Rating

### 👤 User
Handles user data:
- Watched movies list
- Statistics calculation (average rating, genre distribution)

### 🎯 RecommendationEngine
Handles all recommendation logic:
- Personalized recommendations
- Random movie selection
- Movie search functionality

---

## 🎯 Recommendation Logic

The system works as follows:

1. Finds the user’s favorite genre based on weighted ratings  
2. Filters movies that match this genre  
3. Removes already watched movies  
4. Sorts remaining movies by rating  
5. Returns top 3 recommendations  

---

## 🔍 Additional Features

- Random movie recommendation for discovery
- Keyword-based movie search
- User statistics overview
- Duplicate watch prevention

---

## 🛠️ Technologies Used

- Python
- Object Oriented Programming (OOP)
- Functional Programming (map, filter, lambda)

---

## 📌 Purpose of the Project

This project was created for learning purposes to:
- Practice OOP concepts
- Understand basic recommendation system logic
- Use functional programming in real examples
- Improve Python coding skills

---

## ▶️ How to Run

```bash
python main.py
