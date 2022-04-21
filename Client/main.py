from Client_API.client import API

if __name__ == "__main__":

    url = 'http://localhost:6000/music'
    api = API(url)

    data0 = {
        "name": "Moonlight Sonata",
        "band": "Ludwig Van Beethoven"
    }

    data1 = {
        "name": "Paranoid",
        "band": "Black Sabbath"
    }

    update = {
        "name": "Für Elise",
        "band": "Ludwig Van Beethoven"
    }

    delete = {"band": "Black Sabbath"}

    api.get()
    api.post(data0)
    api.post(data1)
    api.get()
    api.put(update)
    api.get()
    api.delete(delete)
    api.get()
    