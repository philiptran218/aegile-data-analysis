# Aegile Data Work

Data sources ranking:

## 1. oc2lab
(https://github.com/Western-OC2-Lab/Student-Performance-and-Engagement-Prediction-eLearning-datasets/tree/main)
- contains great process data including # logins, # forum posts, # quiz reviews, assignment submission times and engagement level
- also contains performance data such as quiz marks, assignment marks and overall course grade
- we can join the data on Student ID to predict how process data determines individual student performance

## 2. Student Performance Data 24 (SPD24)
(https://www.kaggle.com/datasets/nasirayub2/spd24-student-performance-data-revised-features?select=Student_Performance_Data%28SPD24%29.xlsx)
- has a little bit of process data such as class participation, attendance rate and homework completion rate
- LOTS of background/socioeconomic data, like previous academic performance, motivation levels, hours of sleep, diet quality, school type/location
- this is high school data, so doesn't exactly match our use case

## 3. Online Courses
(https://www.kaggle.com/datasets/thedevastator/online-course-user-engagement-data)
- good process data on student interaction with online courses provided by MIT and Harvard
- contains number of event interactions on learning platform, number of active days, number of videos played, number of forum posts
- data is quite unclean, requires lots of clean up before we can extract insights

## 4. xAPI Edu Data
(https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data/data)
- contains good process data from student learning platforms
- includes number of times students raised their hands, number of visited resources, course announcement views, discussion interactions
- data is for high school students from the Middle East, not the best for our use case

## 5. Student Lifestyle Dataset
(https://www.kaggle.com/datasets/steve1215rogg/student-lifestyle-dataset/data)
- contains mostly lifestyle/background data and also GPA to compare performance against
- includes daily study hours, daily extracurricular hours, daily sleep hours, stress levels...

## 6. Student Preferences Dataset
(https://www.kaggle.com/datasets/datasetengineer/slep-dataset/data)
- contains mostly student learning preferences at university such as preferred learning styles and formats
- also includes socioeconomic status, current course details and level of student engagement with course (mostly categorical data)

## 7. Group Work Data
(https://data.mendeley.com/datasets/jys6pdx3p3/2/files/fe3d6659-eb82-436d-acd9-c75499e65b2c)
- not really useful, provides info on team dynamics in group assessments
- looks at group engagement, peer assessment, and personal scores on assessment experience and fairness
