#
import readConfig

readConfig = readConfig.ReadConfig()


class GeturlParams:
    def get_url(self):
        new_url = readConfig.get_http("scheme") + '://' + readConfig.get_http("baseurl") + ':' + readConfig.get_http("port")
        return new_url


if __name__ == "__main__":
    print(GeturlParams().get_url())
