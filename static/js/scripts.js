// Highlights current date on contact page
window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    listHoursArray[new Date().getDay()].classList.add(('today'));
})

// Function controls messages's display
setTimeout(function () {
    let messages = document.getElementById('messages');
    if (messages) {
        messages.style.display = "none";
    }
}, 2500);

