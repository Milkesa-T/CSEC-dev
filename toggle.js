const statusLabel = document.getElementById('statusLabel');
const toggleBtn = document.getElementById('toggleBtn');
let isOn = false;
toggleBtn.addEventListener('click', function() {
    isOn = !isOn;
    if (isOn) {
        statusLabel.textContent = "ON";
        statusLabel.style.color = "#27ae60"; 
    } else {
        statusLabel.textContent = "OFF";
        statusLabel.style.color = "#2c3e50";
    }
});
