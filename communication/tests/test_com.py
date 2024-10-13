from pymodbus.client import ModbusSerialClient
from pymodbus.pdu.register_read_message import ReadHoldingRegistersResponse
from pymodbus.pdu.register_write_message import WriteSingleRegisterResponse
from unittest.mock import patch
import logging

# Setup logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Modbus Client Setup
client = ModbusSerialClient(framer='rtu', port='/dev/ttyUSB0', baudrate=9600, timeout=1)

# For å koble til klienten når vi har en:)
# client.connect()

# Mock Read and Write Methods
with patch.object(client, 'read_holding_registers') as mock_read, \
     patch.object(client, 'write_register') as mock_write:
    
    # Mocked Read Response
    mock_read.return_value = ReadHoldingRegistersResponse([160, 500])
    
    # Perform a read operation
    result_read = client.read_holding_registers(1000, 2)
    if result_read.isError():
        print("Error reading from Modbus")
    else:
        print(f"Read Holding Registers: {result_read.registers}")
    
    # Mocked Write Response
    mock_write.return_value = WriteSingleRegisterResponse(1000, 1234)
    
    # Perform a write operation
    result_write = client.write_register(1000, 1234)
    if result_write.isError():
        print("Error writing to Modbus")
    else:
        print(f"Successfully wrote to register {result_write.address} with value {result_write.value}")
