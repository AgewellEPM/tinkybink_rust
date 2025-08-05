#!/bin/bash

# Test the TinkyBink AAC demo with some example inputs

echo "Testing TinkyBink AAC conversational predictions..."
echo ""

# Use expect or a here document to provide input
(
echo "Let's go to the park"
sleep 0.5
echo "1"
sleep 0.5
echo "cookie or milk?"
sleep 0.5
echo "2"
sleep 0.5
echo "Time for bed"
sleep 0.5
echo "1"
sleep 0.5
echo "quit"
) | $HOME/.cargo/bin/cargo run demo