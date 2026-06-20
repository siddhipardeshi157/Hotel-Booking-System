function validateContact() {

    let name = document.getElementById("cname").value.trim();
    let email = document.getElementById("cemail").value.trim();
    let subject = document.getElementById("subject").value.trim();
    let message = document.getElementById("message").value.trim();
    let error = document.getElementById("contactError");

    error.innerHTML = "";

    if (name === "") {
        error.innerHTML = "Please enter your name";
        error.style.color = "red";
        return;
    }

    if (email === "") {
        error.innerHTML = "Please enter your email";
        error.style.color = "red";
        return;
    }

    if (subject === "") {
        error.innerHTML = "Please enter subject";
        error.style.color = "red";
        return;
    }

    if (message === "") {
        error.innerHTML = "Please enter your message";
        error.style.color = "red";
        return;
    }

    error.innerHTML = "Message sent successfully!";
    error.style.color = "green";

    document.getElementById("contactForm").reset();
}
