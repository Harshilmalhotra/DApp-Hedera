# # Set the base image
FROM node:16-alpine

# Set the working directory in the container
WORKDIR /code

# Copy the npm packages
COPY package.json .
COPY package-lock.json .

# Install dependencies
RUN npm install

# Copy the project across
COPY . .

# Build the SvelteKit app
RUN npm run build

# Start the app when the container is launched
CMD [ "npm", "run", "preview" ]
