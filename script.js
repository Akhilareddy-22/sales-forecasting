// ================= CONFIG =================
const API_URL = "http://127.0.0.1:8000/predict";
let chart = null;

// ================= FUNCTION =================
function predictSales() {
    const daysInput = document.getElementById("days");
    const status = document.getElementById("status");
    const days = parseInt(daysInput.value);

    // Reset status
    status.className = "status";
    status.innerText = "";

    // Validation
    if (!days || days <= 0) {
        status.classList.add("error");
        status.innerText = "Please enter a valid number.";
        return;
    }

    status.classList.add("loading");
    status.innerText = "Predicting sales... Please wait.";

    // API Call
    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            months: days   // backend expects "months"
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Backend error");
        }
        return response.json();
    })
    .then(data => {
        status.innerText = "";

        const sales = data.predictions;

        // Labels
        const labels = sales.map((_, i) => `Day ${i + 1}`);

        // Update sales list
        const list = document.getElementById("salesList");
        list.innerHTML = "";

        sales.forEach((value, index) => {
            const li = document.createElement("li");
            li.innerText = `Day ${index + 1}: ${value.toFixed(2)}`;
            list.appendChild(li);
        });

        // Destroy old chart
        if (chart) {
            chart.destroy();
        }

        // Create new chart
        const ctx = document.getElementById("salesChart").getContext("2d");
        chart = new Chart(ctx, {
            type: "line",
            data: {
                labels: labels,
                datasets: [{
                    label: "Predicted Sales",
                    data: sales,
                    borderColor: "#3498db",
                    backgroundColor: "rgba(52, 152, 219, 0.2)",
                    fill: true,
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: false
                    }
                }
            }
        });
    })
    .catch(error => {
        console.error("Error:", error);
        status.classList.add("error");
        status.innerText = "Error connecting to backend API.";
    });
}
