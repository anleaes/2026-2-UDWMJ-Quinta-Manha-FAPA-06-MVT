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
    marcarPagamentos();
    marcarMenu();
});