# 1. Change Directory to the "~/ml-take-home-assignment/" directory
Run the `cd` command in your command line until you're working in this repository's base path.

# 2. If it doesnt already exist, create the Anaconda Environment
Run the following command in terminal to activate the conda environment
`conda create -f fetch.yml`

# 3. Activate the Anaconda Environment
Run the following command
`conda activate fetch`

# 4. Build the docker image

### If it's your first time building the image, then run this command:
`docker build -t fetch:latest .`

### If you've already build the fetch image, then run this command:
`docker image rm fetch && docker build -t fetch:latest .`

If you get this error `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`, then you likely need to turn on the Docker app on your machine. If you don't have the Docker app, then install it from their official website.

# 5. Check that the docker container exists under the name "fetch"
`docker image ls`

# 6. Run the Docker Container
`docker run --rm -it -p 8888:8888 fetch:latest`

# 7. The Inference Code is in the "Inference.ipynb" file.
Please double click the file name

# 8. To run inference, select the .CSV file you'd like to test the model against.
You will see a file selection box on the screen. Please select the file you'd like the program to load. Then, run the rest of the cells to see the model's results.

# 9. If you're confused in any steps, then please refer to the Loom video at the top of these directions
or email enes.resume@gmail.com


