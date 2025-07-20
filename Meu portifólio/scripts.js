const btnAlert = document.getElementById('btnAlert');
const btnChangeText = document.getElementById('btnChangeText');
const btnToggle = document.getElementById('btnToggle');
const messageDiv = document.getElementById('message');

btnAlert.addEventListener('click', () => {
  alert('Você clicou no botão de alerta!');
});

btnChangeText.addEventListener('click', () => {
  // Muda o texto do botão btnChangeText a cada clique
  if (btnChangeText.textContent === 'Clique para Mudar Texto') {
    btnChangeText.textContent = 'Texto Alterado! Clique Novamente';
  } else {
    btnChangeText.textContent = 'Clique para Mudar Texto';
  }
});

btnToggle.addEventListener('click', () => {
  // Alterna a visibilidade da mensagem
  if (messageDiv.style.display === 'none') {
    messageDiv.style.display = 'block';
  } else {
    messageDiv.style.display = 'none';
  }
});
