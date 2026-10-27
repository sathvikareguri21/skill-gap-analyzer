
from flask import Flask, render_template, request

app = Flask(__name__)

# Job roles and their required skills
job_roles = {
    "Software Developer": ["Python", "Java", "Data Structures", "Algorithms", "Git"],
    "Python Developer": ["Python", "SQL", "Flask", "APIs", "Git"],
    "Java Developer": ["Java", "OOP", "SQL", "Spring Boot", "Git"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "Responsive Design", "Git"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
    "Backend Developer": ["Python", "SQL", "APIs", "Databases", "Git"],
    "Full Stack Developer": ["HTML", "CSS", "JavaScript", "Python", "SQL", "APIs"],
    "Mobile App Developer": ["Java", "Kotlin", "APIs", "Databases", "Git"],
    "Data Analyst": ["Python", "SQL", "Excel", "Statistics", "Power BI"],
    "Data Scientist": ["Python", "SQL", "Statistics", "Machine Learning", "Pandas"],
    "Data Engineer": ["Python", "SQL", "ETL", "Databases", "Cloud Computing"],
    "Machine Learning Engineer": ["Python", "Machine Learning", "Statistics", "Pandas", "Scikit-learn"],
    "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "APIs", "Mathematics"],
    "Business Analyst": ["Excel", "SQL", "Communication", "Data Analysis", "Power BI"],
    "Business Intelligence Analyst": ["SQL", "Excel", "Power BI", "Data Modeling", "Data Analysis"],
    "Cybersecurity Analyst": ["Networking", "Linux", "Cybersecurity", "Python", "Risk Analysis"],
    "Cloud Engineer": ["Linux", "Networking", "Cloud Computing", "Python", "Docker"],
    "DevOps Engineer": ["Linux", "Git", "Docker", "CI/CD", "Cloud Computing"],
    "Network Engineer": ["Networking", "Linux", "Troubleshooting", "Cybersecurity", "Cloud Computing"],
    "System Administrator": ["Linux", "Networking", "System Administration", "Security", "Scripting"],
    "UI/UX Designer": ["UI Design", "UX Research", "Wireframing", "Prototyping", "Figma"],
    "Graphic Designer": ["Graphic Design", "Typography", "Color Theory", "Photoshop", "Illustrator"],
    "Product Designer": ["UI Design", "UX Research", "Prototyping", "Figma", "Communication"],
    "Software Tester": ["Testing", "Test Cases", "Bug Reporting", "SQL", "SDLC"],
    "QA Engineer": ["Testing", "Test Cases", "Automation Testing", "SQL", "SDLC"],
    "Automation Tester": ["Python", "Selenium", "Testing", "Test Automation", "Git"],
    "Project Manager": ["Project Planning", "Communication", "Leadership", "Risk Management", "Agile"],
    "Product Manager": ["Product Strategy", "Communication", "Data Analysis", "Agile", "User Research"],
    "Digital Marketing Specialist": ["SEO", "Content Marketing", "Social Media", "Analytics", "Email Marketing"],
    "HR Analyst": ["Excel", "Data Analysis", "Communication", "HR Analytics", "Reporting"],
    "Financial Analyst": ["Excel", "Financial Modeling", "Accounting", "Data Analysis", "Forecasting"],
    "Accountant": ["Accounting", "Excel", "Financial Reporting", "Taxation", "Bookkeeping"],
    "Database Administrator": ["SQL", "Database Management", "Backup and Recovery", "Security", "Performance Tuning"],
    "Technical Support Engineer": ["Troubleshooting", "Networking", "Operating Systems", "Communication", "Customer Support"],
    "IT Consultant": ["Networking", "Problem Solving", "Communication", "Cloud Computing", "Project Planning"],
    "Game Developer": ["Python", "C#", "Game Design", "Mathematics", "Git"],
    "Blockchain Developer": ["Python", "Cryptography", "Blockchain", "Smart Contracts", "Git"],
    "Embedded Systems Engineer": ["C", "C++", "Microcontrollers", "Electronics", "Debugging"],
    "Robotics Engineer": ["Python", "C++", "Robotics", "Mathematics", "Sensors"],
    "Technical Writer": ["Technical Writing", "Documentation", "Communication", "Research", "Editing"]
}


@app.route("/")
def home():
    return render_template("index.html", job_roles=sorted(job_roles.keys()))


@app.route("/analyze", methods=["POST"])
def analyze():
    name = request.form.get("name", "").strip()
    target_job = request.form.get("target_job", "").strip()
    skills_text = request.form.get("skills", "").strip()

    if not name or target_job not in job_roles or not skills_text:
        return "Please enter your name, skills, and select a valid job role.", 400

    # Convert entered skills into a list
    current_skills = [
        skill.strip()
        for skill in skills_text.split(",")
        if skill.strip()
    ]

    # Compare skills without case sensitivity
    current_skill_set = {skill.casefold() for skill in current_skills}
    required_skills = job_roles[target_job]

    matched_skills = [
        skill for skill in required_skills
        if skill.casefold() in current_skill_set
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill.casefold() not in current_skill_set
    ]

    if required_skills:
        match_percentage = round(
            len(matched_skills) / len(required_skills) * 100
        )
    else:
        match_percentage = 0

    suggestions = [
        f"Start learning {skill} through tutorials and practical exercises."
        for skill in missing_skills
    ]

    return render_template(
        "result.html",
        name=name,
        target_job=target_job,
        current_skills=current_skills,
        required_skills=required_skills,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        suggestions=suggestions,
        match_percentage=match_percentage
    )


if __name__ == "__main__":
    app.run(debug=True)


