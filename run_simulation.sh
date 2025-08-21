#!/bin/bash

# Stroke victim simulation for Tinkybink AAC
echo "🏥 Starting Stroke Victim Communication Simulation"
echo "Patient: 68-year-old stroke survivor with aphasia"
echo "================================================"
echo

# Run in headless mode with simulated inputs
echo "Caregiver: How are you feeling today?" | ./target/release/tinkybink_rust --headless 2>&1 | grep -A5 "Suggestions"

sleep 2

echo "Caregiver: Are you in pain?" | ./target/release/tinkybink_rust --headless 2>&1 | grep -A5 "Suggestions"

sleep 2

echo "Caregiver: Do you need water?" | ./target/release/tinkybink_rust --headless 2>&1 | grep -A5 "Suggestions"

sleep 2

echo "Caregiver: Want to see your family?" | ./target/release/tinkybink_rust --headless 2>&1 | grep -A5 "Suggestions"