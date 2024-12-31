// Get references to HTML elements
const wordInput = document.getElementById('wordInput'); // Field where user types word
const submitButton = document.getElementById('submitButton'); // Button
const messageBox = document.getElementById('messageBox');
const resultsContainer = document.getElementById('resultsContainer'); // Main container

// Define the API endpoint (adjust this to your backend URL)
const apiUrl = 'http://127.0.0.1:8080/guess';

// Function to handle the word submission
function handleSubmit() {
    let word = wordInput.value.trim().toLowerCase(); // Get the value from the input and convert to lowercase

    // Check if the input is not empty
    if (word) {
        // Make an API call to the backend
        fetch(apiUrl, {
            method: 'POST', // Sending data
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ word: word }), // Send the word in the request body
        })
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
            console.log(data); // Handle the response data from the backend

            // Clear any previous results
            resultsContainer.innerHTML = '';

            // Display the message
            messageBox.textContent = data.message; // Display the message from the response

            // Process the guesses (if any)
            if (data.data && data.data.length > 0) {
                data.data.forEach(item => {
                    // Create a container for the guess and its progress bar
                    const guessElement = document.createElement('div');
                    guessElement.classList.add('guess-item');
                    guessElement.innerHTML = `
                        <strong>Guess:</strong> ${item.guess} <br>
                        <strong>Score:</strong> ${item.similarity}
                    `;

                    // Create the progress bar container and progress fill
                    const progressContainer = document.createElement('div');
                    progressContainer.classList.add('progress-bar');
                    const progressFill = document.createElement('div');
                    progressFill.classList.add('progress-fill');

                    progressContainer.appendChild(progressFill); // Insert fill into container
                    guessElement.appendChild(progressContainer); // Add the bar to the result
                    resultsContainer.appendChild(guessElement); // Add the whole result to the page

                    // Update the width of this specific progress bar
                    const decimal = Math.max(0, Math.min(1, item.similarity / 400000)); // Normalize similarity
                    // Apply logarithmic transformation to skew values (ensure it's between 0 and 1)
                    const skewedDecimal = Math.sqrt(decimal)  // More aggressive skewing for high values
                    progressFill.style.width = `${skewedDecimal * 100}%`;
                });
            }
        })
        .catch(error => {
            console.error('Error:', error); // Handle any errors
            alert('There was an error with the API call');
        });

        // Clear the textbox after submitting
        wordInput.value = '';
    } else {
        alert('Please enter a word');
    }
}

// Add event listener for the button
submitButton.addEventListener('click', handleSubmit);

// Add event listener for the Enter key to trigger the submit action
wordInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        handleSubmit(); // Trigger the submit button click when Enter is pressed
    }
});