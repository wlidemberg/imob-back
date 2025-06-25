document.addEventListener("DOMContentLoaded", function () {
    const tipoField = document.getElementById("id_tipo");

    function toggleCampos() {
        const tipo = tipoField.value;

        const cpf = document.querySelector(".form-row.field-cpf");
        const identidade = document.querySelector(".form-row.field-identidade");
        const nome_fantasia = document.querySelector('.form-row.field-nome_fantasia')
        const cnpj = document.querySelector(".form-row.field-cnpj");
        const ie = document.querySelector(".form-row.field-inscricao_estadual");

        if (tipo === "F") {
            cpf.style.display = "block";
            identidade.style.display = "block";
            nome_fantasia.style.display = "none";
            cnpj.style.display = "none";
            ie.style.display = "none";
        } else if (tipo === "J") {
            cpf.style.display = "none";
            identidade.style.display = "none";
            nome_fantasia.style.display = "block";
            cnpj.style.display = "block";
            ie.style.display = "block";
        }
    }

    tipoField.addEventListener("change", toggleCampos);
    toggleCampos(); // Executa na primeira carga
});
