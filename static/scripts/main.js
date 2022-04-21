/* When the submit button is clicked, everything is hidden and a loading circle pops n the middle */
var submitButton = document.getElementById("sub");

submitButton.onclick = function onLoad() {
    var submitButton = document.getElementById("sub");
    submitButton.style.display = "none";
    var loading = document.getElementById("input-group");
    loading.style.display = "none";
    var clearButton = document.getElementById("clear");
    clearButton.style.display = "none";
    var loadingCircle = document.getElementById("loading-text");
    loadingCircle.style.display = "block";
}