# Assessment3

Overview:
The provided code establishes a straightforward passenger booking system which enables users to enter details then select ferry services before receiving approval according to toal service cost. The system creates specific ticket IDs and approval references while enabling the production of booking statistics. The sytem operates using object_oriented methods through a central class named BookingSystem that manages customer data and ferry service specifications and booking approvals and booking performance logs. The BookingSystem class tracks multiple bookings through a global ticket ID counter.

Steps in the code:
1. BookingSystem Class Initialization: When a new BookingSystem object is created, it initializes the passenger's details, such as ticket ID, passenger name, date of travel, and form of ID. The global ticket_id_counter is incremented to ensure unique ticket IDs.
2. Customer Information: The customer_info() method requests users to enter ID type along with ID number and passenger name information.
3. Ferry Service Details: The ferry_service_details() method enables users to submit service items alongside their corresponding costs while accumulating the service total. This method adds together costs from all chosen services.
4. Booking Approval: The booking_approval() method evaluates the total cost against 300 to determine whether the status should be "Approved" or "Not Approved". The method produces an approval reference from part of the ID number upon successful approval.
5. Booking Information Display: The display_booking_info() method will display all booking-related information comprising passenger data along with ticket ID, total cost amount and approval reference details.
6. Booking Statistics: The static booking_statistic() method creates statistics from the status of all bookings which include approved, pending and not approved conditions.
7. Main Program Flow: The program allows the user to enter booking details for multiple passengers, performs the booking process, displays initial statistics, and then shows the final statistics after approval.

Code Quality Principles Analysis:
1. KISS(Keep it Simple Stupid): The code is straightforward and easy to understand, adhering to the KISS principle. The logic is simple, and methods are focused on specific tasks. There's no unnecessary complexity, which makes it easier to maintain.
2. DRY(Don't Repeat Yourself): The code demonstartes a minor violation of DRY although it occurs in the booking_approval() and display_booking_info() methods. Two different methods need to access identical booking information before printing the data. A method should be created to handle booking data formatting and printing to eliminate duplicate code.
3. Open/Closed Principle: The code allows some level of extension through additional service items or changed approval procedures yet remains insufficiently unalterable for modification purposes. Any changes made to new service types or approval process methods need modifications to the class structure itself. Abstracting the approval process through a separate class or using a strategy pattern would enhance the closed nature of modification.
4. Compostion > Inheritance: The code structure follows composition approach instead of inheritance. The BookingSystem class conducts booking processes through its own operations instead of using subclassing inheritance behavior. By placing service item procedures into their own class composition becomes more flexible.
5. Single Responsibility Principle: The BookingSystem class executes multiple responsibilities by managing customer data alongside service facts and bookings along with presentation of statistical information. The code becomes more manageable through modular organization because each responsibility exists as its own distinct class.
6. Separation of Concerns: The code needs to improve how different domains are differentiated from each other. The BookingSystem class takes responsibility for both conducting approvals and handling input/output operations. Each part of concern should exist in independent classes or layers such as controllers for user interaction and services for business logic which would maintain clear responsibilities for each class.
7. YAGNI(You Aren't Gonna Need It): The current code includes no extra features that do not serve a necessary purpose. The current approval_reference generation logic presents future limitations because adding additional complex reference number generation logic in the future may lack flexibility. The code base operates with straightforward functionality.
8. Avoid Premature Optimization: The code implementation avoids performing unnecessary optimization before its execution. The code design follows easy logic that avoids artificial complexity or efficiency enhancements. The code structure includes basic loops together with fundamental computational methods because the system currently operates at this level.
9. Refactor, Refactor, Refactor: The code needs restructuring to enhance its maintainability characteristics. Our code needs reorganization into different classes and methods to enforce the Single Responsibility Principle throughout services management and booking information calculations.
10. Clean Code > Clever Code: This program code presents straightforward logic which avoids complex design choices. Each method functions for only a single reason so code management and modification tasks become simpler.

Limitations:
1. Scalability:The system operates efficiently when dealing with five bookings yet its performance might decrease as booking numbers grow. An extensive number of bookings could need improved data storage optimization through a database implementation.
2. Lack of Error Handling: The application lacks proper error management features that would handle unexpected user data entry. User input validation should be added to the system to ensure correct date formats and positive numbers in service pricing.
3. No Data Persistence: The completion of the program results in permanent data loss of all booking records. A realistic system needs data preservation techniques to save records either in files or databases.
4. User Experience: The user is asked to input information repeatedly in the console, which might not be the most user-friendly approach.The user experience could be improved through implementation of either a graphical interface or a web-based front-end.

Conclusion:
The booking system contains essential features which display a consistently logical structure and functional approach. Furthermore the code follows numerous clean code principles including KISS and DRY and YAGNI yet requires better concern segmentation with Single Responsibility Principle method refactoring and error handling and data persistence implementation. The system's functionality will improve through its modular design and maintainable code structure as well as scalability which ultimately makes it viable for practical usage.

