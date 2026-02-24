class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {

        int sum_gas = 0;
        int sum_cost = 0;

        for (int i = 0; i < gas.length ; i++)
            sum_gas += gas[i];

        for (int i = 0; i < cost.length ; i++)
            sum_cost += cost[i];

        if (sum_cost > sum_gas)
            return -1;

        int total_sum = 0;
        int start_index = 0;

        for (int i = 0; i< gas.length; i++)
        {
            total_sum += gas[i] - cost[i];

            if (total_sum < 0)
            {
                total_sum = 0;
                start_index = i+1;
            }
        }

        return start_index;

        
    }
}