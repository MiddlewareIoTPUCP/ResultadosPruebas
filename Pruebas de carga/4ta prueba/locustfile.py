from locust import HttpUser, task, between
from random import uniform, randint

class MyUser(HttpUser):
    wait_time = between(0, 1)
    headers = { 'content-type': 'application/json' }

    @task
    def query_index(self):
        data = dict()
        data["objID"] = "5f2392b1289e09014b5006ca"
        data["ownerToken"] = "y38MYcw3ZJ8zcsUNqtHa"
        readings = list()
        readings.append({ "index": 0, "reading": round(uniform(10, 30), 2) })
        readings.append({ "index": 1, "reading": randint(0, 100) })
        readings.append({ "index": 2, "reading": round(uniform(0, 4), 2) })
        data["readings"] = readings
        response = self.client.post("/new_reading", json=data)

    @task
    def query_2(self):
        data = dict()
        data["objID"] = "5f23bbe9756b9dff3fa464b6"
        data["ownerToken"] = "NB2KYT8b2fSWDqKy0h6A"
        readings = list()
        readings.append({ "index": 0, "reading": round(uniform(10, 30), 2) })
        readings.append({ "index": 1, "reading": randint(0, 100) })
        data["readings"] = readings
        response = self.client.post("/new_reading", json=data)

    @task
    def query_3(self):
        data = dict()
        data["objID"] = "5f23c4a901c9e282d27f2b3a"
        data["ownerToken"] = "gtZhihItKaoEHO36rHaQ"
        readings = list()
        readings.append({ "index": 0, "reading": round(uniform(10, 30), 2) })
        readings.append({ "index": 1, "reading": randint(0, 100) })
        data["readings"] = readings
        response = self.client.post("/new_reading", json=data)
