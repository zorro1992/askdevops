import qrcode
img = qrcode.make("https://www.udemy.com/course/50-devops-interview-questions-answers/")
img.save("my_udemy_course.png")