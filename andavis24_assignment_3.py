# -----------------------------------
# COMP 163: Assignment 3
# Personal Data Portfolio
# Author: Ajani Davis
# -----------------------------------

# Personal Information Storage
full_name = "Ajani Davis"
student_email = "andavis24@ncat.edu"
hometown = "Houston, TX"
graduation_semester = "Spring 2029"
major = "Computer Science"

# Academic Data Organization
current_course_list = ["COMP 163", "MATH 132", "ENG 100", "COMP 121"]
completed_course_list = ["Calculus 1","Micro Economics"]
credit_hours_list = [3, 3, 3, 1]  # Corresponding to current courses
gpa_history_list = [4.0]  # Semester GPAs

# Contact Information Storage
emergency_contact_tuple = ("Mom", "Shani Davis", "973-207-0835")
home_address_tuple = ("26006 Fiona Sky Lane", "Katy, TX", "77494")
instagram_info_tuple = ("Instagram", "@ajd.london_", 311)
twitter_info_tuple = ("Twitter", "@ajd.london_", 127)
birthday_tuple = ("Birthday", 9, 27, 2006)

# Interest Tracking
current_skills_set = {"Python basics", "HTML", "Problem solving", "Time management", "Leadership"}
skills_to_learn_set = {"Data structures", "Git", "Web design", "Cyber Analytics"}
career_interests_set = {"Software development", "AI development", "Data science", "Cybersecurity"}
hobbies_set = {"Gaming", "Eating", "Basketball", "Music"}
entertainment_backlog_set = {"Naruto", "Stranger Things", "Blackish", "A different World"}

# Organizational Mapping
course_credits_dictionary = {"COMP 163": 3, "MATH 132": 3, "ENG 100": 3, "COMP 121": 1}
course_professors_dictionary = {"COMP 163": "Prof. Rhodes", "MATH 132": "Dr. Johnson", "ENG 100": "Dr. Turman", "COMP 121": "Dr. Rhodes"}
course_rooms_dictionary = {"COMP 163": "Gibbs 322", "MATH 132": "Online", "ENG 100": "GCB 102", "COMP 121": "Graham 210"}
monthly_budget_dictionary = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hours_per_subject_dictionary = {"Programming": 9, "Math": 8, "English": 5,}
contact_directory_dictionary = {"Mom": "973-207-0835", "Roommate": "282-345-3844",
                                "Academic Advisor": "336-384-4659"}

# -----------------------------------
# Section 6: Required Calculations
# -----------------------------------
total_current_credits = sum(credit_hours_list)
cumulative_gpa = sum(gpa_history_list) / len(gpa_history_list)
count_completed_courses = len(completed_course_list)
total_study_hours = sum(study_hours_per_subject_dictionary.values())
academic_load = total_current_credits + total_study_hours
monthly_budget_total = sum(monthly_budget_dictionary.values())
daily_food_budget = round(monthly_budget_dictionary["Food"] / 30, 2)
annual_budget_projection = monthly_budget_total * 12
study_cost_per_hour = round(monthly_budget_dictionary["Books"] / total_study_hours, 2)

# -----------------------------------
# Section 7: Analytics Calculations
# -----------------------------------
total_followers = instagram_info_tuple[2] + twitter_info_tuple[2]
current_skills_count = len(current_skills_set)
skills_to_learn_count = len(skills_to_learn_set)
contact_count = len(contact_directory_dictionary)
backlog_count = len(entertainment_backlog_set)
academic_workload = total_current_credits + len(current_course_list)

# -----------------------------------
# Final Output (No loops, just prints)
# -----------------------------------
print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {graduation_semester}")
print(f"Major: {major}\n")

print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_current_credits} credits across {len(current_course_list)} courses")
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print(f"Weekly Study Time: {total_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour\n")

print("Current Courses:")
print(f"COMP 163 - {course_credits_dictionary['COMP 163']} credits - {course_professors_dictionary['COMP 163']} - {course_rooms_dictionary['COMP 163']}")
print(f"MATH 150 - {course_credits_dictionary['MATH 150']} credits - {course_professors_dictionary['MATH 150']} - {course_rooms_dictionary['MATH 150']}")
print(f"ENG 101 - {course_credits_dictionary['ENG 101']} credits - {course_professors_dictionary['ENG 101']} - {course_rooms_dictionary['ENG 101']}")
print(f"HIS 105 - {course_credits_dictionary['HIS 105']} credits - {course_professors_dictionary['HIS 105']} - {course_rooms_dictionary['HIS 105']}\n")

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills_set}")
print(f"Learning Goals: {skills_to_learn_set}")
print(f"Career Interests: {career_interests_set}")
print(f"Skills Currently Have: {current_skills_count}")
print(f"Skills Want to Learn: {skills_to_learn_count}\n")

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget_dictionary['Food']} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget_dictionary['Entertainment']}")
print(f"Books: ${monthly_budget_dictionary['Books']}")
print(f"Transportation: ${monthly_budget_dictionary['Transportation']}")
print(f"Annual Projection: ${annual_budget_projection}\n")

print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact_tuple[1]} ({emergency_contact_tuple[0]}) - {emergency_contact_tuple[2]}")
print(f"Home Address: {home_address_tuple[0]}, {home_address_tuple[1]}, {home_address_tuple[2]}")
print(f"Social Media Presence: {total_followers} followers across 2 platforms")
print(f"Key Contacts: {contact_count} people in directory\n")

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {count_completed_courses}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog : {backlog_count} items")
print(f"Current Hobbies: {len(hobbies_set)} activities")
print("====================================================")
