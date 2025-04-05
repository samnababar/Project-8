import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in cm"""
    height_in_m = height / 100
    return weight / (height_in_m ** 2)

def get_bmi_category(bmi):
    """Return BMI category based on BMI value"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    st.set_page_config(
        page_title="BMI Calculator",
        page_icon="📊",
        layout="centered"
    )
    
    st.title("📊 BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI)")
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        height = st.number_input(
            "Height (cm)", 
            min_value=50, 
            max_value=250, 
            value=170,
            step=1
        )
    
    with col2:
        weight = st.number_input(
            "Weight (kg)", 
            min_value=30, 
            max_value=300, 
            value=70,
            step=1
        )
    
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        st.success(f"Your BMI is: **{bmi:.1f}**")
        st.write(f"Category: **{category}**")
        
        # Visual indicator
        if category == "Underweight":
            st.warning("Consider consulting a nutritionist")
        elif category == "Normal weight":
            st.success("Maintain your healthy lifestyle!")
        elif category == "Overweight":
            st.warning("Consider more physical activity")
        else:
            st.error("Please consult a healthcare professional")
    
    # Information section
    with st.expander("ℹ️ About BMI"):
        st.markdown("""
        **Body Mass Index (BMI)** is a measure of body fat based on height and weight.
        
        ### BMI Categories:
        - **Underweight**: BMI < 18.5
        - **Normal weight**: 18.5 ≤ BMI < 25
        - **Overweight**: 25 ≤ BMI < 30
        - **Obesity**: BMI ≥ 30
        
        *Note: BMI is a screening tool but not a diagnostic of body fatness or health.*
        """)

if __name__ == "__main__":
    main()