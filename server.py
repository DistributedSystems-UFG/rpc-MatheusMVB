import rpyc
from constRPYC import PORT
from rpyc.utils.server import ThreadedServer


class DBList(rpyc.Service):
    values = []

    def exposed_append(self, data):
        self.values = self.values + [data]
        return self.values

    def exposed_values(self):
        return self.values

    def exposed_search(self, value):
        for v in self.values:
            if value == v:
                return f"Valor {v} encontrado"
        return "Valor não encontrado"

    def exposed_remove(self, value):
        t = 0
        for v in self.values:
            if value == v:
                self.values.remove(value)
                t = -1

            if t == -1:
                return "Valor removido da lista"
            else:
                return "Valor não encontrado na lista"

    def exposed_sort(self):
        self.values.sort(reverse=False)
        return self.values


print(f"Servidor iniciado na porta {PORT}")
server = ThreadedServer(DBList, port=PORT)
server.start()
