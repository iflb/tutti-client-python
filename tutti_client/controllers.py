class ResourceController:
    def __init__(self, duct):
        self.duct = duct
        
    async def list_projects(self):
        await self.duct.send(self.duct.next_rid(), self.duct.EVENT["LIST_PROJECTS"], None)

class MTurkController:
    def __init__(self, duct):
        self.duct = duct
