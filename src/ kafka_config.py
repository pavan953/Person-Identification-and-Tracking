from kafka import KafkaProducer, KafkaConsumer
import json
import logging

# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
FACE_RECOGNITION_TOPIC = 'face_recognition_events'

def create_kafka_producer():
    """
    Create and return a Kafka Producer
    
    Returns:
        KafkaProducer: Configured Kafka producer for sending events
    """
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        logging.info("Kafka Producer created successfully")
        return producer
    except Exception as e:
        logging.error(f"Error creating Kafka Producer: {e}")
        raise

def create_kafka_consumer(group_id='face_recognition_group'):
    """
    Create and return a Kafka Consumer
    
    Args:
        group_id (str): Consumer group ID for managing consumer instances
    
    Returns:
        KafkaConsumer: Configured Kafka consumer for receiving events
    """
    try:
        consumer = KafkaConsumer(
            FACE_RECOGNITION_TOPIC,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            auto_offset_reset='earliest',
            group_id=group_id
        )
        logging.info(f"Kafka Consumer created successfully for group {group_id}")
        return consumer
    except Exception as e:
        logging.error(f"Error creating Kafka Consumer: {e}")
        raise