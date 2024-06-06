# vital_health_gym
# Documentación de la Clase Gym

## Métodos y Propiedades

### `__init__(self, nit: int, name: str, adress: str)`
Inicializa una instancia de la clase Gym.
- **Parámetros**:
  - `nit` (int): Número de identificación tributaria del gimnasio.
  - `name` (str): Nombre del gimnasio.
  - `adress` (str): Dirección del gimnasio.
- **Salida**: None

### Propiedades con getters y setters
- **`get_nit`**: Devuelve el `nit` del gimnasio.
  - **Salida**: int
- **`set_nit`**: Establece un nuevo `nit` para el gimnasio.
  - **Parámetros**:
    - `nit` (int): Nuevo número de identificación tributaria.
  - **Salida**: None

- **`get_name`**: Devuelve el nombre del gimnasio.
  - **Salida**: str
- **`set_name`**: Establece un nuevo nombre para el gimnasio.
  - **Parámetros**:
    - `name` (str): Nuevo nombre.
  - **Salida**: None

- **`get_adress`**: Devuelve la dirección del gimnasio.
  - **Salida**: str
- **`set_adress`**: Establece una nueva dirección para el gimnasio.
  - **Parámetros**:
    - `adress` (str): Nueva dirección.
  - **Salida**: None

- **`get_clients_list`**: Devuelve la lista de clientes.
  - **Salida**: list
- **`set_clients_list`**: Establece una nueva lista de clientes.
  - **Parámetros**:
    - `clients_list` (list): Nueva lista de clientes.
  - **Salida**: None

- **`get_locker_list`**: Devuelve la lista de casilleros.
  - **Salida**: list
- **`set_locker_list`**: Establece una nueva lista de casilleros.
  - **Parámetros**:
    - `locker_list` (list): Nueva lista de casilleros.
  - **Salida**: None

- **`get_membership_list`**: Devuelve la lista de membresías.
  - **Salida**: list
- **`set_membership_list`**: Establece una nueva lista de membresías.
  - **Parámetros**:
    - `membership_list` (list): Nueva lista de membresías.
  - **Salida**: None

- **`get_earnings`**: Devuelve la lista de ingresos.
  - **Salida**: list
- **`set_earnings`**: Establece una nueva lista de ingresos.
  - **Parámetros**:
    - `earnings` (list): Nueva lista de ingresos.
  - **Salida**: None

### `print_all_lockers(self, to_print=False)`
Imprime o devuelve la lista de todos los casilleros.
- **Parámetros**:
  - `to_print` (bool, opcional): Si es True, imprime la información de los casilleros. Por defecto es False.
- **Salida**: None o list

### `get_empty_lockers(self, to_print=False)`
Imprime o devuelve la lista de casilleros vacíos.
- **Parámetros**:
  - `to_print` (bool, opcional): Si es True, imprime la información de los casilleros vacíos. Por defecto es False.
- **Salida**: None o list

### `assign_lockers(self, client_id, name)`
Asigna el primer casillero vacío a un cliente.
- **Parámetros**:
  - `client_id` (int): ID del cliente.
  - `name` (str): Nombre del cliente.
- **Salida**: Locker (objeto del casillero asignado)

### `get_client(self, client_id=None)`
Devuelve o imprime la información de un cliente específico o de todos los clientes.
- **Parámetros**:
  - `client_id` (int, opcional): ID del cliente. Si no se proporciona, se imprimen todos los clientes.
- **Salida**: Client (objeto cliente) o None

### `update_client(self)`
Actualiza la información de un cliente.
- **Parámetros**: Ninguno.
- **Salida**: None

### `delete_client(self, client_id)`
Elimina un cliente de la lista.
- **Parámetros**:
  - `client_id` (int): ID del cliente a eliminar.
- **Salida**: None

### `create_membership(self)`
Crea una nueva membresía y la añade a la lista de membresías.
- **Parámetros**: Ninguno.
- **Salida**: None

### `assign_client_membership(self, client_id, membership)`
Asigna una membresía a un cliente.
- **Parámetros**:
  - `client_id` (int): ID del cliente.
  - `membership` (Membership): Objeto de la membresía a asignar.
- **Salida**: None

### `handle_change_client_training(self, client_id)`
Cambia el estado de entrenamiento de un cliente.
- **Parámetros**:
  - `client_id` (int): ID del cliente.
- **Salida**: None

### `handle_client_status(self, client_id)`
Cambia el estado de actividad de un cliente.
- **Parámetros**:
  - `client_id` (int): ID del cliente.
- **Salida**: None

### `update_client_membership(self, client_id)`
Actualiza la membresía de un cliente.
- **Parámetros**:
  - `client_id` (int): ID del cliente.
- **Salida**: None

### `remaining_days_for_membership(self, client_id)`
Calcula y muestra los días restantes para la membresía de un cliente.
- **Parámetros**:
  - `client_id` (int): ID del cliente.
- **Salida**: None

### `print_membership_list(self)`
Imprime la lista de todas las membresías.
- **Parámetros**: Ninguno.
- **Salida**: None

### `generate_report_current_clients(self)`
Genera un reporte de los clientes actuales y lo guarda en un archivo.
- **Parámetros**: Ninguno.
- **Salida**: str (información del gimnasio)

### `update_assigned_client_locker(self, client_id, locker_id=None)`
Asigna un casillero a un cliente.
- **Parámetros**:
  - `client_id` (int): ID del cliente.
  - `locker_id` (int, opcional): ID del casillero a asignar. Si no se proporciona, se asigna el primer casillero disponible.
- **Salida**: None

### `delete_client_assigned_locker(self, client_id)`
Elimina el casillero asignado a un cliente.
- **Parámetros**:
  - `client_id` (int): ID del cliente.
- **Salida**: None

### `delete_client_membership(self, client_id)`
Elimina la membresía de un cliente.
- **Parámetros**:
  - `client_id` (int): ID del cliente.
- **Salida**: None

### `generate_report_day(self, date_to_search)`
Genera un reporte de los clientes atendidos en una fecha específica.
- **Parámetros**:
  - `date_to_search` (str): Fecha a buscar en formato YYYY-MM-DD.
- **Salida**: None

### `calculate_earning_peer_day(self, date_to_search)`
Calcula las ganancias del gimnasio en un día específico.
- **Parámetros**:
  - `date_to_search` (str): Fecha a buscar en formato YYYY-MM-DD.
- **Salida**: None

### `get_client_info(self, client_id)`
Muestra la información de un cliente específico.
- **Parámetros**:
  - `client_id` (int): ID del cliente.
- **Salida**: None

### `save_user(self)`
Crea y guarda un nuevo cliente.
- **Parámetros**: Ninguno.
- **Salida**: None

### `delete_membership(self, membership_type)`
Elimina una membresía específica.
- **Parámetros**:
  - `membership_type` (str): Tipo de membresía a eliminar.
- **Salida**: None

### `create_locker(self)`
Crea un nuevo casillero y lo añade a la lista de casilleros.
- **Parámetros**: Ninguno.
- **Salida**: None
