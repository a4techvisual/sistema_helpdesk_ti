const maskPatrimonio = document.querySelector('#patrimonio');
const maskTel = document.querySelector('#telefone');

if (maskPatrimonio) {
    maskPatrimonio.addEventListener('input', function() {
        const numeros = this.value.replace(/\D/g, '').slice(0, 6);
        this.value = numeros ? 'PAT-' + numeros : '';
    });
}

if (maskTel) {
    maskTel.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '')
        .replace(/(\d{2})(\d)/, '($1) $2')
        .replace(/(\d{4,5})(\d)/, '$1-$2')
        .replace(/(\d{4})\d+?$/, '$1');
    });
}

// Contador de caracteres da descrição
const descricao = document.querySelector('#descricao');
const contador = document.querySelector('#contador-descricao');
if (descricao && contador) {
    const atualizar = () => contador.textContent = descricao.value.length + ' caracteres';
    descricao.addEventListener('input', atualizar);
    atualizar();
}
