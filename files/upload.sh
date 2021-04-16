#!/bin/bash

# My first script

for entry in "/home/ubuntu/Software-Project-Back-End-COMP308/files"/*
do
  curl -XPOST 'https://search-software-project-pn6qjbc5x2vzyxwdvgsipf6ava.ca-central-1.es.amazonaws.com//_bulk' --data-binary @"$entry" -H 'Content-Type: application/json'
  echo "$entry"
done
