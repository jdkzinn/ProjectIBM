# 🐍 Desafio de Programação — Microserviços em Python (FastAPI)
## Banco JAVER – Cadastro de Clientes (com SQLite3)

Bem-vindos, desenvolvedores intrépidos, ao nosso desafio de programação! Preparem-se para uma jornada emocionante onde vocês irão explorar os confins do Python com FastAPI, criar microserviços interconectados e levá-los para a nuvem!

---

## 🔨 Missão

Criar duas aplicações em Python (FastAPI), cada uma desempenhando um papel crucial em nosso ecossistema de microsserviços.

---

## 📘 TEMA: Cadastro de Clientes do Banco JAVER

Informações do cliente (Para CRUD):
- **nome** (String)
- **telefone** (Long/int)
- **correntista** (Boolean)
- **score_credito** (Float)
- **saldo_cc** (Float) - **⚠️ IMPORTANTE: O saldo da conta não pode ser negativo (deve ser 0 ou maior)**

---

## 🧱 Arquitetura dos Microserviços

### 🟦 1) Primeira Aplicação: Gateway Service

Esta aplicação será nossa ponte para a segunda aplicação. Ela deve realizar requisições REST para a segunda aplicação.

**Responsabilidades:**

- Expor os quatro endpoints CRUD (Create, Read, Update, Delete):
  - POST /customers
  - GET /customers
  - GET /customers/{id}
  - PUT /customers/{id}
  - DELETE /customers/{id}

- Realizar chamadas REST para o Storage Service

- Implementar um endpoint adicional que realizará um cálculo simples de score de crédito:
  
  ### 👉 GET /customers/{id}/score
  
  Este endpoint:
  - Consulta o cliente no Storage Service
  - Obtém o saldo_cc da base de dados
  - Calcula: `score_calculado = saldo_cc * 0.1`
  - Retorna o valor calculado

O Gateway atua como um intermediário inteligente, agregando informações e executando regras adicionais.

---

### 🟩 2) Segunda Aplicação: Storage Service

Esta aplicação é o coração do nosso sistema de armazenamento. Ela será responsável por realizar operações CRUD em uma base de dados local SQLite3.

**Responsabilidades:**

- Conectar-se ao SQLite3
- Criar e gerenciar tabelas via SQLAlchemy
- Implementar CRUD completo de clientes
- Aplicar regras de negócio, incluindo:
  - **saldo_cc >= 0** (não pode ser negativo)
    - Validado no Pydantic (schemas)
    - Validado no SQLite3 via CheckConstraint

O banco utilizado neste projeto é SQLite3, configurado automaticamente pelo SQLAlchemy.

---

## 🧪 Requisitos de Testes

Ambas as aplicações devem possuir **100% de cobertura de testes unitários**. Garantir que suas implementações estejam robustamente testadas para garantir a qualidade e a confiabilidade do código.

### Testes do Storage Service:
- Criar cliente
- Buscar cliente
- Listar clientes
- Atualizar cliente
- Remover cliente
- Validar que saldo_cc não pode ser negativo
- Testar constraints no banco

### Testes do Gateway:
- Testar endpoints CRUD chamando o Storage
- Mockar chamadas REST com httpx + ASGITransport
- Testar cálculo do score
- Testar erros (cliente inexistente, saldo inválido, etc.)

---

## ⭐ Desafio Extra (Opcional)

Para os bravos que desejam ir além, o desafio extra aguarda! Você pode hospedar ambas as aplicações em instâncias EC2 do tipo t2.micro na AWS e expor seus endpoints publicamente na nuvem. Além disso, a base de dados pode residir em um RDS gratuito. Desafie-se a explorar os limites da computação em nuvem!

Este passo é opcional; o seu projeto usa SQLite3 local.

---

## 📚 O que deve estar documentado

Lembre-se de documentar adequadamente suas implementações, fornecendo instruções claras sobre:

- Como instalar dependências
- Como configurar o SQLite3
- Como executar o Storage e o Gateway
- Como rodar os testes
- Como acessar os endpoints via Swagger
- Arquitetura e fluxo dos microserviços

---

## 🎤 Apresentação Final

Ao final da trilha, cada um deverá apresentar o que foi desenvolvido! Portanto treine no espelho sua apresentação.

Ao concluir o desafio, você deve apresentar:

- Arquitetura dos serviços
- Funcionamento de Gateway e Storage
- Demonstração de todos os endpoints
- Testes unitários e cobertura
- Regras de negócio aplicadas (especialmente saldo_cc >= 0)
- Aprendizados técnicos

---

## 🏆 Premiação

Além da satisfação pessoal de conquistar este desafio, os participantes terão a oportunidade de aprimorar suas habilidades em:

- Desenvolvimento de microserviços reais
- APIs REST modernas com FastAPI
- SQLite3 integrado com SQLAlchemy
- Testes unitários robustos
- Arquitetura modular e profissional
- Comunicação entre serviços via REST

Esse conhecimento é utilizado diariamente em empresas como IBM, Itaú, Santander, XP, Banco Inter, PagBank e muitas outras.

---

## 🚀 Boa sorte, programadores!

Então, estão prontos para embarcar nesta jornada desafiadora? Que os códigos estejam a seu favor e que a nuvem seja sua aliada nesta aventura! 

Que seus microserviços se comuniquem com harmonia, que seus testes passem e que seu código brilhe na apresentação! 🔥🐍⚡

---