const BASE = 'http://localhost:5000';

// Obtiene el saldo actual del servidor y lo muestra en pantalla
async function getSaldo() {
    const res = await fetch(`${BASE}/saldo`);
    const data = await res.json();
    document.getElementById('saldo').textContent = `Q${data.saldo.toFixed(2)}`;
}

// Lee los inputs del formulario y envía la apuesta al servidor
async function apostar() {
    const number = parseInt(document.getElementById('bet-number').value);
    const color  = document.getElementById('bet-color').value;
    const monto  = parseFloat(document.getElementById('bet-monto').value);
    const msg    = document.getElementById('bet-msg');

    // Limpia el mensaje anterior antes de hacer la petición
    msg.className = 'msg';
    msg.textContent = '';

    const res = await fetch(`${BASE}/apostar`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ number, color, monto })
    });

    const data = await res.json();

    // Actualiza saldo y lista de apuestas si la apuesta fue exitosa
    if (res.ok) {
        msg.className = 'msg ok';
        msg.textContent = 'Bet placed!';
        getSaldo();
        verApuestas();
    } else {
        msg.className = 'msg err';
        msg.textContent = data.error;
    }
}

// Solicita las apuestas activas al servidor y las renderiza en la lista
async function verApuestas() {
    const res  = await fetch(`${BASE}/ver_apuestas`);
    const data = await res.json();
    const list = document.getElementById('apuestas-list');

    if (data.apuestas.length === 0) {
        list.innerHTML = '<li class="empty">No bets yet.</li>';
        return;
    }

    // Genera un <li> por cada apuesta con su número, color y monto
    list.innerHTML = data.apuestas.map(a =>
        `<li><span>#${a.number} — ${a.color}</span><span>Q${a.monto}</span></li>`
    ).join('');
}

// Llama al endpoint /girar y muestra el número y color ganador
async function girar() {
    const btn     = document.getElementById('spin-btn');
    const numEl   = document.getElementById('result-number');
    const colorEl = document.getElementById('result-color');

    // Deshabilita el botón y muestra estado de carga
    btn.disabled = true;
    numEl.className = 'result-number';
    numEl.textContent = '...';
    colorEl.textContent = '';

    const res  = await fetch(`${BASE}/girar`, { method: 'POST' });
    const data = await res.json();

    if (res.ok) {
        // Aplica la clase del color para cambiar el color del número en pantalla
        numEl.textContent = data.numero_ganador;
        numEl.classList.add(data.color_ganador);
        colorEl.textContent = data.color_ganador;
        getSaldo();
        verApuestas();
    } else {
        numEl.textContent = '!';
        colorEl.textContent = data.apuestas;
    }

    btn.disabled = false;
}

// Reinicia el juego completo y resetea la pantalla al estado inicial
async function reiniciar() {
    await fetch(`${BASE}/reiniciar`, { method: 'POST' });
    document.getElementById('result-number').className = 'result-number';
    document.getElementById('result-number').textContent = '—';
    document.getElementById('result-color').textContent = '';
    getSaldo();
    verApuestas();
}

// Carga inicial: obtiene saldo y apuestas al abrir la página
getSaldo();
verApuestas();
