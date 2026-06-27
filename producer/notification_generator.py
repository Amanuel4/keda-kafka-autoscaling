import os, json, time, random, uuid
from datetime import datetime
from kafka import KafkaProducer

BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "demo-kafka-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "notification-events")

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP,
    value_serializer=lambda v: json.dumps(v).encode()
)

channels = ["SMS", "EMAIL", "PUSH"]
priorities = ["LOW", "NORMAL", "HIGH"]
types = ["PAYMENT_SUCCESS", "ORDER_SHIPPED", "PASSWORD_CHANGED", "PROMOTIONAL_CAMPAIGN", "ACCOUNT_VERIFICATION", "MONTHLY_STATEMENT"]

while True:
    event = {
        "notificationId": f"NOTIF-{uuid.uuid4().hex[:8].upper()}",
        "customerId": f"CUST-{random.randint(1000, 9999)}",
        "channel": random.choice(channels),
        "priority": random.choice(priorities),
        "messageType": random.choice(types),
        "recipient": f"+2519{random.randint(10000000, 99999999)}",
        "createdAt": datetime.utcnow().isoformat()
    }
    producer.send(TOPIC, event)
    print(f"[PRODUCED] {event['notificationId']} {event['channel']} {event['messageType']}")
    time.sleep(0.01)