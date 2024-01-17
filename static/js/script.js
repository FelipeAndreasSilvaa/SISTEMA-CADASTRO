function validarFormulario(){
    var nome = document.getElementById('nome').value;
    var email = document.getElementById('email').value;
    var senha = document.getElementById('senha').value;
    var senhaErrorMessage = document.getElementById('senha-error-message');
    var campomsg = document.getElementById('campo-error-message')


    if (nome === ''|| email === '' || senha === ''){
        campomsg.textContent = 'Preencha os campos corretamente'
        document.getElementById('nome').style.border = '1px solid red';
        document.getElementById('email').style.border = '1px solid red';
        document.getElementById('senha').style.border = '1px solid red';

        return false; // Impede o envio do formulário

    }

        if (senha.length < 6 || !/[A-Z]/.test(senha) || !/[!@#$%^&*(),.?":{}|<>]/.test(senha) || senha === nome) {
            senhaErrorMessage.textContent = 'A senha deve ter pelo menos 6 caracteres, incluindo pelo menos 1 letra maiúscula e 1 símbolo e a senha nao pode ter referencia com o nome';
            document.getElementById('senha').style.border = '1px solid red';
            return false; // Impede o envio do formulário
        }

        return true

}