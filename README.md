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
Dead-Man's Timer (DMT)•Configurar:python3 src/selock-admin.py dmt config --threshold <segundos> --nuke-command "<comando_shell>"Exemplo: python3 src/selock-admin.py dmt config --threshold 7200 --nuke-command "shred -zuf /data/data/com.example.app/files/sensitive_data.txt"•Atualizar Interação:python3 src/selock-admin.py dmt update-interaction•Verificar Status:python3 src/selock-admin.py dmt status•Executar Checagem Manual:python3 src/selock-admin.py dmt run-checkUSB-C Sentinel (USB)•Configurar Ação:python3 src/selock-admin.py usb config --action "<comando_shell>"Exemplo: python3 src/selock-admin.py usb config --action "echo 0 > /sys/class/typec/port0/usb_data_enabled" (Este comando é um exemplo e pode variar dependendo do hardware e kernel).•Simular Status do Telefone:python3 src/selock-admin.py usb simulate-locked --status [locked|unlocked]•Simular Status de Conexão USB:python3 src/selock-admin.py usb simulate-usb --status [connected|disconnected]•Verificar Status:python3 src/selock-admin.py usb status•Executar Checagem Manual:python3 src/selock-admin.py usb run-checkAutomação com CrontabPara garantir que o SELOCK-Sentinel opere de forma contínua em segundo plano, é recomendável configurá-lo para ser executado periodicamente via crontab.Instalação1.Tornar o script de administração executável:chmod +x src/selock-admin.py2.Executar o script de configuração do Crontab:./setup-crontab.shEste script adicionará duas entradas ao crontab do usuário atual, que executarão as checagens do Dead-Man's Timer e do USB-C Sentinel a cada 5 minutos. Os logs serão direcionados para selock_sentinel.log no diretório raiz do projeto.VerificaçãoPara verificar se os jobs foram adicionados corretamente ao crontab:crontab -lAtribuição e LicençaEste projeto é desenvolvido e mantido pela SELOCK. Visite nosso site para mais informações sobre nossas soluções em segurança e privacidade: https://www.selock.netEste projeto é licenciado sob a Licença MIT.
