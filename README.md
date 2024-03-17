### Asset Tracker <br/>

### Project Description:
1. To track corporate assets such as phones, tablets, laptops and other gears handed out to employees.
2. The application might be used by several companies
3. Each company might add all or some of its employees
4. Each company and its staff might delegate one or more devices to employees for a certain period of time
5. Each company should be able to see when a Device was checked out and returned
6. Each device should have a log of what condition it was handed out and returned

### Project Features:
I have used Django Rest Framework for creating the API's. <br/>
I have used SQLITE3 database for this project. <br/>
I have used Django ORM for database operations. <br/>
I have used Django Serializer for creating the serializers. <br/>
I have used Django Rest Framework Spectacular for creating the API documentation. <br/>
I have used Pytest for creating the tests. <br/>
I have used Postman & swagger for testing the API's. <br/>

### Steps to run the project:
1. Run the following commands:
    - py manage.py makemigrations
    - py manage.py migrate 
    - py manage.py createsuperuser
    - py manage.py runserver
2. Following url for performing API testing in swagger:<br/>
   - url: http://127.0.0.1:8000/api/schema/swagger-ui/

3. You can also run the tests using the following command:
   - pytest
4. API documentation using the following url:
    - url:http://127.0.0.1:8000/api/schema/redoc/
    - pdf:https://drive.google.com/file/d/1WAa0Fd6kxVJetIB1KMHzMpPNQzHc63ua/view?usp=sharing


### Database Schema:
This implementation has 4 main models: Company, Device, Employee, and DeviceAssign.<br/>
1. `Company` stores information about the companies using the app.<br/>
2. `Employee` represents the company's staff, with a one-to-one relationship to a Django user and employee belongs to the company.<br/>
3. `Device` represents the corporate assets, with information such as their name, description, serial number, condition, and which company they belong to.<br/>
4. `DeviceAssign` represents the assignments of devices to employees, with a foreign key to both the Device and Employee models, as well as the assignment and return dates with device conditions<br/>

## Swagger UI
`Compaines API Routes` 

![1](https://github.com/Zayed-Rahat/device-tracker/blob/main/UI_SS/companies_api.png)

`Devices API Routes`

![2](https://github.com/Zayed-Rahat/device-tracker/blob/main/UI_SS/devices_api.png)

`Employess API Routes`

![3](https://github.com/Zayed-Rahat/device-tracker/blob/main/UI_SS/employees_api.png)
