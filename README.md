Here’s a clean, professional, and **beautiful README** for your **Meal Nutrition Analyzer** Streamlit app:

---

# 🥗 Meal Nutrition Analyzer

**AI-powered tool to estimate calories, macronutrients, and provide health suggestions from meal images or text.**

![banner](https://img.shields.io/badge/Powered%20by-Gemini%202.0-blueviolet?style=flat-square) ![Python](https://img.shields.io/badge/Made%20with-Python%203.10-yellow?style=flat-square) ![Streamlit](https://img.shields.io/badge/UI-Streamlit-fd4f00?style=flat-square)

---

## 🔍 Overview

**Meal Nutrition Analyzer** is a Streamlit-based application that leverages Google Gemini API to:

* Analyze meal images and/or text descriptions
* Estimate **calories**, **carbohydrates**, **fat**, and **protein** per dish
* Provide **visual insights** and **health suggestions**

---

## 📸 Features

✅ Upload a meal image
✅ Describe your meal in text
✅ Get per-dish nutritional breakdown
✅ Beautiful bar and pie charts
✅ Smart health suggestions powered by AI

---

## 🖼️ video Demo
![Demo](demo.gif)
---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/meal-nutrition-analyzer.git
cd meal-nutrition-analyzer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 🧠 Powered By

* [Google Gemini 2.0](https://ai.google.dev/)
* [Streamlit](https://streamlit.io/)
* [Pydantic](https://docs.pydantic.dev/)
* [Matplotlib](https://matplotlib.org/)
* [Pillow](https://python-pillow.org/)

---

## 📁 Project Structure

```
📦meal-nutrition-analyzer
├── research                 # jupyter notebooks
├── app.py                   # Streamlit frontend
├── src
│   ├── chatbot.py           # AI agent logic using Gemini
│   └── visualization.py     # Visualization & summaries
├── saved_meal_images/       # Stores uploaded images
├── .env                     # Your Gemini API Key
├── requirements.txt
└── README.md
```

---

## ✅ Example Use Cases

* Nutrition tracking for fitness goals
* Diet logging for healthcare professionals
* Wellness apps looking for AI integrations

---

## 🙌 Contribution

Pull requests are welcome! Feel free to improve functionality, add models, or enhance visuals.

---

## 🛡️ License

This project is open-source under the [MIT License](LICENSE).

---

## 📬 Contact

Made with ❤️ by saurav kumar
📧 [spynom01@gmail.com](mailto:spynom01@gmail.com)
---
