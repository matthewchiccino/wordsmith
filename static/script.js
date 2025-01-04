// Get references to HTML elements
const wordInput = document.getElementById('wordInput'); 
const submitButton = document.getElementById('submitButton'); 
const hintButton = document.getElementById('hintButton');
const messageBox = document.getElementById('messageBox');
const guessCountBox = document.getElementById('guessCountBox');
const recentScoreBox = document.getElementById('recentScoreBox');
const resultsContainer = document.getElementById('resultsContainer'); // Main container

// Define the API endpoint (adjust this to your backend URL)
const guessApiUrl = 'https://wordsmith-1.onrender.com//guess';
const hintApiUrl = 'https://wordsmith-1.onrender.com//hint';

// Function to handle the word submission
function handleSubmit() {
    const word = wordInput.value.trim().toLowerCase(); // Get the value from the input and convert to lowercase

    // Check if the input is not empty
    if (word) {
        // Make an API call to the backend
        fetch(guessApiUrl, {
            method: 'POST', // Sending data
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ word: word }), // Send the word in the request body
        })
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
            processApiResponse(data); // Pass the data to the processing function
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

function hint(){
    // Make an API call to the backend
    fetch(hintApiUrl, {
        method: 'GET', // Sending data
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
        processApiResponse(data); // Pass the data to the processing function
    })
    .catch(error => {
        console.error('Error:', error); // Handle any errors
        alert('There was an error with the API call');
    });
}

// Function to process the API response and update the UI
function processApiResponse(data) {
    // Clear any previous results
    resultsContainer.innerHTML = '';

    // Display the message and recent score
    messageBox.textContent = data.message;
    recentScoreBox.textContent = data.score;
    guessCountBox.textContent = `Guess count: ${data.data.length}`;;

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
            
            progressBar(item.similarity, progressFill); // Update the progress bar
        });
    }
}

// Function to calculate and update the progress bar
function progressBar(sim_score, progressFill) {
    // Calculate decimal using the formula
    const decimal = Math.pow(sim_score + 1, -0.0001 * sim_score);

    // Calculate the opposite (flip) of the decimal value since I shade in the grey area not the colored
    let decimal_flip = 1 - decimal;

    // Slightly modify so that bar is never super empty
    if (decimal_flip > 0.999) {
        decimal_flip -= 0.01; 
    } else if (decimal_flip > 0.99) {
        decimal_flip -= 0.02;
    }
    progressFill.style.width = `${decimal_flip * 100}%`; // Use the calculated decimal
}

// Add event listeners for buttons and input
submitButton.addEventListener('click', handleSubmit);
hintButton.addEventListener('click', hint); 

wordInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        handleSubmit(); // Trigger the submit button click when Enter is pressed
    }
});
