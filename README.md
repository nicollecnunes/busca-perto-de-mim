# Buscador
> Busca estabelecimentos próximos ao usuário, retornando-os com número de telefone e link direto para o Whatsapp.

## Vídeo demonstração
[![Vídeo Demonstração](https://github.com/nicollecnunes/busca-perto-de-mim/blob/main/thumb.png)](https://www.linkedin.com/posts/activity-6935232142893326336-QT9C?utm_source=linkedin_share&utm_medium=member_desktop_web)

## 🚀 Instalando as dependências

Para instalar as dependências, use:
```
pip install -r requirements.txt 
```

## ☕ Etapas de uso
Para executar: 
```
python main.py
```

1. Digite a sua API KEY do Google Places. Caso não possua uma, siga <a href="https://www.youtube.com/watch?v=pHhIICVcI6s">estes passos</a>

2. Digite o que você deseja buscar. Não é necessário digitar o nome da sua cidade.

```
O que você deseja buscar?
> Farmácias
```

3. (Opcional) Digite a mensagem que você deseja enviar para os estabelecimentos que possuírem o número cadastrado no Whatsapp. Caso não queira enviar uma mensagem, pressione a tecla enter.
```
Digite a mensagem que você quer enviar:
> Olá, qual o valor mínimo para a entrega?
```
4. Em alguns instantes, será gerada uma lista com os resultados, seus telefones de contato e os links diretos para o Whatsapp. (Não há verificação para saber se os telefones estão cadastrados, então pode ser que alguns links não funcionem)

```
Drogaria A
(99) 9999-9999
Link do whatsapp: wa.me/999999999999?text=Olá,%20qual%20o%20valor%20mínimo%20para%20a%20entrega?
-------------------------------------------------------------------------------------------------------
Drogamed B
(99) 9999-9999
Link do whatsapp: wa.me/999999999999?text=Olá,%20qual%20o%20valor%20mínimo%20para%20a%20entrega?
-------------------------------------------------------------------------------------------------------
Farmácia C
(99) 9999-9999
Link do whatsapp: wa.me/999999999999?text=Olá,%20qual%20o%20valor%20mínimo%20para%20a%20entrega?
-------------------------------------------------------------------------------------------------------
```

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
