const colorInput = document.getElementById('colorInput');
const saveBtn = document.getElementById('saveBtn');

saveBtn.addEventListener('click', saveBtn);

localStorage.setItem('color', colorInput.value);


function saveBtn() {
    const color = colorInput.value;
    // Do something with the color value, e.g., change the background color of an element
}