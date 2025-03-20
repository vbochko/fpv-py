import hid

def main():
    read_hid()

def read_hid():
    device = hid.device()

    # edgeTX specific
    # https://manual.edgetx.org/edgetx-how-to/joystick-mapping-information-for-game-developers
    VENDOR_ID = 4617
    PRODUCT_ID = 20308

    device.open(VENDOR_ID, PRODUCT_ID)
    device.set_nonblocking(True)

    try:
        while True:
            data = device.read(64)
            if data:
                print("Received:", data)
    except KeyboardInterrupt:
        pass
    finally:
        device.close()


def list_devices():
    for dev in hid.enumerate():
        print(dev)


if __name__ == "__main__":
    main()