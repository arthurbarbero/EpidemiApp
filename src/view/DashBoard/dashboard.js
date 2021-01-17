window.onload = () => {
    if (!localStorage.getItem('user_id')) {
        window.location.href = '/';
    }
}

function viewIncidences() {
    var selectedDisease = document.getElementById('doencas');

    if (!selectedDisease.value) {
        !selectedDisease.value ? selectedDisease.style.border = '2px solid red' : null;
        return null;
    }  

    window.location.href=`/incidence/view/${selectedDisease.value}`
}