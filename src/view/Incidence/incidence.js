window.onload = () => {
    if (!localStorage.getItem('user_id')) {
        window.location.href = '/';
    }
}

function sendIncidence() {
    var selectedDisease = document.getElementById('doencas');
    var incidenceDate = document.getElementById('incidence-date');

    if (!selectedDisease.value || !incidenceDate.value) {
        !selectedDisease.value ? selectedDisease.style.border = '2px solid red' : null;
        !incidenceDate.value ? incidenceDate.style.border = '2px solid red' : null;
        return null;
    }  

    let obj = { 
        user_id: localStorage.getItem('user_id'),
        selectedDisease: selectedDisease.value,
        incidenceDate: incidenceDate.value,
    }

    var ajax = new XMLHttpRequest();

    // Pega o tipo de requisição: Post e a URL da API
    ajax.open("POST", "http://127.0.0.1:5000/incidence/register", true);
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