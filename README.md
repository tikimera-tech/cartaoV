# Cartão de visita web com QR Code

Este pacote contém um modelo simples de cartão de visita digital.

## Arquivos

- `index.html`: página do cartão de visita.
- `contato.vcf`: arquivo para a pessoa salvar seu contato no celular.
- `qr-code-exemplo.png`: QR Code de exemplo apontando para `https://seudominio.com/cartao`.
- `gerar_qrcode.py`: script para gerar um QR Code com a URL final do seu cartão.

## Como usar

1. Edite o arquivo `index.html` e troque:
   - Seu Nome
   - Cargo/profissão
   - Telefone/WhatsApp
   - E-mail
   - Instagram
   - Endereço
   - Texto de apresentação

2. Edite também o arquivo `contato.vcf` com os mesmos dados.

3. Publique a pasta em uma hospedagem estática, como Netlify, GitHub Pages, Vercel ou seu próprio servidor.

4. Depois que tiver a URL pública, gere o QR Code definitivo:
   ```bash
   python gerar_qrcode.py "https://sua-url-publica.com"
   ```

5. Use o arquivo `qr-code.png` em materiais impressos, adesivos, cartões físicos, placas, folders etc.

Importante: o QR Code precisa apontar para uma URL pública. Um arquivo local no computador não abrirá corretamente no celular de outras pessoas.
