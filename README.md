# TerraTrade
TerraTrade is a smart marketplace connecting local farmers with consumers. Farmers can manage produce, receive weather updates, and adjust pricing dynamically. Customers can interact with farmers via calls, rate products, and track deliveries. TerraTrade optimizes farm-to-table with secure payments and analytics for farmers.

## Steps:
1. Inside root folder: (For backend)
   - $ virtualenv backend
   - $ cd backend
   - $ Scripts\activate 
2. pip install Django django-cors-headers djangorestframework psycopg2 django-phonenumber-field django-phonenumbers
3. For starting django backend project, run:
   - $ django-admin startproject TerraTrade
   - $ mv TerraTrade src
   - $ cd src
   - Start a new app in the project:
      - $ python manage.py startapp account
      - $ python manage.py startapp pages
      - $ python manage.py migrate
      - $ python manage.py createsuperuser


## Database Setup
- Install `pgAdmin`
- Create a new **Role/User** with `Username`=`sa` and `Password`=`sa`
- For the Role/User, in `Properties` section under `Privilege` subsection, **Turn on** the **Can Login** option
- Then create a database named  `TerraTrade` giving user `sa` as the **Owner** Permission


Added This for Test
This is very important for start