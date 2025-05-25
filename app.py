import streamlit as st
from PIL import Image
import os
from src.chatbot import ai_agent
from src.visualization import visualization



# ---- Configuration ----
st.set_page_config(page_title="🍽️ Meal Nutrition Analyzer", layout="wide")
st.title("🥗 Meal Nutrition Analyzer")

# ---- Directories ----
SAVE_DIR = "saved_meal_images"
os.makedirs(SAVE_DIR, exist_ok=True)

# ---- Mode Selection ----
mode = st.radio("Choose input method:", ["📷 Upload Meal Image", "✍️ Text Description"])

user_input = ""
image_path = None
json_data = {}

# ---- Mode: Image Upload ----
if mode == "📷 Upload Meal Image":
    uploaded_file = st.file_uploader("Upload a meal image", type=["jpg", "jpeg", "png","webp"])
    user_input = st.text_area("Optional description of the meal")

    if uploaded_file:
        # Save image
        image_filename = f"meal.jpg"
        image_path = os.path.join(SAVE_DIR, image_filename)
        image = Image.open(uploaded_file)
        image.save(image_path)

        st.image(image_path, caption="Saved Meal Image", width=300)

        if st.button("Analyze Image"):
            with st.spinner("Analyzing image and description..."):
                # You pass user_input and indicate image exists
                json_data = ai_agent(user_input, is_image_exist=True)
                visualization(json_data)

# ---- Mode: Text Description Only ----
elif mode == "✍️ Text Description":
    user_input = st.text_area("Describe your meal (e.g., Garlic Naan, Butter Chicken, Rice)")

    if st.button("Analyze Text"):
        if user_input.strip():
            with st.spinner("Analyzing text..."):
                json_data = ai_agent(user_input, is_image_exist=False)
                visualization(json_data)
        else:
            st.warning("Please enter a meal description.")

