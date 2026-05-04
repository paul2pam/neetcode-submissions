class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adj(n + 1);
        for (vector<int> time : times) {
            adj[time[0]].push_back({time[1], time[2]}); //time[1] is the dest, time[2] is the weight
        }

        vector<int> dist(n+1, INT_MAX); dist[k] = 0; dist[0] = 0;//because 0 doesnt exist
        
        priority_queue <pair<int, int>> pq;
        pq.push({0, k});

        while (!pq.empty()) {
            auto [d, curr] = pq.top(); pq.pop(); 

            for (auto p : adj[curr]) {
                int weight = p.second;
                int vertex = p.first;
                if (dist[curr] + weight < dist[vertex]) {
                    dist[vertex] = dist[curr] + weight;
                    pq.push({dist[vertex], vertex});
                }
            }
        }
        int tr = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == INT_MAX) return -1;
            tr = max(dist[i], tr);
        }
        return tr;
    }

};
