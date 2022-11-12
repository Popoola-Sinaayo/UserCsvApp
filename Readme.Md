# Clone the project or dowload the Zip Folder

## Install Dependencies

- open your terminal and migrate to the project folder

- type the command 'pip install -r requirements.txt'

## To create users

- open your terminal and migrate to the project folder

- type the command 'python users.py'

- the users.csv file will be created with 10 users

- (id,FirstName,LastName,Username,Email,Avatar,Gender,Dob,Address

4360,Dorsey,Labadie,dorsey.labadie,dorsey.labadie@email.com,<https://robohash.org/fugiatillonisi.png?size=300x300&set=set1,Genderfluid,2004-03-23,South> Kermitmouth

4068,Kimberlee,Reinger,kimberlee.reinger,kimberlee.reinger@email.com,<https://robohash.org/repudiandaenemodeserunt.png?size=300x300&set=set1,Agender,1998-04-02,East> Roryside

3007,Wallace,Lindgren,wallace.lindgren,wallace.lindgren@email.com,<https://robohash.org/estutsit.png?size=300x300&set=set1,Male,1982-08-29,Ashleymouth>

481,My,Mitchell,my.mitchell,my.mitchell@email.com,<https://robohash.org/omnissintaccusamus.png?size=300x300&set=set1,Non-binary,1978-06-20,New> Gusstad

7549,Cruz,Haag,cruz.haag,cruz.haag@email.com,<https://robohash.org/atqueaperiamexcepturi.png?size=300x300&set=set1,Genderqueer,1978-05-05,Corlissview>

420,Arlena,Olson,arlena.olson,arlena.olson@email.com,<https://robohash.org/sintesseerror.png?size=300x300&set=set1,Genderfluid,2003-05-15,South> Kyle

3339,Lawrence,Balistreri,lawrence.balistreri,lawrence.balistreri@email.com,<https://robohash.org/laudantiumoptiovero.png?size=300x300&set=set1,Genderfluid,2000-07-21,Emmerichview>

1266,Pansy,Heaney,pansy.heaney,pansy.heaney@email.com,<https://robohash.org/blanditiisestcorporis.png?size=300x300&set=set1,Male,1961-08-24,Stefanland>

2833,Darnell,Borer,darnell.borer,darnell.borer@email.com,<https://robohash.org/voluptasfacilisnihil.png?size=300x300&set=set1,Female,1991-07-05,Prohaskaton>

9354,Karleen,Gutkowski,karleen.gutkowski,karleen.gutkowski@email.com,<https://robohash.org/quiarchitectoquod.png?size=300x300&set=set1,Polygender,2000-04-19,Jacobsmouth>)

## To Sort the created users

- while still in the project folder in your terminal

- type the commnad 'python filter.py'

- a new csv file called user_sorted.csv will be created (Note that sorting is based on username)

- Output (id,FirstName,LastName,Username,Email,Avatar,Gender,Dob,Address

420,Arlena,Olson,arlena.olson,arlena.olson@email.com,<https://robohash.org/sintesseerror.png?size=300x300&set=set1,Genderfluid,2003-05-15,South> Kyle

7549,Cruz,Haag,cruz.haag,cruz.haag@email.com,<https://robohash.org/atqueaperiamexcepturi.png?size=300x300&set=set1,Genderqueer,1978-05-05,Corlissview>

4360,Dorsey,Labadie,dorsey.labadie,dorsey.labadie@email.com,<https://robohash.org/fugiatillonisi.png?size=300x300&set=set1,Genderfluid,2004-03-23,South> Kermitmouth

2833,Darnell,Borer,darnell.borer,darnell.borer@email.com,<https://robohash.org/voluptasfacilisnihil.png?size=300x300&set=set1,Female,1991-07-05,Prohaskaton>

4068,Kimberlee,Reinger,kimberlee.reinger,kimberlee.reinger@email.com,<https://robohash.org/repudiandaenemodeserunt.png?size=300x300&set=set1,Agender,1998-04-02,East> Roryside

9354,Karleen,Gutkowski,karleen.gutkowski,karleen.gutkowski@email.com,<https://robohash.org/quiarchitectoquod.png?size=300x300&set=set1,Polygender,2000-04-19,Jacobsmouth>

3339,Lawrence,Balistreri,lawrence.balistreri,lawrence.balistreri@email.com,<https://robohash.org/laudantiumoptiovero.png?size=300x300&set=set1,Genderfluid,2000-07-21,Emmerichview>

481,My,Mitchell,my.mitchell,my.mitchell@email.com,<https://robohash.org/omnissintaccusamus.png?size=300x300&set=set1,Non-binary,1978-06-20,New> Gusstad

1266,Pansy,Heaney,pansy.heaney,pansy.heaney@email.com,<https://robohash.org/blanditiisestcorporis.png?size=300x300&set=set1,Male,1961-08-24,Stefanland>

3007,Wallace,Lindgren,wallace.lindgren,wallace.lindgren@email.com,<https://robohash.org/estutsit.png?size=300x300&set=set1,Male,1982-08-29,Ashleymouth>)

## To find a User

- while still in the project folder in your terminal

- type the commnad 'python finduser.py'

- you'll be prompted to enter a user id

- Enter the user id and press enter

- The user with a matching id is displayed

- Example 
    - Enter id of user: 420
    - Output: ['420', 'Arlena', 'Olson', 'arlena.olson', 'arlena.olson@email.com', 'https://robohash.org/sintesseerror.png?size=300x300&set=set1', 'Genderfluid', '2003-05-15', 'South Kyle']
