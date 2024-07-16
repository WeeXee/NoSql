#!/bin/bash

# Pull the MongoDB Docker image
docker pull mongo:latest

# Run a MongoDB container using the image you just pulled
docker-compose up -d

# Wait for a few seconds to ensure that the container is up and running
sleep 10

# Verify that the container is running
docker ps

# Connect to the MongoDB container using the mongo shell and perform the required operations
docker exec -it mongodb_container mongosh <<EOF
  use Galaxies
  db.createCollection("Stars")
  db.Stars.insertMany([
    { Name: "Sirius", Type: "A1V", Distance: 8.6 },
    { Name: "Canopus", Type: "A9II", Distance: 310 },
    { Name: "Arcturus", Type: "K1.5III", Distance: 37 },
    { Name: "Vega", Type: "A0V", Distance: 25 },
    { Name: "Capella", Type: "G3III", Distance: 43 }
  ])
  db.Stars.find().pretty()
  db.createCollection("Planets")
  db.Planets.insertMany([
    { Name: "Mercury", Type: "Terrestrial", Distance: 0.39 },
    { Name: "Venus", Type: "Terrestrial", Distance: 0.72 },
    { Name: "Earth", Type: "Terrestrial", Distance: 1 },
    { Name: "Mars", Type: "Terrestrial", Distance: 1.52 },
    { Name: "Jupiter", Type: "Gas Giant", Distance: 5.2 }
  ])
  db.Stars.createIndex({ Name: 1 })
  db.Planets.createIndex({ Name: 1 })
  use admin
  db.shutdownServer()
EOF

# Create a backup of the Galaxies database
docker exec -it mongodb_container mongodump --db Galaxies --out /data/backup