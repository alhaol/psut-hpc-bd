# To build an Image and tag it
docker build -t alhaol/python3app . 

# Login to the docker hub
docker login 

# Push your images to the hub 
docker push alhaol/python3app

# Run a container to execute the app 
docker run alhaol/python3app



