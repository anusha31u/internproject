document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');
    const searchResults = document.getElementById('searchResults');

    // Add an event listener to the search form
    searchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        // Create FormData object from the search form
        const formData = new FormData(searchForm);

        // Send a POST request to the search API endpoin
        fetch('/api/search/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Display search results
            renderResults(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Function to render search results
    function renderResults(results) {
        searchResults.innerHTML = '';
        if (results.length === 0) {
            searchResults.innerHTML = 'No results found.';
            return;
        }

        // Loop through results and display each one
        results.forEach(result => {
            const resultDiv = document.createElement('div');
            resultDiv.innerHTML = `<strong>${result.username}</strong>: ${result.sentence}`;
            searchResults.appendChild(resultDiv);
        });
    }
});
