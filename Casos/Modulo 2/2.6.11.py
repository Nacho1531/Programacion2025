hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

start_minutes = hour * 60 + mins
end_minutes = start_minutes + dura

final_hour = (end_minutes // 60) % 24
final_mins = end_minutes % 60

print(f"{final_hour}:{final_mins}")
