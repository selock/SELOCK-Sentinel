# SELOCK-Sentinel: Sistema de Segurança Ativa para Dispositivos Móveis

## Visão Geral

O **SELOCK-Sentinel** é um sistema de segurança ativa desenvolvido pela SELOCK para proteger dispositivos móveis em cenários de risco extremo, onde a integridade dos dados e a privacidade do usuário podem ser comprometidas por coação física ou apreensão do aparelho. Complementando a segurança robusta do GrapheneOS, o Sentinel oferece camadas adicionais de proteção através de mecanismos de autodestruição de dados e monitoramento de hardware.

Este projeto é uma iniciativa da SELOCK para fortalecer a **Soberania Digital** de seus usuários, garantindo que o controle sobre as informações permaneça sempre nas mãos do proprietário do dispositivo, mesmo sob as condições mais adversas.

## Funcionalidades Principais

### 1. Dead-Man's Timer (Temporizador de Inatividade)

O Dead-Man's Timer é um mecanismo de segurança que monitora a atividade do usuário no dispositivo. Se o aparelho não for desbloqueado ou não houver interação por um período de tempo pré-definido e configurável, o sistema assume que o proprietário está incapacitado ou que o dispositivo foi comprometido. Em resposta, o Dead-Man's Timer executa um **"Data-Nuke"**, que pode incluir:

*   **Criptografia Adicional:** Aplicação de uma camada extra de criptografia a arquivos e diretórios sensíveis, tornando-os inacessíveis sem uma chave de recuperação específica.
*   **Deleção Segura:** Exclusão irrecuperável de dados críticos, garantindo que informações confidenciais não possam ser acessadas por terceiros.

O objetivo é assegurar que, em caso de perda de controle sobre o dispositivo, os dados sensíveis sejam protegidos contra acesso não autorizado, mesmo que isso signifique sua destruição.

### 2. USB-C Sentinel (Monitoramento de Porta USB-C)

O USB-C Sentinel é uma funcionalidade que monitora ativamente a porta USB-C do dispositivo. Em ambientes de alto risco, a conexão de dispositivos externos pode representar uma ameaça à segurança, permitindo a extração de dados ou a injeção de malware. O USB-C Sentinel atua da seguinte forma:

*   **Detecção de Dispositivos Desconhecidos:** Identifica quando um dispositivo USB-C não autorizado ou desconhecido é conectado ao celular enquanto ele está bloqueado.
*   **Corte de Comunicação Lógica:** Ao detectar uma ameaça, o Sentinel corta instantaneamente a comunicação lógica da porta USB-C, impedindo qualquer tentativa de extração de dados ou interação maliciosa com o hardware.

Esta funcionalidade adiciona uma camada de **Hardening dinâmico**, protegendo o dispositivo contra ataques físicos que tentam contornar as defesas do sistema operacional.

## Uso da Interface de Linha de Comando (CLI)

O `selock-admin.py` é a ferramenta central para gerenciar e configurar o SELOCK-Sentinel. Ele permite interagir com as funcionalidades do Dead-Man's Timer e do USB-C Sentinel.

### Comandos Gerais

```bash
python3 src/selock-admin.py --help
