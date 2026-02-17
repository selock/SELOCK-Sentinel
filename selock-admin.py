
import argparse
import json
import os
import sys
import time

# Caminhos para os arquivos de configuração e status
BASE_DIR = os.path.join(os.path.dirname(__file__), '..')

DEAD_MANS_TIMER_CONFIG_FILE = os.path.join(BASE_DIR, 'config', 'dead_mans_timer_config.json')
LAST_INTERACTION_FILE = os.path.join(BASE_DIR, 'config', 'last_interaction.txt')

USB_C_SENTINEL_CONFIG_FILE = os.path.join(BASE_DIR, 'config', 'usb_c_sentinel_config.json')
PHONE_LOCKED_STATUS_FILE = os.path.join(BASE_DIR, 'config', 'phone_locked_status.txt')
USB_DEVICE_STATUS_FILE = os.path.join(BASE_DIR, 'config', 'usb_device_status.txt')

# --- Funções de utilidade para Dead-Man's Timer ---

def load_dead_mans_timer_config():
    if not os.path.exists(DEAD_MANS_TIMER_CONFIG_FILE):
        return {
            "inactivity_threshold_seconds": 3600, # 1 hour
            "data_nuke_command": "echo 'Simulando Data-Nuke: Dados críticos criptografados/deletados!' > /tmp/data_nuke_log.txt"
        }
    with open(DEAD_MANS_TIMER_CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_dead_mans_timer_config(config):
    with open(DEAD_MANS_TIMER_CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def update_last_interaction():
    with open(LAST_INTERACTION_FILE, 'w') as f:
        f.write(str(int(time.time())))
    print("Última interação para Dead-Man's Timer atualizada.")

def get_dead_mans_timer_status():
    config = load_dead_mans_timer_config()
    inactivity_threshold = config["inactivity_threshold_seconds"]
    data_nuke_command = config["data_nuke_command"]

    last_interaction_time = 0
    if os.path.exists(LAST_INTERACTION_FILE):
        with open(LAST_INTERACTION_FILE, 'r') as f:
            try:
                last_interaction_time = int(f.read())
            except ValueError:
                pass # Handle empty or invalid file

    current_time = int(time.time())
    time_since_last_interaction = current_time - last_interaction_time

    status = {
        "inactivity_threshold_seconds": inactivity_threshold,
        "data_nuke_command": data_nuke_command,
        "last_interaction_timestamp": last_interaction_time,
        "time_since_last_interaction_seconds": time_since_last_interaction,
        "status": "Ativo" if time_since_last_interaction < inactivity_threshold else "Inativo (pronto para Data-Nuke)"
    }
    return status

# --- Funções de utilidade para USB-C Sentinel ---

def load_usb_c_sentinel_config():
    if not os.path.exists(USB_C_SENTINEL_CONFIG_FILE):
        return {
            "unauthorized_device_action": "echo 'Simulando corte de comunicação USB-C: Dispositivo não autorizado detectado!' > /tmp/usb_c_sentinel_log.txt"
        }
    with open(USB_C_SENTINEL_CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_usb_c_sentinel_config(config):
    with open(USB_C_SENTINEL_CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def set_phone_locked_status(locked=True):
    with open(PHONE_LOCKED_STATUS_FILE, 'w') as f:
        f.write('locked' if locked else 'unlocked')
    print(f"Status do telefone: {'bloqueado' if locked else 'desbloqueado'}")

def set_usb_device_status(connected=True):
    with open(USB_DEVICE_STATUS_FILE, 'w') as f:
        f.write('connected' if connected else 'disconnected')
    print(f"Status do dispositivo USB: {'conectado' if connected else 'desconectado'}")

def get_usb_c_sentinel_status():
    config = load_usb_c_sentinel_config()
    unauthorized_device_action = config["unauthorized_device_action"]

    phone_locked = False
    if os.path.exists(PHONE_LOCKED_STATUS_FILE):
        with open(PHONE_LOCKED_STATUS_FILE, 'r') as f:
            phone_locked = (f.read().strip() == 'locked')

    usb_connected = False
    if os.path.exists(USB_DEVICE_STATUS_FILE):
        with open(USB_DEVICE_STATUS_FILE, 'r') as f:
            usb_connected = (f.read().strip() == 'connected')

    status = {
        "unauthorized_device_action": unauthorized_device_action,
        "phone_locked": phone_locked,
        "usb_connected": usb_connected,
        "threat_detected": phone_locked and usb_connected
    }
    return status

# --- Funções de execução dos módulos ---

def run_dead_mans_timer_check():
    # Importa e executa a função de checagem do Dead-Man's Timer
    # Nota: Em um ambiente real, você importaria o módulo diretamente.
    # Aqui, para simplificar a demonstração, estamos re-implementando a lógica.
    config = load_dead_mans_timer_config()
    inactivity_threshold = config["inactivity_threshold_seconds"]
    data_nuke_command = config["data_nuke_command"]

    last_interaction_time = 0
    if os.path.exists(LAST_INTERACTION_FILE):
        with open(LAST_INTERACTION_FILE, 'r') as f:
            try:
                last_interaction_time = int(f.read())
            except ValueError:
                pass

    current_time = int(time.time())
    if (current_time - last_interaction_time) > inactivity_threshold:
        print(f"[Dead-Man's Timer] Inatividade detectada por mais de {inactivity_threshold} segundos. Executando Data-Nuke...")
        os.system(data_nuke_command)
        print("[Dead-Man's Timer] Data-Nuke executado. Resetando temporizador.")
        update_last_interaction()
    else:
        print(f"[Dead-Man's Timer] Atividade recente detectada. Próxima verificação em {inactivity_threshold - (current_time - last_interaction_time)} segundos.")

def run_usb_c_sentinel_check():
    # Importa e executa a função de checagem do USB-C Sentinel
    # Nota: Em um ambiente real, você importaria o módulo diretamente.
    # Aqui, para simplificar a demonstração, estamos re-implementando a lógica.
    config = load_usb_c_sentinel_config()
    unauthorized_device_action = config["unauthorized_device_action"]

    phone_locked = False
    if os.path.exists(PHONE_LOCKED_STATUS_FILE):
        with open(PHONE_LOCKED_STATUS_FILE, 'r') as f:
            phone_locked = (f.read().strip() == 'locked')

    usb_connected = False
    if os.path.exists(USB_DEVICE_STATUS_FILE):
        with open(USB_DEVICE_STATUS_FILE, 'r') as f:
            usb_connected = (f.read().strip() == 'connected')

    if phone_locked and usb_connected:
        print("[USB-C Sentinel] Ameaça USB-C detectada: Telefone bloqueado e dispositivo USB conectado. Executando ação...")
        os.system(unauthorized_device_action)
        print("[USB-C Sentinel] Ação de corte de comunicação USB-C executada.")
        # set_usb_device_status(connected=False) # Não resetamos o status aqui, o sistema real faria isso
    else:
        print("[USB-C Sentinel] Nenhuma ameaça USB-C detectada.")

# --- CLI Principal ---

def main():
    parser = argparse.ArgumentParser(description="SELOCK-Sentinel: Ferramenta de administração para Dead-Man's Timer e USB-C Sentinel.")
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponíveis')

    # Subparser para Dead-Man's Timer
    dmt_parser = subparsers.add_parser('dmt', help='Gerenciar Dead-Man\'s Timer')
    dmt_subparsers = dmt_parser.add_subparsers(dest='dmt_command', help='Comandos do Dead-Man\'s Timer')

    # dmt config
    dmt_config_parser = dmt_subparsers.add_parser('config', help='Configurar Dead-Man\'s Timer')
    dmt_config_parser.add_argument('--threshold', type=int, help='Tempo de inatividade em segundos para o Data-Nuke.')
    dmt_config_parser.add_argument('--nuke-command', type=str, help='Comando a ser executado para o Data-Nuke.')

    # dmt update-interaction
    dmt_subparsers.add_parser('update-interaction', help='Atualizar o timestamp da última interação.')

    # dmt status
    dmt_subparsers.add_parser('status', help='Mostrar status do Dead-Man\'s Timer.')

    # dmt run-check
    dmt_subparsers.add_parser('run-check', help='Executar uma checagem manual do Dead-Man\'s Timer.')

    # Subparser para USB-C Sentinel
    usb_parser = subparsers.add_parser('usb', help='Gerenciar USB-C Sentinel')
    usb_subparsers = usb_parser.add_subparsers(dest='usb_command', help='Comandos do USB-C Sentinel')

    # usb config
    usb_config_parser = usb_subparsers.add_parser('config', help='Configurar USB-C Sentinel')
    usb_config_parser.add_argument('--action', type=str, help='Comando a ser executado quando um dispositivo não autorizado é detectado.')

    # usb simulate-locked
    usb_simulate_locked_parser = usb_subparsers.add_parser('simulate-locked', help='Simular status de telefone bloqueado.')
    usb_simulate_locked_parser.add_argument('--status', choices=['locked', 'unlocked'], required=True, help='Definir status do telefone.')

    # usb simulate-usb
    usb_simulate_usb_parser = usb_subparsers.add_parser('simulate-usb', help='Simular status de conexão USB.')
    usb_simulate_usb_parser.add_argument('--status', choices=['connected', 'disconnected'], required=True, help='Definir status do dispositivo USB.')

    # usb status
    usb_subparsers.add_parser('status', help='Mostrar status do USB-C Sentinel.')

    # usb run-check
    usb_subparsers.add_parser('run-check', help='Executar uma checagem manual do USB-C Sentinel.')

    args = parser.parse_args()

    if args.command == 'dmt':
        if args.dmt_command == 'config':
            config = load_dead_mans_timer_config()
            if args.threshold:
                config['inactivity_threshold_seconds'] = args.threshold
                print(f"Threshold de inatividade definido para {args.threshold} segundos.")
            if args.nuke_command:
                config['data_nuke_command'] = args.nuke_command
                print(f"Comando Data-Nuke definido para: {args.nuke_command}")
            save_dead_mans_timer_config(config)
            print("Configuração do Dead-Man's Timer atualizada.")
        elif args.dmt_command == 'update-interaction':
            update_last_interaction()
        elif args.dmt_command == 'status':
            status = get_dead_mans_timer_status()
            print("\n--- Status do Dead-Man's Timer ---")
            for key, value in status.items():
                print(f"{key.replace('_', ' ').capitalize()}: {value}")
            print("----------------------------------")
        elif args.dmt_command == 'run-check':
            run_dead_mans_timer_check()
        else:
            dmt_parser.print_help()

    elif args.command == 'usb':
        if args.usb_command == 'config':
            config = load_usb_c_sentinel_config()
            if args.action:
                config['unauthorized_device_action'] = args.action
                print(f"Comando de ação para dispositivo não autorizado definido para: {args.action}")
            save_usb_c_sentinel_config(config)
            print("Configuração do USB-C Sentinel atualizada.")
        elif args.usb_command == 'simulate-locked':
            set_phone_locked_status(args.status == 'locked')
        elif args.usb_command == 'simulate-usb':
            set_usb_device_status(args.status == 'connected')
        elif args.usb_command == 'status':
            status = get_usb_c_sentinel_status()
            print("\n--- Status do USB-C Sentinel ---")
            for key, value in status.items():
                print(f"{key.replace('_', ' ').capitalize()}: {value}")
            print("----------------------------------")
        elif args.usb_command == 'run-check':
            run_usb_c_sentinel_check()
        else:
            usb_parser.print_help()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
