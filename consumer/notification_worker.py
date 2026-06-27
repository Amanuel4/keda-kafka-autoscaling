import os, json, time, random, socket, logging
from kafka import KafkaConsumer

POD = socket.gethostname()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s [%(name)s] %(message)s")
logger = logging.getLogger(POD)

BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "demo-kafka-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "notification-events")
GROUP = os.getenv("KAFKA_GROUP", "notification-processors")

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP,
    group_id=GROUP,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode())
)

for msg in consumer:
    e = msg.value
    logger.info(f"Received ID={e['notificationId']} Channel={e['channel']} Priority={e['priority']} Type={e['messageType']} Recipient={e['recipient']}")
    time.sleep(random.randint(3, 5))
    logger.info(f"Delivered ID={e['notificationId']} Partition={msg.partition} Offset={msg.offset}")