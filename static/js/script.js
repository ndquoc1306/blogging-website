function openModal(username) {
    var modal = document.getElementById("myModal-" + username);
    modal.style.display = "block";
}

function closeModal(username) {
    var modal = document.getElementById("myModal-" + username);
    modal.style.display = "none";
}