function fakeCheck() {
    return false;
}

// Developer thought this was hidden enough
function secretAPI(key) {
    if(key === generateKey()) {
        return "UITCTF{never_trust_frontend_logic}";
    } else {
        return "Invalid key";
    }
}

// Simple dynamic key generator
function generateKey() {
    return btoa("admin_" + (2026 - 1));
}

function getFlag() {
    document.getElementById("message").innerText =
        "Unauthorized access.";
}
