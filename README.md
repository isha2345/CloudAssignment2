# Instructions
 - Step one: Clone the repository.
 - Step two: For running the flask app, run the following command:
   
   ```
   python server.py
   ```
 - Step three: For running the flask app, run the following command:

   ```
   python tests_server.py
   ```
 - Step four: Dockerfile is used for running the API.
   - To build the docker image, run the following command:
     ```
     docker build -t rest-api-app .
     ```
   - To run the docker image, run the following command:
     ```
     docker run -p 5000:5000 rest-api-app
     ```
 

