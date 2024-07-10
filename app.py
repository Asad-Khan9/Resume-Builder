import streamlit as st
import os
from datetime import time, date, datetime
import pdfkit
from io import BytesIO
import base64

# Define the save directory
save_directory = r"C:\Users\Night\OneDrive\Documents\Builder_resumes"

def get_binary_file_downloader_html(bin_data, file_label='File', btn_label='Download', file_name='file.pdf'):
    bin_str = base64.b64encode(bin_data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_name}">{btn_label}</a>'
    return href

# Ensure the directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

st.title("Resume Builder")
all_details = {}
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Personal details", "Education", "Experience", "Projects", "Achievements", "Technical Skills", "Save resume"])

with tab1:
    st.header("Personal Details")
    all_details['name'] = st.text_input("Enter your name", key="name")
    all_details['phone_number'] = st.text_input("Enter your phone number", key="phone")
    all_details['mail_id'] = st.text_input("Enter your mail id", key="email")   
    all_details['linkedin_link'] = st.text_input("Enter your LinkedIn link", key="linkedin")
    all_details['github_link'] = st.text_input("Enter your GitHub link", key="github")
    all_details['summary'] = st.text_area("Write a small summary about yourself", key="summary")

with tab2:
    st.header("Education")
    all_details['education'] = []
    num_edu = st.number_input("Number of educational qualifications", min_value=1, value=1, key="num_edu")
    for i in range(num_edu):
        st.subheader(f"Education {i+1}")
        edu = {}
        edu['institution'] = st.text_input(f"Institution name {i+1}", key=f"edu_institution_{i}")
        edu['location'] = st.text_input(f"Location {i+1}", key=f"edu_location_{i}")
        edu['degree'] = st.text_input(f"Degree {i+1}", key=f"edu_degree_{i}")
        edu['time_period'] = st.text_input(f"Time period {i+1}", key=f"edu_time_period_{i}")
        edu['grade'] = st.text_input(f"Grade/CGPA {i+1}", key=f"edu_grade_{i}")
        all_details['education'].append(edu)

with tab3:
    st.header("Experience")
    all_details['experience'] = []
    num_exp = st.number_input("Number of experiences", min_value=0, value=1, key="num_exp")
    for i in range(num_exp):
        st.subheader(f"Experience {i+1}")
        exp = {}
        exp['company'] = st.text_input(f"Company name {i+1}", key=f"exp_company_{i}")
        exp['position'] = st.text_input(f"Position {i+1}", key=f"exp_position_{i}")
        exp['time_period'] = st.text_input(f"Time period {i+1}", key=f"exp_time_period_{i}")
        exp['description'] = st.text_area(f"Description of responsibilities {i+1}", key=f"exp_description_{i}")
        all_details['experience'].append(exp)

with tab4:
    st.header("Projects")
    all_details['projects'] = []
    num_proj = st.number_input("Number of projects", min_value=0, value=1, key="num_proj")
    for i in range(num_proj):
        st.subheader(f"Project {i+1}")
        proj = {}
        proj['name'] = st.text_input(f"Project name {i+1}", key=f"proj_name_{i}")
        proj['technologies'] = st.text_input(f"Technologies used {i+1}", key=f"proj_tech_{i}")
        proj['description'] = st.text_area(f"Project description {i+1}", key=f"proj_desc_{i}")
        all_details['projects'].append(proj)

with tab5:
    st.header("Achievements")
    all_details['achievements'] = st.text_area("List your achievements (one per line)", key="achievements")

with tab6:
    st.header("Technical Skills")
    all_details['languages'] = st.text_input("Programming Languages", key="languages")
    all_details['skills'] = st.text_input("Skills", key="skills")
    all_details['libraries'] = st.text_input("Libraries/Frameworks", key="libraries")
    all_details['certifications'] = st.text_input("Certifications", key="certifications")

