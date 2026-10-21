from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    now_time = 0
    bridge = deque()
    i = 0

    while i < len(truck_weights):
        truck_weight = truck_weights[i]

        # 다리 위에 트럭이 없으면 트럭을 올린다.
        if len(bridge) == 0:
            now_time += 1
            bridge.append((truck_weight, now_time + bridge_length))
            weight -= truck_weight
            i += 1
            continue

        # 다음 트럭이 올라갈 수 있다면 다음 트럭을 올린다. 1초가 지나간다.
        if len(bridge) < bridge_length and weight >= truck_weight:
            now_time += 1
            bridge.append((truck_weight, now_time + bridge_length))
            weight -= truck_weight
            i += 1

            # 이 때, 앞의 트럭이 빠져나오는 시간이라면 빠져나온다.
            while bridge:
                if bridge[0][1] <= now_time:
                    bridge_truck_weight, _ = bridge.popleft()
                    weight += bridge_truck_weight
                else:
                    break

        # 트럭이 올라갈 수 없다면 다리 위의 트럭이 빠져나온다. 그만큼 시간이 지난다.
        else:
            bridge_truck_weight, bridge_time = bridge.popleft()
            weight += bridge_truck_weight

            if now_time < bridge_time:
                now_time = bridge_time

            if weight >= truck_weight:
                bridge.append((truck_weight, now_time + bridge_length))
                weight -= truck_weight
                i += 1

    if bridge:
        bridge_time = bridge[-1][1]
        if now_time < bridge_time:
            now_time = bridge_time

    answer = now_time

    return answer