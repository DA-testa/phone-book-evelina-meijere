# python3
class Kontakti:
    def __init__(self,vards,numurs):
        self.vards=vards
        self.numurs=numurs

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
           if cur_query.number in contacts:
              contacts[cur_query.number].vards = cur_query.name
           else:
            contacts[cur_query.number] = Kontakti(cur_query.name, cur_query.number)
    
        elif cur_query.type == 'del':
           if cur_query.number in contacts:
            del contacts[cur_query.number]
        else:
            response = 'not found'
            if cur_query.number in contacts:
                response =contacts[cur_query.number].vards
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
