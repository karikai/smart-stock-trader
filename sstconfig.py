class SSTConfig:
    latency = None

    def __init__(self, waitTime):
        self.latency = waitTime

    def setLatency(self, latency):
        self.latency = latency
