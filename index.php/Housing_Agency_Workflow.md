---
title: "Housing Agency Workflow"
layout: default
permalink: /index.php/Housing_Agency_Workflow
---

# Housing Agency Workflow

## Housing Agency Workflow
This is an exercise to build a [Workflow Net](Workflow_Nets)

### Description
Housing Agency

Registration
- potential tenants indicate their interests: 
  - certain <u>criteria</u>: price, size, location, etc
- the interests are entered into some database

Offer
- after the registration, the agency <u>sends an offer</u> when a suitable apartment is found
- customer decides to <u>accept</u> or <u>decline</u> the offer 
- if he declines, the agency <u>continues to look</u> for another flat
- if the customer doesn't respond in 2 weeks, it's assumed he has declined the offer
- if the customer declines two offers in a row, <u>the process ends</u> automatically

Contract
- if the customer accepts the offer, he has to <u>sign a contract</u>
- after signing he has to send the signed copy
- and pay 1000 USD deposit 
- once it's done, the tenants receive the keys


Payments
- they pay of the monthly basis
- every two months the finance department  <u>checks the payment history</u>
- if everything is alright - no further action is needed
- if not, then a <u>warning is sent</u>
- then the payment is checked 2 months later: if there are still problems, the <u>eviction process starts</u>
- and then the process ends

Annual inspection
- the flat is checked annually 
- ok - no actions needed
- if problems (damages) - <u>tenants have to solve</u> them in 4 weeks
- second inspection: if the problems solved - no actions are needed
- if not, the <u>damage must be paid</u> by the tenants
- if payment is not received in 3 weeks, the <u>eviction process starts</u>
- and the process ends


## [Workflow Net](Workflow_Nets) Model
To model this in [Petri Nets](Petri_Nets), [PNEditor](http://www.pneditor.org/) was used 

Obtained model:

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-housing-agency.png" alt="Image">

Bad sides of the model:
- lack of parallelism
- the model is too restrictive


## [YAWL](YAWL) Model
The main flow:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-housing-agency1.png" alt="Image">
- there are 2 [Cancellation Regions](Cancellation_Regions)
- note that for "initiate eviction process" this activity is also included to the cancellation regions of itself (for the reasons described in [Cancellation Regions](Cancellation_Regions))


Initiate Renting flow:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-housing-agency3.png" alt="Image">

Check Payment flow
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-housing-agency4.png" alt="Image">

Annual Check flow:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-housing-agency2.png" alt="Image">

In this model:
- the issue with the lack of parallelism was fixed


## Re-discovering the Model
Using the [$\alpha^+$ algorithm](Alpha_Algorithm)


Steps
- first of all, the transitions were renamed to letters
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-housing-agency-ren.png" alt="Image">
- to obtain the possible sequences  we construct the following graph:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-housing-agency-firing.png" alt="Image">
- then we execute [Breadth-First Search](Breadth-First_Search) restricting the traversal of each node to 2 visits
- and get a log with the following possible firing sequences: http://pastebin.com/kSyhR9uK
- then the [$\alpha^+$ algorithm](Alpha_Algorithm) is applied to these sequences using [EMiT](http://www.processmining.org/discontinued/emit) 
- and the following workflow net is rediscovered:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-housing-agency-redisc.png" alt="Image">



## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))

[Category:Business Process Management](Category_Business_Process_Management)