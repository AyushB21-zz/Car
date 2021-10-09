def getSegmentEquation(p, q):          #equazioni in variabile y tra due punti (tenendo conto del sistema di coordinate con y invertito) nella forma generale ax + by + c =  0

    a = p.y - q.y
    b = q.x -p.x
    c = p.x*q.y - q.x*p.y

    return (a,b,c)

def getDistance(world, car, sensors, sensorsEquations, p, q):     #dato il segmento (m,q) calcolo la distanza e la metto nel sensore corrispondente
    (a2,b2,c2) = getSegmentEquation(p, q)

    for i,(a1,b1,c1) in enumerate(sensorsEquations):
        #get intersection between sensor and segment

        if a1!=a2 or b1!=b2:
            d = b1*a2 - a1*b2
            if d == 0:
                continue
            y = (a1*c2 - c1*a2)/d
            x = (c1*b2 - b1*c2)/d
            if (y-p.y)*(y-q.y) > 0 or (x-p.x)*(x-q.x) > 0:        #se l'intersezione non sta tra a e b, vai alla prossima iterazione
                continue
        else:       #rette coincidenti
            (x, y) = (abs(p.x-q.x), abs(p.y-q.y))

        #get distance
        dist = ((car.x - x)**2 + (car.y - y)**2)**0.5

        #inserisci nel sensore nel verso giusto
        omega = car.rot +45*i                               #angolo della retta del sensore (e del suo opposto)
        alpha = 90- degrees(atan2(car.y - y, x-car.x))     #angolo rispetto alla verticale (come car.rot)
        if cos(alpha)*cos(omega)*100 + sin(alpha)*sin(omega)*100 > 0:
            index = i
        else:
            index = i + 4

        if dist < sensors[index]:
            sensors[index] = dist
