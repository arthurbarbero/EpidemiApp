function logout() {
    localStorage.removeItem('user_id')
    window.location.href = '/';
}

function dash() {
    window.location.href = '/dash/';
}