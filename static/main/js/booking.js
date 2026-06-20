function validateBooking() {
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let phone = document.getElementById("phone").value.trim();
    let checkin = document.getElementById("checkin").value;
    let checkout = document.getElementById("checkout").value;

    if (name === "" || email === "" || phone === "" || checkin === "" || checkout === "") {
        alert("❌ Please fill all fields");
        return false;
    }

    if (phone.length !== 10 || isNaN(phone)) {
        alert("❌ Enter valid 10-digit phone number");
        return false;
    }

    if (checkout <= checkin) {
        alert("❌ Check-out date must be after check-in date");
        return false;
    }

    return true; // ✅ allow submit
}
