function submitForm(event) {
    event.preventDefault();

    // Get form data
    const formData = {
        generatorDuty: document.getElementById('generatorDuty').value,
        pumpPressure: document.getElementById('pumpPressure').value,
        massFlowRate: document.getElementById('massFlowRate').value,
        chillerInTemp: document.getElementById('chillerInTemp').value
    };

    // Send data to the server
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Update results
            document.getElementById('outputTemp').textContent = data.result.outputTemp;
            document.getElementById('evaporatorDuty').textContent = data.result.evaporatorDuty;
            document.getElementById('generatorOutput').textContent = data.result.generatorOutput;
            document.getElementById('cop').textContent = data.result.cop;
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while processing the request.');
    });
}

// Attach event listener to the form
document.getElementById('chillerForm').addEventListener('submit', submitForm);