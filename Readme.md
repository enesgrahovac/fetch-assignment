# I made a Loom video to help you set up this Docker image
https://www.loom.com/share/c338c35e250a404d8f8f32780614c67f

# 1. Change directory into this git repository

# 2. Turn on Docker on my computer
If you don't already have Docker installed, then please download it from Docker's official website.

# 3. Build the Docker image
If it's your first time doing this, then run 
`docker build -t fetch:latest .`

If you already have the fetch docker image built, then run this command to ensure the image is fresh
`docker image rm fetch && docker build -t fetch:latest . `

# 4. Run the Docker image
`docker run --rm -it -p 8888:8888 fetch:latest`

# 5. Run inference on your dataset
open the `Inference.ipynb` file and follow the specified instructions to test my model!