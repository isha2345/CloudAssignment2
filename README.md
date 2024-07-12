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
 - Step five: Dockerfile.test consists of tests for the API.
   - To build the docker image, run the following command:
     
     ```
     docker build -f Dockerfile.test -t rest-api-app-test .
     ```
   - To run the docker image, run the following command:
     
     ```
     docker run --rm rest-api-app-test
     ```

