// pede confirmacao antes de excluir
function confirmarExclusao(event) {
    if (!confirm("Tem certeza que deseja excluir este registro?")) {
        event.preventDefault();
    }
}

// filtra as linhas da tabela enquanto digita
function filtrarTabela() {
    var campo = document.getElementById("busca");
    if (!campo) {
        return;
    }
    campo.addEventListener("keyup", function () {
        var texto = campo.value.toLowerCase();
        var linhas = document.querySelectorAll("tbody tr");
        linhas.forEach(function (linha) {
            var achou = linha.textContent.toLowerCase().indexOf(texto) > -1;
            linha.style.display = achou ? "" : "none";
        });
    });
}

// matricula: sugere a data de termino (inicio + 1 mes)
function preencherTermino() {
    var inicio = document.getElementById("id_start_date");
    var fim = document.getElementById("id_end_date");
    if (!inicio || !fim) {
        return;
    }
    inicio.addEventListener("change", function () {
        if (!inicio.value || fim.value) {
            return;
        }
        var data = new Date(inicio.value + "T00:00:00");
        data.setMonth(data.getMonth() + 1);
        var ano = data.getFullYear();
        var mes = String(data.getMonth() + 1).padStart(2, "0");
        var dia = String(data.getDate()).padStart(2, "0");
        fim.value = ano + "-" + mes + "-" + dia;
    });
}

// pagamentos: pinta de verde os pagos e de vermelho os vencidos
function marcarPagamentos() {
    var agora = new Date();
    var hoje = agora.getFullYear() + "-" +
        String(agora.getMonth() + 1).padStart(2, "0") + "-" +
        String(agora.getDate()).padStart(2, "0");

    var linhas = document.querySelectorAll("tr[data-vencimento]");
    linhas.forEach(function (linha) {
        if (linha.dataset.pago === "1") {
            linha.classList.add("pago");
        } else if (linha.dataset.vencimento < hoje) {
            linha.classList.add("vencido");
        }
    });
}

// destaca no menu a pagina atual
// destaca no menu a pagina atual
function marcarMenu() {
    var links = document.querySelectorAll("a.menu-link");
    links.forEach(function (link) {
        var destino = link.getAttribute("href");
        if (destino && window.location.pathname.indexOf(destino) === 0) {
            link.classList.add("ativo");
        }
    });
}

document.addEventListener("DOMContentLoaded", function () {
    var excluir = document.querySelectorAll("a[href*='/excluir/']");
    excluir.forEach(function (link) {
        link.addEventListener("click", confirmarExclusao);
    });

    filtrarTabela();
    preencherTermino();
    marcarPagamentos();
    marcarMenu();
});