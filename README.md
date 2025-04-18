# Assessment3

Introduction;
This project represents a fun, interactive python-based grade management system intended to help users, such as teachers or administrators,and  add as well as view student grade information easily. The main aim of this project is to build a working program and also to write code observing software design principles, to keep it clean, organized, and fututre-proof.
This is a simple python program for managing student grade data. It allows users to;
1. Add a student's name, roll number, and 3 grades,
2. Automatically calculate their average and result (Passed/Failed),
3. View all entered student records.

Goal of the Project; The main goal of this project consists of demonstarting how "software design principles" can transform unorganized code into clean maintainabe and extensible arrangements.

Software Design Principles;
1. KISS(Keep it Simple, Stupid): The code is simple and easy to use, the logic is broken down into small, understandable pieces. I implemented transparent programming logic while keeping variable names simple and using basic control structures.
   
2. DRY(Don't Repeat Yourself): This principle avoid repeating the grade calculation and pass/fail logic and, the input and processing logic are encapsulated into reusable functions. I used functions like calculate_average() and check_pass_fail() to prevent repetition of the same logical separations.

3. Open/Closed Principle: The code is open to extension(you can add more features), but closed to modification of core logic.
   
4.Composition > Inheritance:   I chose to construct this project through composition which enables smaller reusable functions to be combined. The program became more understandable because of its composition design which provided future flexibility to modify and extend functionality.

5.Single Responsibility Principle: In this project, each function does exactly one job:
   a. Calculate_avegare()--> Calculates average
   b. Check_pass_fail()--> Checks result
   c. add_student()--> handles input
   d. display_students()--> handles output
   Each function performs a single duty within my program wither by handling   input or processing data or presenting output.
   
6. Separation of Concerns: In this principle; Input, processing, and output are handled in different functions. and main function controls the flow, helper functions do the work. I designed my program to contain the three essential sections which involve user input and grade processing as well as output display.
   
7. YAGNI(You Aren't Gonna Need It): This principle helps to focus on what's needed for the current requirement and avoid unnecessary features or overengineering.I limited the application to essential functionality for grade management( inputting grades and computing averages while determinig pass and fail results) instead of adding features such as file saving or online integration at this stage.
   
8. Avoid Premature Optimization: I have not added any complex logic before it's needed, and i have more focused on clarity over performance.
   
9. Refractor, Refractor, Refractor: The principle makes the code easier to test, understand, and maintain. here original loop-based code was split into small functions. I improved my code after testing by simplifying sections by cutting duplicate prints and making variable names more descriptive.
   
10. Clean Code > Clever: The principle simply tells that clean code is better than clever code and I have done the same by avoiding fancy tricks, clarity is the priority here, overhere i have used meaningful names like add_student, display_students.

Conclusion;
I have created this project in such a way to show how even a beginner python program can follow software design principles. Each function has within it a clear purpose. The logic is broken into various understanable forms, and the code is simple enough for modifications or extension later on, such as adding further subjects or else saving data to some file. The project reflects a strong grasp of clean coding, structure, seperation of logic. It's quite a helpful base for future academic projects. It can be real tool for teachers managing student data.
