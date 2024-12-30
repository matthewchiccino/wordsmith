// Get references to HTML elements
const wordInput = document.getElementById('wordInput'); // field where user types word
const submitButton = document.getElementById('submitButton'); // button
const messageBox = document.getElementById('messageBox');
const resultsContainer = document.getElementById('resultsContainer'); // main container

// Define the API endpoint (adjust this to your backend URL)
const apiUrl = 'http://127.0.0.1:8080/guess';

// Add event listener for the button
submitButton.addEventListener('click', () => {
    const word = wordInput.value.trim(); // Get the value from the input

    // Check if the input is not empty
    if (word) {
        // Make an API call to the backend
        fetch(apiUrl, {
            method: 'POST', // since im sending data
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
            const messageBox = document.getElementById('messageBox'); // Assuming you have a div with this ID
            messageBox.textContent = data.message; // Display the message from the response

            // Process the guesses (if any)
            if (data.data && data.data.length > 0) {
                data.data.forEach(item => {
                    const guessElement = document.createElement('div');
                    guessElement.classList.add('guess-item');
                    guessElement.innerHTML = `
                        <strong>Guess:</strong> ${item.guess} <br>
                        <strong>Score:</strong> ${(item.similarity)} <br><br>
                    `;
                    resultsContainer.appendChild(guessElement); // Append the results to the container
                });
            }
        })
        .catch(error => {
            console.error('Error:', error); // Handle any errors
            alert('There was an error with the API call');
        });
    } else {
        alert('Please enter a word');
    }
});
