class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        
        def find_distance(worker_loc, bike_loc):
            return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])
        
        all_triplets = []
        for worker, worker_loc in enumerate(workers):
            for bike, bike_loc in enumerate(bikes):
                distance = find_distance(worker_loc, bike_loc)
                all_triplets.append((distance, worker, bike))

        all_triplets.sort()
        bike_status = [False] * len(bikes)
        worker_status = [-1] * len(workers)
        pair_count = 0

        for _, worker, bike in all_triplets:
            if worker_status[worker] == -1 and not bike_status[bike]:
                bike_status[bike] = True
                worker_status[worker] = bike
                pair_count += 1
                if pair_count == len(workers):
                    return worker_status
        
        return worker_status
    
