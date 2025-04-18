# Assessment3

Introduction;
This project represents a fun, interactive python-based grade management system intended to help users, such as teachers or administrators,and  add as well as view student grade information easily. The main aim of this project is to build a working program and also to write code observing software design principles, to keep it clean, organized, and fututre-proof.
This is a simple python program for managing student grade data. It allows users to;
1. Add a student's name, roll number, and 3 grades,
2. Automatically calculate their average and result (Passed/Failed),
3. View all entered student records.

Goal of the Project; The main goal of this project consists of demonstarting how "software design principles" can transform unorganized code into clean maintainabe and extensible arrangements.

Software Design Principles;
1. KISS(Keep it Simple, Stupid): The code is simple and easy to use, the logic is broken down into small, understandable pieces.
2. DRY(Don't Repeat Yourself): This principle avoid repeating the grade calculation and pass/fail logic and, the input and processing logic are encapsulated into reusable functions.
3. Single Responsibility Principle: In this project, each function does exactly one job:
   a. Calculate_avegare()--> Calculates average
   b. Check_pass_fail()--> Checks result
   c. add_student()--> handles input
   d. display_students()--> handles output
4. Separation of Concerns: In this principle; Input, processing, and output are handled in different functions. and main function controls the flow, helper functions do the work.
5. Open/Closed Principle: The code is open to extension(you can add more features), but closed to modification of core logic.
6. YAGNI(You Aren't Gonna Need It): This principle helps to focus on what's needed for the current requirement and avoid unnecessary features or overengineering.
7. Avoid Premature Optimization: I have not added any complex logic before it's needed, and i have more focused on clarity over performance.
8. Refractor, Refractor, Refractor: The principle makes the code easier to test, understand, and maintain. here original loop-based code was split into small functions.
9. Clean Code > Clever: The principle simply tells that clean code is better than clever code and I have done the same by avoiding fancy tricks, clarity is the priority here, overhere i have used meaningful names like add_student, display_students.

Conclusion;
This project was created in order to show how even a beginner python program can follow software design principles. Each function has within it a clear purpose. The logic is broken into various understanable chunks, and the code is simple enough for modifications or extension later on, such as adding further subjects or else saving data to some file. The project reflects a strong grasp of clean coding, structure, seperation of logic. It's quite a helpful base for future academic projects. It can be real tool for teachers managing student data.
