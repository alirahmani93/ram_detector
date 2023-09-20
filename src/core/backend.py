import psutil


def convert_byte_to_megabyte(byte: int):
    return byte / 1000000


def store_ram_data() -> (float, float, float):
    ram_data = psutil.virtual_memory()

    total_ram = convert_byte_to_megabyte(ram_data.total)
    free_ram = convert_byte_to_megabyte(ram_data.available)
    used_ram = convert_byte_to_megabyte(ram_data.used)
    return total_ram, free_ram, used_ram
