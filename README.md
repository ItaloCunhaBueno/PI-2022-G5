# Projeto Integrador UNIVESP Turma 2022 Grupo 05

## Requerimentos

É necessário instalar o banco de dados [PostgreSQL](https://www.postgresql.org/download/) e configurar um arquivo .env na mesma pasta do script de entrada do backend `api/.env` da seguinte forma:

```toml
HOST=127.0.0.1
PORT=5432
USER=postgres
PASS=123
DB=postgres
CONNECTIONSTRING=postgresql+psycopg://${USER}:${PASS}@${HOST}:${PORT}/${DB}
```

Altere esses dados de acordo com sua instalação.

## Desenvolvimento

### Front-end:

Clone este repositório e inicialize com `npm install` (ou `pnpm install` ou `yarn`), inicie o servidor com:

```bash
npm run dev

# ou inicie o servidor e abra a pagina no navegador com:
npm run dev -- --open
```

Para compilar a versão de produção, execute:

```bash
npm run build
```

Você pode visualizar a versão de produção com `npm run preview`.

### Back-end:

É recomendado criar um ambiente virtual na pasta api para instalar as bibliotecas requisitos:

```bash
cd api
python -m virtualenv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

Após isso, basta iniciar o servidor com:

```bash
python app.py
```
