class Solution(object):
    def canVisitAllRooms(self, rooms):
		
        if rooms == None or len(rooms) == 0:  # check whether the input is none
            return False
        
        entered = self.dfs(rooms, 0, [])      # start dfs from room 0
        return len(entered) == len(rooms)     # check if all the rooms have been entered
    
    def dfs(self, rooms, source, entered):
        
        if source in set(entered):            # if the room is entered, stop
            return entered
        
        entered.append(source)                # if the room is not entered, add it to the entered list 
        
        for j in rooms[source]:               # start dfs
            if j not in entered:
                entered = self.dfs(rooms, j, entered)
            
        return entered