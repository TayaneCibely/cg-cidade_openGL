from config import state

def handle_keyboard(key, x, y):
    if key == b' ':
        state["traffic_light"] = 1 - state["traffic_light"]

def update_car_position():
    semaforo_pos = -0.5  # posição do semáforo

    # Se o carro ainda não passou do semáforo
    if not state["passed_light"]:
        if state["car_position"] + 0.5 < semaforo_pos:  # corpo inteiro antes do semáforo
            state["car_position"] += 0.05
        elif state["traffic_light"] == 1:  # sinal verde
            state["car_position"] += 0.05
            if state["car_position"] >= semaforo_pos + 0.5:
                state["passed_light"] = True
    else:
        # Já passou, segue andando
        state["car_position"] += 0.05

    # Reset ao fim do caminho
    if state["car_position"] > 5:
        state["car_position"] = -5.0
        state["passed_light"] = False

def update_clouds():
    state["cloud_offset"] += 0.01
    if state["cloud_offset"] > 12:
        state["cloud_offset"] = -12