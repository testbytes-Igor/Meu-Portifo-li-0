const texts = [
  "Estudante de Engenharia de Software",
  "Apaixonado por boas práticas",
  "Explorando Inteligência Artificial",
  "Amante de tecnologia e open source"
];

let index = 0;
let charIndex = 0;
let element = document.querySelector(".typing");

function type() {
  if (charIndex < texts[index].length) {
    element.textContent += texts[index].charAt(charIndex);
    charIndex++;
    setTimeout(type, 60);
  } else {
    setTimeout(erase, 1500);
  }
}

function erase() {
  if (charIndex > 0) {
    element.textContent = texts[index].substring(0, charIndex - 1);
    charIndex--;
    setTimeout(erase, 40);
  } else {
    index = (index + 1) % texts.length;
    setTimeout(type, 400);
  }
}

document.addEventListener("DOMContentLoaded", type);
