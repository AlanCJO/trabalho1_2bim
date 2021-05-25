const inputs = document.querySelectorAll('p input');
const selects = document.querySelectorAll('select')
const textarea = document.querySelector('textarea')

inputs.forEach(input => input.classList.add("form-control"));
selects.forEach(select => select.classList.add("form-control"));

textarea.classList.add("form-control")
textarea.setAttribute("rows", "5")
textarea.style.resize = 'none'