with tab7:
    st.header("Resume")
    html_content = ""
    if st.button("Generate PDF", key="save_pdf"):
        html_content = f"""
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{all_details['name']} - Resume</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    font-size: 14px;
                    line-height: 1.2;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 100%;
                    max-width: 800px;
                    margin: auto;
                    padding: 10px;
                }}
                header {{
                    text-align: center;
                    margin-bottom: 10px;
                }}
                header h1 {{
                    margin: 0;
                    font-size: 18px;
                }}
                header p {{
                    margin: 5px 0;
                    font-size: 14px;
                }}
                section {{
                    margin-bottom: 10px;
                }}
                h2 {{
                    color: #2c3e50;
                    border-bottom: 1px solid #2c3e50;
                    padding-bottom: 2px;
                    margin: 5px 0;
                    font-size: 14px;
                }}
                h3 {{
                    color: #34495e;
                    margin: 5px 0;
                    font-size: 12px;
                }}
                p {{
                    margin: 2px 0;
                }}
                .edu-item, .project-item, .exp-item {{
                    margin-bottom: 5px;
                    font-size: 17px;
                }}
                ul {{
                    padding-left: 20px;
                    margin: 5px 0;
                }}
                .skills p {{
                    margin: 2px 0;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <header>
                    <h1>{all_details['name']}</h1>
                    <p>{all_details['phone_number']} | {all_details['mail_id']} | {all_details['linkedin_link']} | {all_details['github_link']}</p>
                </header>
                <section class="summary">
                    <h2>Summary</h2>
                    <p>{all_details['summary']}</p>
                </section>
                <section class="education">
                    <h2>Education</h2>
        """

        for edu in all_details['education']:
            html_content += f"""
                    <div class="edu-item">
                        <h3>{edu['institution']} - {edu['location']}</h3>
                        <p>{edu['degree']} | {edu['time_period']} | Grade/CGPA: {edu['grade']}</p>
                    </div>
            """

        html_content += """
                </section>
                <section class="experience">
                    <h2>Experience</h2>
        """

        for exp in all_details['experience']:
            html_content += f"""
                    <div class="exp-item">
                        <h3>{exp['company']} - {exp['position']}</h3>
                        <p>{exp['time_period']}</p>
                        <p>{exp['description']}</p>
                    </div>
            """

        html_content += """
                </section>
                <section class="projects">
                    <h2>Projects</h2>
        """

        for proj in all_details['projects']:
            html_content += f"""
                    <div class="project-item">
                        <h3>{proj['name']}</h3>
                        <p><strong>Technologies:</strong> {proj['technologies']}</p>
                        <p>{proj['description']}</p>
                    </div>
            """

        html_content += """
                </section>
                <section class="achievements">
                    <h2>Achievements</h2>
                    <ul>
        """

        for achievement in all_details['achievements'].split('\n'):
            if achievement:
                html_content += f"<li>{achievement}</li>"

        html_content += f"""
                    </ul>
                </section>
                <section class="skills">
                    <h2>Technical Skills</h2>
                    <p><strong>Languages:</strong> {all_details['languages']}</p>
                    <p><strong>Skills:</strong> {all_details['skills']}</p>
                    <p><strong>Libraries/Frameworks:</strong> {all_details['libraries']}</p>
                    <p><strong>Certifications:</strong> {all_details['certifications']}</p>
                </section>
            </div>
        </body>
        </html>
        """
        st.success("Resume generated successfully!")

        options = {
            'page-size': 'A4',
            'margin-top': '0.5in',
            'margin-right': '0.5in',
            'margin-bottom': '0.5in',
            'margin-left': '0.5in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        
        # Generate PDF in memory
        pdf_data = pdfkit.from_string(html_content, False, options=options)
        
        # Offer the PDF as a download
        st.markdown(get_binary_file_downloader_html(pdf_data, 'Resume.pdf', 'Download PDF'), unsafe_allow_html=True)









    # if st.button("save", key="save_pdf "):
    #     # Save the HTML content as a PDF
    #     # Define the PDF filename
    #     pdf_filename = f"{all_details['name']}{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    #     # Define the PDF path
    #     pdf_path = os.path.join(save_directory, pdf_filename)

    #     # PDF generation options
        # options = {
        #     'page-size': 'A4',
        #     'margin-top': '0.5in',
        #     'margin-right': '0.5in',
        #     'margin-bottom': '0.5in',
        #     'margin-left': '0.5in',
        #     'encoding': "UTF-8",
        #     'no-outline': None
        # }
    
    #     # Save the HTML content as a PDF
    #     pdfkit.from_string(html_content, pdf_path, options=options)
    #     st.success(f"Resume saved as PDF: {pdf_path}")

    #     # # Provide a download button for the generated PDF
    #     with open(pdf_path, "rb") as pdf_file:
    #         PDFbyte = pdf_file.read()

    #     st.download_button(label="Download PDF", 
    #                        data=PDFbyte,
    #                        file_name=pdf_filename,
    #                        mime='application/octet-stream')