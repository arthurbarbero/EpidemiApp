function logout() {
    localStorage.removeItem('user_id')
    window.location.href = '/';
}