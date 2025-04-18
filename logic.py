from config import state

def handle_keyboard(key, x, y):
    if key == b' ':
        state["traffic_light"] = 1 - state["traffic_light"]

def update_car_position(delta_time):
    semaforo_pos = -0.5  # Posição do semáforo no eixo X
    speed = state["constant_speed"] * delta_time

    # Lógica do semáforo com velocidade baseada no tempo
    if not state["passed_light"]:
        if state["car_position"] + 0.5 < semaforo_pos:
            # Movimento normal antes do semáforo
            state["car_position"] += speed
        elif state["traffic_light"] == 1:  # Sinal verde
            state["car_position"] += speed
            if state["car_position"] >= semaforo_pos + 0.5:
                state["passed_light"] = True
        else:
            pass  # Não move se o sinal estiver vermelho
    else:
        # Movimento normal após passar o semáforo
        state["car_position"] += speed

    # Reset ao completar o percurso
    if state["car_position"] > 5:
        state["car_position"] = -5.0
        state["passed_light"] = False

def update_clouds(delta_time):
    state["cloud_offset"] += state["constant_speed"] * 0.25 * delta_time

    if state["cloud_offset"] > 12:
        state["cloud_offset"] = -12
