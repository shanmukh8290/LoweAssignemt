# LowesAssignment

# UserManagement Module
 This Assignment includes the development of APIs using python and django for the management of user data and doing CRUD operations on the user information.
    
## 1. Prerequisites
Install python-3.7.2 and python-pip. Follow the steps from the below reference document based on your Operating System. Reference: https://docs.python-guide.org/starting/installation/

## 2. Setup Virtual Environment:
### a. Using conda:
    #Install AnacondaPrompt (if not available):
    https://docs.anaconda.com/anaconda/install/windows/

    #Install Virtual environment
 
    conda create -n virtualenv
 
    #Activating the virtual environment
 
    conda activate virtualenv
 
### b. Using pip (for windows):
    ##Install package:
 
    pip install virtualenv
 
    ##Install Virtual environment:
 
    virtualenv <path where you need to install venv> mypython
    
    #Activating Virtual environment:
 
    cd <go to the path where venv is installed>
    
    mypython\Scripts\activate
    
## 3.  Clone git Repository:
 Clone the repository using the below command:
 
    git clone "https://github.com/shanmukh8290/LoweAssignemt.git"
    
## 4. Install Requirements:
    cd LoweAssignemt
    pip install -r "requirements.txt"
    
## 5. Setting the Database:
 There is no setting for the database because here we used sqlite as default database. Hence, no change required in settings.py file.
 
## 6. Run the server:
 Once the above process is completed, we need to run the below commands to create table in database.
 
     # Make Migrations
     python manage.py makemigrations
     python manage.py migrate
     
     # Run Server
     python manage.py runserver

## 7. URLs to check the CRUD operations for the user management module:
 Create User:  http://127.0.0.1:8000/user/create/  (POST)
 
 ![Create_User](https://user-images.githubusercontent.com/60460030/121009088-5db1bc00-c7b1-11eb-83a5-2dd0103de1b7.png)

 User Details after Creating User:  http://127.0.0.1:8000/user/userDetails/  (GET)
 
 ![userdetailsaftercreating](https://user-images.githubusercontent.com/60460030/121007387-9cdf0d80-c7af-11eb-8ec5-cfa782a429fa.png)

 Update User:  http://127.0.0.1:8000/user/updateUser/  (POST)
 
 ![update_user](https://user-images.githubusercontent.com/60460030/121009110-67d3ba80-c7b1-11eb-86f8-e16294ebef85.png)

 User Details after Modifying User:  http://127.0.0.1:8000/user/userDetails/  (GET)
 
 ![userdetailsafterupdating](https://user-images.githubusercontent.com/60460030/121008734-f136bd00-c7b0-11eb-93c2-a0e99e641359.png)

 Delete User:  http://127.0.0.1:8000/user/deleteUser/  (POST)
 
 ![Delete_User](https://user-images.githubusercontent.com/60460030/121008417-9a30e800-c7b0-11eb-8895-3cbfba16269c.png)
 
 User Details after Deleting User:  http://127.0.0.1:8000/user/userDetails/  (GET)
  
 ![userdetailsafterdeleting](https://user-images.githubusercontent.com/60460030/121008460-a6b54080-c7b0-11eb-8eec-51f0c9fce84c.png)
