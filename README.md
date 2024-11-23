# 🎵 Projeto Disciplina - Prática 5: Jingle Bells com Raspberry Pi

Este repositório contém os arquivos e scripts desenvolvidos para implementar um sistema que toca a música "Jingle Bells" em um buzzer enquanto LEDs piscam sincronizados. O projeto foi implementado utilizando a Raspberry Pi, Python e o controle de serviços via **systemd**, garantindo inicialização automática no boot.

## 📜 Visão Geral

O objetivo deste projeto foi explorar o controle de hardware da Raspberry Pi através do **Python**, implementar o controle de versão com **Git**, e configurar um serviço no **systemd** para gerenciar a execução dos scripts no sistema operacional. O sistema integra:
- Um **buzzer** para tocar a melodia de "Jingle Bells".
- Dois **LEDs** que piscam alternadamente, sincronizados com as notas musicais.

## 🛠️ Arquivos no Repositório

### 1️⃣ **Scripts**
- **`natalina.py`**:
  - Toca a música "Jingle Bells" utilizando o buzzer.
  - Controla dois LEDs que piscam sincronizados com as notas musicais.
  - O script utiliza a biblioteca `RPi.GPIO` para o controle dos GPIOs.

- **`parando.py`**:
  - Desliga os LEDs e o buzzer ao encerrar o serviço.
  - Garante a liberação adequada dos recursos GPIO.

### 2️⃣ **Serviço systemd**
- **`feliznatal.service`**:
  - Configura o serviço que inicia automaticamente os scripts no boot do sistema.
  - Inclui o `natalina.py` como serviço principal e o `parando.py` para finalizar o programa ao ser parado.

### 3️⃣ **Documentação**
- **`README.md`** (este arquivo):
  - Descrição completa do projeto, incluindo instruções de configuração e funcionamento.
  - Links para vídeos e imagens.

## 🔧 Configuração do Sistema

### Requisitos:
- Uma Raspberry Pi com sistema operacional baseado em Linux.
- Conexões de hardware para o buzzer e LEDs nos GPIOs especificados.
