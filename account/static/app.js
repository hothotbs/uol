const showPass = document.getElementById("pass-label")
const passInput = document.getElementById('password')

showPass.addEventListener('click', () => {

  if (passInput.type == 'password') {
    showPass.innerText = 'esconder'
    passInput.setAttribute('type', 'text')
  } else {
    passInput.setAttribute('type', 'password')
    showPass.innerText = 'monstrar'

  }
})