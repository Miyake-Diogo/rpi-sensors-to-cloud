# Aqui vai as infos do provider
provider "google" {
  version = "3.5.0"

  credentials = file(var.credentials_location) # coloque o caminho completo para o arquivo de credenciais

  project = var.project_id # Coloque aqui o nome de seu projeto
  region  = var.default_region
  zone    = var.default_zone
}

# Aqui será feito a criação de um bucket
resource "google_storage_bucket" "rpi-iot-data-storage" {
  name          = "rpi-iot-data-storage"
  location      = "US"
  force_destroy = true
  storage_class = "STANDARD"

}

# Aqui a criação de um topico do pub sub para que ele capture o streaming do Cloud Iot Core
resource "google_pubsub_topic" "movement-sensor" {
  name = "movement-sensor"
}

resource "google_cloudiot_registry" "cloudiot-registry" {
  name     = "rpi-cloudiot-registry"
  region   = "us-central1"
  event_notification_configs {
    pubsub_topic_name = google_pubsub_topic.movement-sensor.id
    subfolder_matches = ""
  }

}

# Aqui as infos para o Bigquery

resource "google_bigquery_dataset" "iot-dataset" {
  dataset_id                  = "movement_sensor"
  friendly_name               = "movement_sensor_data"
  description                 = "This is a dataset for movement sensor"
  location                    = "US"
  delete_contents_on_destroy  = true
  labels = {
    env = "sensor-test"
  }

}

resource "google_bigquery_table" "table" {
  dataset_id = google_bigquery_dataset.iot-dataset.dataset_id
  table_id   = "mov_sensor_data"

  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "sensor-test"
  }

  schema = <<EOF
[
  {
    "name": "timestamp",
    "type": "TIMESTAMP",
    "mode": "NULLABLE",
    "description": "Timestamp of data is captured"
  },
  {
    "name": "movement",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "String with movement is captured"
  },
  {
    "name": "temperature",
    "type": "FLOAT",
    "mode": "NULLABLE",
    "description": "Temperature of environment"
  },
  {
    "name": "humidity",
    "type": "FLOAT",
    "mode": "NULLABLE",
    "description": "Humidity of environment"
  }
]
EOF

}

# Aqui as infos para o Dataflow
resource "google_dataflow_job" "iot_data_job" {
  name              = "iot-dataflow-job"
  template_gcs_path = "gs://dataflow-templates/latest/PubSub_to_BigQuery" # tem de buscar na documentação
  temp_gcs_location = "gs://rpi-iot-data-storage/tmp"
  project           = var.project_id
  region            = var.default_region
  machine_type      = "n1-standard-1"
  max_workers       = "2"
  on_delete         = "drain"
  parameters = {
    inputTopic     = "projects/miyake-tech/topics/movement-sensor"
    outputTableSpec= "miyake-tech:movement_sensor.mov_sensor_data"
  }

}


