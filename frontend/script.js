async function spin() {
    const btn = document.getElementById('spin-btn');
    const numEl = document.getElementById('result-number');
    const colorEl = document.getElementById('result-color');

    btn.disabled = true;
    numEl.className = 'result-number';
    numEl.textContent = '...';
    colorEl.textContent = '';

    try {
        const response = await fetch('http://localhost:5000/spin');
        const data = await response.json();

        numEl.textContent = data.number;
        numEl.classList.add(data.color);
        colorEl.textContent = data.color;
    } catch (error) {
        numEl.textContent = '!';
        colorEl.textContent = 'Server not connected';
    }

    btn.disabled = false;
}
