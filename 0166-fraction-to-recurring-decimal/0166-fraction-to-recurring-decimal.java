class Solution {
    public String fractionToDecimal(int numerator, int denominator) {

        if (numerator == 0)
        return "0";

        StringBuilder result = new StringBuilder();
        //now check if num or denom either is negative
        //use xor
        boolean negative = (numerator > 0) ^ (denominator > 0);

        if (negative)
            result.append("-");

        long dividend = Math.abs((long) numerator);
        long divisor = Math.abs((long) denominator);

        //append the integer part

        result.append(dividend/divisor);

        long remainder = dividend % divisor;

        if (remainder == 0)
            return result.toString();

        result.append(".");

        //create a hashMap

        Map<Long, Integer> hashMap = new HashMap<>();

        //process the remainder
        while (remainder != 0)
        {
            hashMap.put(remainder, result.length());
            remainder = remainder*10;
            result.append(remainder/divisor);
            remainder = remainder% divisor;

            if (hashMap.containsKey(remainder))
            {
                int position = hashMap.get(remainder);
                result.insert(position, "(");
                result.append(")");

                break;
            }

        }
        return result.toString();

    }
}