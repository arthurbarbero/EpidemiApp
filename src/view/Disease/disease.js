window.onload = () => {
    if (!localStorage.getItem('user_id')) {
        window.location.href = '/';
    }
}

function sendDisease() {
    var doencaName = document.getElementById('doenca-name');
    var doencaDescription = document.getElementById('doenca-description');

    if (!doencaName.value || !doencaDescription.value) {
        !doencaName.value ? doencaName.style.border = '2px solid red' : null;
        !doencaDescription.value ? doencaDescription.style.border = '2px solid red' : null;
        return null;
    }  

    let obj = { 
        name: doencaName.value,
        symptoms: doencaDescription.value,
    }

    var ajax = new XMLHttpRequest();

    // Pega o tipo de requisição: Post e a URL da API
    ajax.open("POST", "http://127.0.0.1:5000/disease/register", true);
    ajax.setRequestHeader("Content-type", "application/json");

    ajax.onload = (e) => {
        var data = JSON.parse(ajax.responseText);
        if (ajax.readyState == 4 && ajax.status == 200) {
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