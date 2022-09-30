# Add-different-sources-to-POS-orders
Add different sources to POS orders odoo




# Related Scenario: 
POS users spend their time inserting orders into the system, they get those orders from different sources. Usually, they get it directly from customers standing in front of them, but sometimes they get orders by phone or through another platform like Talabat. 


# The problem: 
Currently, there's no way to distinguish different order sources. So, managers can't tell how much of their sales come from which source, and that's what we need to solve. 


# Proposed Solution: 

* Add a new model to represent the different sources.

* Add a new Many2one field to pos.order to relate orders to their sources.

* POS users should be able to select an order source from POS Screen before sending it to the backend.

* In the Orders list view, add an option to quickly search by source.

* In the Orders list view, add an option to quickly group by source.        
     
