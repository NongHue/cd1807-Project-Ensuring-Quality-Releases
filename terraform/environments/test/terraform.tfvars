# Azure subscription vars
subscription_id = "4e780871-9657-43bf-b521-9c73706b76b1"
client_id = "a8a50224-b866-4090-8044-a7c540383a52"
client_secret = "80d8Q~JYphu3mDompG8EZdIF4zK37adIO3PDocC7"
tenant_id = "f958e84a-92b8-439f-a62d-4f45996b6d07"

# Resource Group/Location
location = "East US"
resource_group_name = "Azuredevops"
application_type = "huent15Application"

# Network
virtual_network_name = "huent15-vn"
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"

# VM
name_image = "VM"
name_vm = "VM-QA"
name_size = "Standard_B1s"
type_storage = "Standard_LRS"
admin_username = "admin26062022"
admin_password = "P@ssw0rd2022Xyz"
public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCttsH1Jkdo22a3d11vNygiagxMUywWgwpfCtMZe+D14ZhwAhFOEGTo+slDCdo1EC3+gGxX1YcC51cy2i4DGYiju6ShjvrkcyQehPVzTWokR+XN4Vks7F/UCMrI8rpZpidF6BIFrLTrJtRuik/hYd1RNvf4GQ1oP49Y593DjpRM20bRUPO+db73d1Fk+WVrknRMjIZf6Ur0AE2+KeG7wQakl6bbVpKw8Rr6gdT9gT3+/w9MgLEhxhYvD7c61UUEnVIU7OtlHXc+KHbHbcJaKZdjQroLa6KFNW1/jNqccfHMWzVL8CEk/n8JWsCpg06FKXUjrVJmoMRukRoOFoMgRqGan+B6ExnyZv3fu4sMSWk/d8UcpNaMnqexb4F+CWSOwXn9tpxOsAWMeGM3TWrzl2YzbY2SB8IwRja2+5zIMQghsph9hxNfbeju7Wd4QZuf4ma1BGiFvdDuNx0U1FR2fe8t1QJtmLco1+py+B4DG7WpNZjnv7VUWwCNXtB+3ELqiGU= nguyenkhoa@nguyens-MacBook-Air.local"

#public key on pipeline
public_key_path = "/home/vsts/work/_temp/id_rsa.pub"