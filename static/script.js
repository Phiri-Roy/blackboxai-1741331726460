document.getElementById('solve-button').addEventListener('click', function() {
    const puzzle = document.getElementById('puzzle').value;
    fetch('/solve', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ puzzle: puzzle })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('solution').innerText = JSON.stringify(data.solution);
    });
});
