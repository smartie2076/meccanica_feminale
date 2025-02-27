import matplotlib.pyplot as plt
import oemof.solph
import pandas as pd

data = pd.read_csv("timeseries/input_data.csv")
data = data[["demand_el", "pv", "wind"]]

datetimeindex = oemof.solph._energy_system.create_time_index(2020, number=24*365-1)
data.index = datetimeindex
data.plot()
plt.show()

energysystem = oemof.solph.EnergySystem(timeindex=datetimeindex)

bus = oemof.solph.Bus(label="Electricity")
energysystem.add(bus)

peak_demand = 1000
demand = oemof.solph.components.Sink(label="Demand",
                                     inputs={bus: oemof.solph.flows.Flow(
                                         fix=data["demand_el"], nominal_value=peak_demand)})
energysystem.add(demand)
excess = oemof.solph.components.Sink(label="Excess",
                                     inputs={bus: oemof.solph.flows.Flow()})

energysystem.add(excess)

pv = oemof.solph.components.Source(label="PV",
                                   outputs={bus: oemof.solph.flows.Flow(
                                       fix=data["pv"], nominal_value=oemof.solph.Investment(ep_costs=300)
                                   )})
energysystem.add(pv)

storage = oemof.solph.components.GenericStorage(label="Storage",
                                                inputs={bus: oemof.solph.flows.Flow()},
                                                outputs={bus: oemof.solph.flows.Flow()},
                                                nominal_storage_capacity=oemof.solph.Investment(ep_costs=500),
                                                inflow_conversion_factor=0.8)
energysystem.add(storage)

energysystem_model = oemof.solph.Model(energysystem)
energysystem_model.solve(solver="cbc")

energysystem.results["main"] = oemof.solph.processing.results(energysystem_model)
energysystem.results["meta"] = oemof.solph.processing.meta_results(energysystem_model)

results = energysystem.results["main"]
storage = energysystem.groups["Storage"]

pv_cap = results[(pv, bus)]["scalars"]["invest"]
storage_cap = results[(storage, None)]["scalars"]["invest"]
print(f"Optimized capacities: PV {pv_cap}, Storage {storage_cap} to supply annual demand of {data['demand_el'].sum()*peak_demand} at average demand of {data['demand_el'].mean()*peak_demand}")
print(f"Performance factor PV: {data['demand_el'].mean()*peak_demand/pv_cap} (ie. PV is this {pv_cap/data['demand_el'].mean()*peak_demand} times larger than highest demand)")

# electricity flows
electricity_bus_df = oemof.solph.views.node(results, "Electricity")
electricity_bus_df["sequences"].plot()
plt.show()

# Storage flows
custom_storage = oemof.solph.views.node(results, "Storage")
storage_df = custom_storage["sequences"].plot()
plt.show()