window.onload = () => {
    if (localStorage.getItem('user_id')) {
        window.location.href = '/dash/';
    }
}
