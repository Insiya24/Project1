import streamlit as st
import openai
# from fpdf import FPDF

# Set your OpenAI API key here
openai.api_key = st.secrets["INSANIYA"]

def generate_prescription(name, diagnosis, age, sex, weight, current_medications, allergies, coexisting_conditions):
    prompt = f"""Act as a Medical profession. Use Name: {name}\nDiagnosis: {diagnosis}\nAge: {age} years\nSex: {sex}\nWeight: {weight} 
            kg\nCurrent Medications: {current_medications}\nAllergies: {allergies}\nCoexisting Conditions: {', '.join(coexisting_conditions)}
            \n\nUse it and Prescribe medications in the following format\n\n\n Output Format:\nName\n\nAge\n\nWeight\n\Medicine name\n DosageFrequency
            \nInstructions \nPrecautions(if any).Make it in 400 words in proper output format with proper name of medicine"""

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=600
    )

    prescription = response['choices'][0]['text']
    return prescription

# def save_pdf(prescription):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt="Prescription:", ln=True, align="C")
#     pdf.multi_cell(0, 10, prescription)
#     pdf_file_path = "prescription.pdf"
#     pdf.output(pdf_file_path)
#     return pdf_file_path

# Streamlit UI
st.title("Medical Prescription Generator")

name = st.text_input("Name:")
diagnosis = st.text_area("Describe your condition here in detail. Also mention the severity of your condition:")
age = st.number_input("Age:")
sex = st.radio("Sex:", ["Male", "Female"])
weight = st.number_input("Weight (kg):")
current_medications = st.text_area("Current Medications (if any):")
allergies = st.text_area("Any Allergies? Please mention here:")
coexisting_conditions = st.multiselect("Coexisting Conditions:", 
                                      ["Pregnancy or Breastfeeding", "Hypertension (high blood pressure)", 
                                       "Diabetes", "Obesity", "Cardiovascular diseases", 
                                       "Respiratory diseases", "Chronic kidney disease", 
                                       "Arthritis and musculoskeletal disorders", "Mental health disorders", 
                                       "Gastrointestinal disorders", "Thyroid Disorders"])

if st.button("Generate Prescription"):
    if name and diagnosis and age and weight:
        prescription = generate_prescription(name, diagnosis, age, sex, weight, current_medications, allergies, coexisting_conditions)
        st.text("Prescription:")
        st.write(prescription)
        # pdf_file_path = save_pdf(prescription)
        # st.markdown(f"Download [Prescription PDF](/{pdf_file_path})")
    else:
        st.warning("Please fill in all the required information.")

    
