window.onload = () => {
    if (!localStorage.getItem('user_id')) {
        window.location.href = '/';
    } else {
        var select = document.getElementById('doencas')
        if (select) {
            var ajax = new XMLHttpRequest();

            ajax.open("GET", "http://127.0.0.1:5000/disease/getAllDisease", true);

            ajax.onload = (e) => {
                var data = JSON.parse(ajax.responseText);
                if (ajax.readyState == 4 && ajax.status == 200) {
                    data.map(doenca => {
                        let option = document.createElement("option");
                        option.value = doenca
                        option.appendChild(document.createTextNode(doenca))
                        select.appendChild(option) 
                    })
                } else {
                    alert(`Não foi possível carregar as doênças: ${data.Erro}`)
                }
            }
        
            ajax.onerror = (e) => {
                console.error(ajax.statusText);
            }
        
            ajax.send();
        }
    }
}