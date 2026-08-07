class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dest = {}
        tickets = sorted(tickets, reverse = True)
        for ticket in tickets: 
            dest[ticket[0]] = dest.get(ticket[0], [])
            dest[ticket[0]].append(ticket[1])
        print(tickets)
        print(dest)
        res = []
        def dfs(airport):
            print(f"airport: {airport}, destinations: {dest.get(airport, [])}")
            while dest.get(airport, []):
                adj = dest.get(airport, []).pop()
                dfs(adj)
            
            res.append(airport)
            print(f"we just added {airport} to {res}")
        dfs("JFK")

        
        return res[::-1]