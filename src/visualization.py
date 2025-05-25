import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ---- Visualization ----
def visualization(json_data):
    if "dishes" in json_data:
        df = pd.DataFrame(json_data["dishes"]).drop_duplicates()
        total = df[["Calories", "carbohydrate", "fat", "protein"]].sum().to_dict()

        st.subheader("🔍 Meal Summary")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Calories", f'{total["Calories"]} kcal')
        col2.metric("Carbs", f'{total["carbohydrate"]} g')
        col3.metric("Fat", f'{total["fat"]} g')
        col4.metric("Protein", f'{total["protein"]} g')

        st.subheader("📋 Dish Nutrition Table")
        st.dataframe(df.set_index("dish_name"), use_container_width=True)

        st.subheader("📊 Macronutrients per Dish")
        macros = df.melt(id_vars="dish_name", value_vars=["carbohydrate", "fat", "protein"],
                         var_name="Macronutrient", value_name="Amount (g)")
        st.bar_chart(macros.pivot(index="dish_name", columns="Macronutrient", values="Amount (g)"))

        st.subheader("🥧 Macronutrient Distribution")
        labels = ["Carbohydrates", "Fat", "Protein"]
        values = [total["carbohydrate"], total["fat"], total["protein"]]
        colors = ["#FFD54F", "#FF8A65", "#81C784"]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
        ax.axis('equal')
        st.pyplot(fig)
        st.subheader("Suggestions")
        st.write(json_data["suggestions"])

    elif 'error' in json_data:
        st.error(json_data['error'])
