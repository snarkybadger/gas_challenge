#initialize arrays
amount_gas = [12, 4, 5, 12, 2, 3, 2, 2, 3]
cost_of_gas_to_travel = [14, 3, 5, 2, 8, 3, 2, 4, 3]

#write function

def canCompleteCircuit(amount_gas, cost_of_gas_to_travel):
    
    for initial_gas_station in range(len(amount_gas)):
        gas_tank=0 
        for i,amount in enumerate(amount_gas): 
        
            gas_station=(i+initial_gas_station)%len(amount_gas)
            print(gas_station)
            gas_tank=gas_tank+amount_gas[gas_station]
        
            gas_tank=gas_tank-cost_of_gas_to_travel[gas_station]
            print(" I'm at index: " + str(i) )
            
            if gas_tank<0:
                print("Out of gas at index" + str(gas_station))
                break
        if i==len(amount_gas)-1:
            print("Trip complete:IT IS PARTY TIME!")

#test function
print(canCompleteCircuit(amount_gas, cost_of_gas_to_travel))

