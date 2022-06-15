# unopass

A platfrom built for handling and managing users password across different platform

# Routers

    #User router

        1. user creation
            route : "unopass/user/create"

            This is a router used for handling user creation.
            It takes 4 parameter which is : first name, lastname, email(unique) and password



    #Password router

    1. create new password
        route : "unopass/password/add"

        This router handles the creation of user password in relation to the platform
        It takes 3 parameter which is : Plaform, username/email, password

    2. get list of users saved password
        route : "unopass/password/"

        This routers process and return all password saved by a particular user
        This requires the user to be signed in, as the router fetch information in relation to the signed in user
        Takes ones parameter which is : user_id. NOTE: This is handled by the the browser once user is singned in. The router fetch a unique token from the browser, which is decoded to get users information.

    3. Get user by platform

        router : "unopass/password/{platform}"
        This router returns user password based on the platform selected
        Takes 1 parameter : Platform


    4. Edit password
        .......


    # User Authentication(Login)

    1. Login

    route : "unopass/login/token"
    This router authenticates users

    Takes 2 parameters : username/email and password
