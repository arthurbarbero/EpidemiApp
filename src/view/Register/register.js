window.onload = () => {
    if (localStorage.getItem('user_id')) {
        window.location.href = '/dash/';
    }
}

function sendRegister() {
    var name = document.getElementById('name');
    var email = document.getElementById('email');
    var password =  document.getElementById('password');

    if (!email.value || !password.value || !name.value) {
        !email.value ? email.style.border = '2px solid red' : null;
        !password.value ? password.style.border = '2px solid red' : null;
        !name.value ? name.style.border = '2px solid red' : null;
        return null;
    }  

    let obj = { 
        name: name.value,
        email: email.value,
        password: password.value
    }

    var ajax = new XMLHttpRequest();

    // Pega o tipo de requisição: Post e a URL da API
    ajax.open("POST", "http://127.0.0.1:5000/account/registerUser", true);
    ajax.setRequestHeader("Content-type", "application/json");

    ajax.onload = (e) => {
        var data = JSON.parse(ajax.responseText);
        if (ajax.readyState == 4 && ajax.status == 200) {
            localStorage.setItem('user_id', data.id);
            window.location.href = '/dash/';
        } else {
            alert(`Tente novamente: ${data.Erro}`)
        }
    }

    ajax.onerror = (e) => {
        console.error(ajax.statusText);
    }

    ajax.send(JSON.stringify(obj));

}
