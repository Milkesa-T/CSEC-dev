document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
       

        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const message = document.querySelector("textarea").value.trim();      
        if (name === "" || email === "" || message === "") {
            alert("Please fill in all fields.");
            return;
        }       
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            alert("Please enter a valid email address.");
            return;
        }     
        alert( name + " " + " submitted successfully.");    
        form.reset();
    });
});
