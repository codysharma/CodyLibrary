# CodyLibrary  
A library website with functionality tied to authorization level: browsing and "contact us" without login, borrowing books and registering for events with user, CRUD functionality of models with admin. 

Tech used: 
Django, Django Templates, PostgreSQL as backend, Python, Dynamic API calls, Boostrap, Bootstwatch, JS

Features:
-Django models, including use of ForeignKey and ManytoMany
-Search function through books model, including linked field
-Ticketing system with contact model having issue, resolved status, last contact
-Display list of books tied to current user logged in
-Views pages based on filter through the database

Future ideas:
-Map page refinement - tooltips on hover to show section title and list of books, fixing placement of icons
-Turn events list page into an actual calendar - need to serialize the Events model for an API call
-Make a "requests" model and button for users to request books already loaned out.  

Landing page:
![image](https://github.com/codysharma/CodyLibrary/assets/123990673/01d06670-d109-4288-89e9-7464fab0048f)

Logged in to user level:
![image](https://github.com/codysharma/CodyLibrary/assets/123990673/acc9d0b5-96e0-4c37-a77f-5c7b838edd7d)

Map of the library with each icon as a link to the specific genre catalog:
![image](https://github.com/codysharma/CodyLibrary/assets/123990673/5a6de4ed-3326-4a57-8c83-f3d31393664c)

List of books individual user has borrowed:
![image](https://github.com/codysharma/CodyLibrary/assets/123990673/f9df39e6-bb9f-457d-9866-def9b8d3b0c0)

Contact us ticket list for admin access level:
![image](https://github.com/codysharma/CodyLibrary/assets/123990673/b2c0b292-2e54-4377-81be-66f3b8d80e44)
