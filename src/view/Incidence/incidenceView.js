window.onload = () => {
    if (!localStorage.getItem('user_id')) {
        window.location.href = '/';
    }

    var graphChart = document.getElementById('graph_chart').children
    if ( graphChart ) {
        let sum = 0
        for (let div of graphChart) {
            sum += parseInt(div.children[0].style.height.split('px')[0])
        }
        for (let div of graphChart) {
            div.children[0].style.height = `${(parseInt(div.children[0].style.height.split('px')[0])/sum)* 90}%`
        }
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