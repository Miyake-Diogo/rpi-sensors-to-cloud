# Arquivo com as Variaveis

variable "project_id"{
  type  = string
  default = "miyake-tech"
}

variable "default_region"{
  type = string
  default = "us-east1"
}

variable "default_zone"{
  type = string
  default = "us-east1-a"
}

variable "credentials_location"{
  type = string
  default = "/home/diogo/cred/terraform_miyake-tech.json"
}