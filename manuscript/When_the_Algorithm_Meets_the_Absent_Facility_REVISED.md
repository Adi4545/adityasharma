# When the Algorithm Meets the Absent Facility: The AI–Physical Execution Gap in India’s E-Waste Circular Economy

Aditya Sharma¹, Hossein Tabasi¹*, Anurag Rana¹, Pankaj Vaidya¹

¹ Shoolini University of Biotechnology and Management Sciences, Solan, Himachal Pradesh 173229, India

\* Corresponding author: Hossein Tabasi — hosseintabasi@shooliniuniversity.com

## Abstract

Recommendation models can now classify an end-of-life electronic device, score its condition, price its residual value, and rank circular recovery options in well under a second. That computational cheapness has outrun the physical system in which the recommendations are supposed to land. India is the world’s third-largest source of electronic waste, generating about 3.8 million metric tonnes a year under international accounting conventions, with generation projected to approach 14 million tonnes by 2030. Against that volume the formal layer is thin: roughly 322 registered recyclers and 72 registered refurbishers for a population of 1.4 billion, processing capacity clustered in a few industrial regions, rural collection largely missing, and about 30 percent of volume by formal accounting—considerably more by independent estimate—still moving through informal channels that have no digital interface.

The claim of this chapter is straightforward and easy to miss: an AI recommendation is not a circular outcome. Using India’s semiconductor-dense device stream, and smartphones in particular, as the empirical setting, we define the **AI–Physical Execution Gap (AIPEG)** as the systematic divergence between the circular pathway an algorithm ranks as optimal and the subset of pathways that a territory’s physical, institutional, logistical, and market infrastructure can actually deliver. Executability is specified as five simultaneous conditions—**availability, accessibility, capacity, viability, and legibility**. From those conditions we construct an Execution Feasibility Index and a Circularity Execution Ratio, locate the binding constraint at each stage of the smartphone circular chain, and formalise the reverse-logistics economics of the rural–urban divide. India’s Extended Producer Responsibility (EPR) rules and digital public infrastructure are then examined as possible gap-narrowing or gap-widening designs.

An illustrative computation under stated parameter assumptions shows that, for small devices, consolidation dominates haulage distance by more than two orders of magnitude. Consolidation still cannot restore feasibility where no licensed executor exists. The chapter therefore proposes **Infrastructure-Constrained Circular AI**: a design stance in which facility availability, distance, transport economics, and real-time capacity enter the objective function as constraints, not as friction discovered after the recommendation has already been issued.

**Keywords:** circular economy; artificial intelligence; electronic waste; India; reverse logistics; Extended Producer Responsibility; infrastructure constraints; emerging markets; semiconductor devices; rural–urban divide

---

## 1. Introduction: The Recommendation That Cannot Be Executed

Take a five-year-old smartphone in a village in Nuapada district, Odisha. The screen is intact. Battery capacity has fallen to about 60 percent of rating. The system-on-chip, camera module, and radio-frequency front end still function. Fed with images, diagnostic telemetry, secondary-market prices, and a materials database, a competent model will return a tidy circular plan: harvest the display and camera for the spare-parts market, replace the battery, refurbish the handset, and sell it into a price-sensitive segment. It will also emit a recovery value, an avoided-emissions figure, and a confidence score—quickly, cheaply, and often with defensible accuracy.

None of that plan has a local executor. No registered refurbisher sits within several hundred kilometres. The block has no formal collection point. The nearest authorised dismantler is in a metropolitan cluster, and moving a single 180-gram device there costs an order of magnitude more than the value recoverable from it. The aggregator who could bundle the handset into a viable shipment is informal, has no digital footprint, and does not appear in the model’s world. In practice the phone is sold for cash to a travelling scrap buyer, passed along an untraceable chain into an informal cluster, stripped of high-value components by hand, and the residual board fraction is processed in ways that recover only part of the available metal while shifting environmental and occupational harm onto workers and nearby communities.

The inference was not false. It was unused. That unused inference is the object of this chapter.

Scholarship on artificial intelligence and the circular economy has grown quickly, and much of it is optimistic. Documented applications include machine-vision sorting, predictive maintenance, digital product passports, residual-value estimation, demand forecasting for secondary materials, and platform-mediated reverse marketplaces (Ellen MacArthur Foundation, 2019; Ghoreishi & Happonen, 2020; Sarc et al., 2019; Wilts et al., 2016). The implicit theory of change is that better identification, classification, prediction, and optimisation will move materials through higher-value loops. That theory is plausible where facilities are dense, capitalised, and standardised enough to carry out most of what an optimiser proposes. India’s physical system does not meet that precondition. Once that is granted, “better inference” ceases to be a sufficient theory of circular improvement.

The limiting factor in emerging-market circularity is no longer the ability to infer. It is the ability to execute. The two have come apart. We name that decoupling the **AI–Physical Execution Gap (AIPEG)**: the systematic, measurable difference between the set of circular pathways an algorithm identifies as optimal and the subset of those pathways that a given territory’s physical, institutional, logistical, and market infrastructure can execute at acceptable cost and environmental impact. AIPEG is not a change-management problem sitting downstream of a good model. It is a structural property of the coupled system. It varies with geography and device class. Standard recommenders do not emit a signal when their output is ignored, so the gap can widen while reported performance still improves.

That invisibility has practical stakes. Programmes can post rising circularity on the strength of recommendations issued, EPR certificates traded, or platform-reported diversion even as material outcomes stall or worsen. We call the resulting artefact **phantom circularity**: algorithmically legitimated circular intent that is never physically realised, yet is counted, reported, and, under certificate-based compliance, monetised.

India is a demanding test of this claim. It is the third-largest generator of e-waste, and generation is growing faster than the infrastructure meant to absorb it. Formal recovery capacity sits in a small number of industrial clusters, while the device population is national and majority rural. At the same time, the E-Waste (Management) Rules, 2022, the Central Pollution Control Board (CPCB) EPR portal, and India’s digital public infrastructure together form one of the more digitally mediated waste-governance regimes among emerging economies—hence a real test of whether digital coordination can stand in for physical capacity. Composition matters as well. The stream is increasingly made of small, semiconductor-dense, high-value-per-kilogram devices, principally smartphones, whose circular economics are unusually sensitive to logistics cost, the variable current recommendation systems are least likely to represent.

### 1.1 Research questions

Three questions organise the chapter.

- **RQ1.** How should the divergence between the circular pathway an unconstrained optimiser recommends for an Indian end-of-life smartphone and the pathway its surrounding infrastructure can actually execute be defined and measured?
- **RQ2.** Which of the executability conditions binds first, and does the binding condition change systematically with distance from a formal facility cluster?
- **RQ3.** Do India’s certificate-based Extended Producer Responsibility regime and its digital public infrastructure stack narrow the execution gap, or does the design of either widen it?

Sections 2 and 3 answer RQ1 conceptually and formally. Sections 4 to 6 address RQ2 through India’s material substrate, a stage-by-stage bottleneck analysis, and a break-even computation. Sections 7 and 8 take up RQ3 and the design consequences.

---

## 2. Conceptual Foundations: From Circular Ambition to Circular Capability

### 2.1 The R-hierarchy and its silent assumption

Circular-economy practice is commonly organised as a hierarchy of retention strategies—refuse, rethink, reduce, reuse, repair, refurbish, remanufacture, repurpose, recycle, recover—ranked by how much product function and embodied value each preserves (Kirchherr et al., 2017; Potting et al., 2017; Reike et al., 2018). The ranking is normative. Higher R-strategies are preferred because they keep more of the energy, labour, and material complexity already locked in the artefact. Geissdoerfer et al. (2017) and Blomsma and Brennan (2017) describe how previously scattered ideas hardened into a governing paradigm; Ghisellini et al. (2016) review its spread across policy regimes.

The hierarchy is silent on who performs each R, where, at what cost, and at what throughput. It ranks desirability and treats availability as given. In dense industrial economies that assumption is often close enough that it never becomes the analytical problem. In India it is wrong in a specific way: over most of the national territory the higher R-strategies have no local executor. A ten-item menu then collapses, in practice, to informal recycling or landfill—regardless of what the artefact would merit and regardless of what an algorithm ranks first.

Velenturf and Purnell (2021) argue that circular-economy research has attended more to material flows than to the institutional and infrastructural systems that carry those flows. Corvellec et al. (2022) go further, treating circular-economy discourse as a device that can displace attention from material constraints on implementation. The extension we offer is constructive rather than dismissive. Circularity is not a fiction. The field has not named executability as an explicit variable, and in emerging markets that omission is not a second-order correction. It is often the dominant term.

### 2.2 What AI actually does in the circular economy

AI applications in circular systems cluster into four functional families. Each family stands in a different relation to physical infrastructure.

**Identification and classification.** Convolutional and transformer-based vision models classify device type, brand, model, and cosmetic condition from images; spectroscopic and X-ray systems classify material fractions on sorting lines (Gundupalli et al., 2017; Nowakowski & Pamuła, 2020; Sarc et al., 2019). These systems are substrate-coupled. They run inside a facility and are useful because the facility exists.

**Prediction and forecasting.** Models estimate remaining useful life, residual market value, component-failure probability, and secondary-material demand. Prediction is substrate-independent. It can be run anywhere, on any device, at negligible cost, and accuracy does not require a nearby plant.

**Routing and optimisation.** Systems assign end-of-life devices to R-pathways, plan collection routes, allocate volumes to facilities, and price transactions. This family is nominally substrate-aware. In the dominant literature and in commercial practice, however, the facility network is treated as an exogenous given: usually complete, always reachable.

**Coordination.** Platforms, digital product passports, marketplaces, and traceability systems match supply and demand among participating actors (Jensen et al., 2023). Coordination is substrate-conditional. It can raise the productivity of capacity that already exists. It cannot invent capacity that does not.

The argument turns on the asymmetry among these families. Substrate-independent capabilities scale quickly and cheaply, and they have. Substrate-coupled and substrate-conditional capabilities are bounded by physical assets that scale slowly, need capital, and are unevenly placed. A model could, in principle, classify every smartphone retired in India this year. The formal system can process only a fraction of that volume, and only in a few places. The recommendation layer has scaled by orders of magnitude. The execution layer has not.

### 2.3 The missing variable: executability

A circular recommendation is therefore treated here as a triple: a device state, a proposed retention strategy, and a designated executing facility. The recommendation is executable if and only if five conditions hold at once.

- **Availability** — a facility exists within the reachable system that is technically equipped and licensed to perform the strategy.
- **Accessibility** — the device can physically reach that facility along an existing, lawful, and functioning logistics chain.
- **Capacity** — the facility has throughput available to accept the device within a window before residual value decays below threshold.
- **Viability** — recovered value net of collection, aggregation, transport, processing, and compliance cost is positive for every actor whose participation the chain requires.
- **Legibility** — the transaction is recordable, verifiable, and creditable within the governing institutional framework, so that the actors who perform it are recognised and compensated.

Failure of any one condition invalidates the recommendation, however accurate the underlying inference. Executability is conjunctive, not compensatory: strength on four dimensions does not offset failure on the fifth. That structure is why AIPEG is severe rather than merely inconvenient, and why further gains in model accuracy yield near-zero gains in circular outcomes once any single condition binds.

---

## 3. Defining the AI–Physical Execution Gap

### 3.1 Conceptual definition

The **AI–Physical Execution Gap** is the systematic divergence between the set of circular pathways an algorithmic system identifies as optimal for a population of end-of-life devices and the subset of those pathways that the surrounding physical, institutional, logistical, and market infrastructure can execute at acceptable cost and environmental impact within the devices’ value-retention window.

Four properties follow from the definition. First, the gap is systematic rather than stochastic. Geography, device class, and institutional design structure it, which makes it predictable and, in principle, addressable. Second, it is relational: a property of the pairing of an algorithm with a territory, not of either alone. The same model can show a small gap in a metropolitan cluster and a near-total gap two hundred kilometres away. Third, it is time-bounded. Residual value decays, so a pathway that becomes executable only after the value-retention window has closed was never executable in any operational sense. Fourth, it is invisible by default. Ordinary recommendation architectures do not flag unused output, so reported performance can improve while the gap widens without bound.

### 3.2 Five dimensions of the gap

The five executability conditions map onto five dimensions of the gap. Each has characteristic causes, observables, and remediation instruments (Table 1).

**Table 1.** The five dimensions of the AI–Physical Execution Gap.

| Dimension | Failure condition | Primary observable indicator | Dominant cause in India | Remediation instrument |
| --- | --- | --- | --- | --- |
| Availability | No licensed facility can perform the strategy anywhere in the reachable system | Facility counts per device-population unit; strategy coverage ratio | Extreme scarcity of registered refurbishers relative to recyclers; near-absence of component-level recovery licensing | Licensing reform; capacity investment; strategy-specific authorisation categories |
| Accessibility | A facility exists but the device cannot lawfully or economically reach it | Mean and 90th-percentile distance to nearest capable facility; collection-point density | Spatial concentration of capacity in industrial clusters; absent rural collection infrastructure | Aggregation nodes; hub-and-spoke reverse logistics; postal and retail network integration |
| Capacity | The facility exists and is reachable but cannot accept the volume in time | Facility utilisation rate; queue time versus value-decay rate | Thin installed throughput; seasonal and campaign-driven volume spikes; no real-time capacity signalling | Capacity registers; dynamic allocation; buffer storage nodes |
| Viability | Execution is physically possible but value-negative for at least one required actor | Net margin per device by pathway and origin; break-even distance and minimum viable consignment | High fixed consignment cost for small devices; low formal buy-back prices versus informal cash offers | Floor prices; EPR fee modulation; origin-indexed subsidy; consolidation economics |
| Legibility | Execution occurs but cannot be recorded, verified, or credited | Share of flow with digital provenance; informal-sector integration rate | Structural exclusion of informal aggregators from the EPR portal architecture | Tiered registration; aggregator digital identity; verified handover protocols |

The dimensions bind in chain order and combine multiplicatively rather than additively. Better logistics does not repair an availability failure. Extra plant capacity does not help a device that cannot reach the plant. Information does not repair a viability failure. The measurement approach below encodes that multiplicative structure. It also helps explain a recurring policy puzzle: large outlays along one dimension often produce little aggregate change, because another dimension remains binding.

### 3.3 Operationalisation: the Execution Feasibility Index

Let \(d\) be an end-of-life device with state vector \(s(d)\). Let \(r\) be a candidate retention strategy in the R-hierarchy, and let \(F(r)\) be the set of licensed and equipped facilities able to perform \(r\). The Execution Feasibility Index \(\varphi(d, r)\) is the product of five terms, each bounded on the unit interval:

\[
\varphi(d, r) = A(r) \times Acc(d, r) \times Cap(r, t) \times V(d, r) \times L(d, r) \tag{1}
\]

where the terms are as follows.

- \(A(r)\) is the availability term, a binary indicator equal to 1 if \(F(r)\) is non-empty within the administratively reachable system and 0 otherwise. The binary form is deliberate. Existence of a licensing category is not the same as availability of a facility able to accept a particular device, so \(A(r)\) as specified here is a permissive upper bound.
- \(Acc(d, r)\) is the accessibility term, a monotonically decreasing function of the effective transport distance from the device origin to the nearest facility in \(F(r)\), modulated by route quality, consolidation opportunity, and lawful transport constraints on hazardous fractions. We adopt a logistic-decay form, \(Acc = 1 / (1 + \exp[\beta(\delta - \delta_{1/2})])\), where \(\delta\) is effective road distance, \(\delta_{1/2}\) is the distance at which accessibility falls to one half, and \(\beta\) controls the steepness of decay. Both parameters are device-class specific: decay is steep for low-mass, low-unit-value items and shallow for high-value or high-mass items over which transport cost is amortised against recoverable value.
- \(Cap(r, t)\) is the capacity term, the probability that a facility in \(F(r)\) can accept the device within the value-retention window beginning at time \(t\). It is computed from installed throughput, current utilisation, and expected queue length. Of the five terms, this one is most amenable to real-time instrumentation, and it is the one most conspicuously absent from current systems.
- \(V(d, r)\) is the viability term, a normalised measure of the net economic surplus generated by executing \(r\) on \(d\) after collection, aggregation, transport, processing, compliance, and margin requirements at every intermediate node. \(V\) must be read as the minimum across the chain, not the sum across it: a chain with positive aggregate surplus but one value-negative intermediary will not run, because that intermediary defects to the informal channel. Formally, \(V\) is zero if any required actor faces a non-positive surplus.
- \(L(d, r)\) is the legibility term, the probability that a completed transaction will be recorded and credited within the prevailing institutional framework. It is zero along routes passing through unregistered actors. In India, legibility failure and viability success are frequently correlated: the least legible path is often the cheapest executable one.

### 3.4 Aggregate measurement: the Circularity Execution Ratio

The Execution Feasibility Index evaluates a single device–strategy pair. System-level assessment requires an aggregate. Let \(R^*(d)\) be the strategy an unconstrained optimiser would recommend for device \(d\) on purely technical grounds, that is, the highest attainable point on the R-hierarchy. Let \(\hat{R}(d)\) be the highest-ranked strategy whose \(\varphi\) exceeds a decision threshold. For a population of devices \(D\) we define the Circularity Execution Ratio as:

\[
CER(D) = \frac{\sum_{d \in D} w(d) \cdot value(\hat{R}(d))}{\sum_{d \in D} w(d) \cdot value(R^*(d))} \tag{2}
\]

where \(w(d)\) weights devices by mass, embodied impact, or recoverable value according to the purpose of the analysis, and \(value(\cdot)\) maps a strategy to a retained-value or avoided-impact score. A system with no execution gap has a CER of one; a system whose recommendations are systematically inexecutable has a CER approaching zero. A summary measure of the AI–Physical Execution Gap follows directly as

\[
AIPEG(D) = 1 - CER(D).
\]

The measure is useful for policy in three respects. Because \(\varphi\) is multiplicative, shortfalls can be attributed to specific dimensions, so a state or district can see which constraint to relieve first. CER can be computed by district, which maps the geography of inexecutable circularity and identifies where marginal infrastructure investment would release the greatest volume—arguably the highest-value use of AI in an infrastructure-constrained circular economy. The comparison is also counterfactual: realised outcomes against technical potential, rather than against last year’s performance, which is the relevant benchmark for a resource-constrained transition.

### 3.5 The status of these measures

\(\varphi\) and CER are proposed measurement instruments, not validated indices. Their parameters—particularly the accessibility decay parameters \(\beta\) and \(\delta_{1/2}\), the consolidation factor, and the normalisation of \(V\)—require calibration against operator-level logistics and facility data that are not currently in the public domain. Section 6 computes both quantities for a small set of stated parameter assumptions in order to show the structure of the framework and the relative magnitude of its terms. Those computations are illustrative. They are not empirical estimates of Indian circularity, and they should not be cited as such. Section 9.4 sets out what a first empirical estimation would require.

---

## 4. India’s Material Substrate: What the Algorithm Is Recommending Into

### 4.1 Volume, composition, and trajectory

India’s e-waste generation is approximately 3.8 million metric tonnes per annum under international monitoring conventions, making it the third-largest generator in the world after China and the United States (Baldé et al., 2024). Generation is projected to reach roughly 14 million tonnes by 2030 on a business-as-usual path of device penetration, income growth, shortening replacement cycles, and the electronification of formerly non-electronic product categories.

For the argument developed here, composition matters more than size. India has recorded among the fastest growth rates in the world in screens, computing equipment, and small information and telecommunications equipment: the fraction that is semiconductor-dense, low in unit mass, high in unit value, and rich in critical and precious metals. The country has more than a billion active mobile connections, and aggressive device financing and trade-in promotion are shortening handset replacement cycles. A smartphone weighs roughly 180 to 200 grams and contains gold, silver, palladium, copper, cobalt, lithium, tantalum, and rare-earth elements at concentrations that make its printed circuit board assembly one of the most metal-dense materials in the anthropogenic environment, richer per tonne than primary ore by orders of magnitude. That is exactly the device class that most rewards high-R strategies and most penalises long-distance, low-density reverse logistics. Smartphone circularity is therefore governed by the variable recommendation systems are least likely to represent.

### 4.2 Evidence of data asymmetry

Credible Indian e-waste figures diverge by a factor of about three. International monitoring, which estimates generation from apparent consumption and product lifespan distributions, puts annual arisings close to 4 million tonnes. Official Indian figures, derived from registered producers’ sales data and prescribed average equipment lifespans and published through the CPCB EPR portal, recorded approximately 1.25 million tonnes in FY 2023–24 and 1.40 million tonnes in FY 2024–25, with official collection-and-processing shares of roughly 62 percent and 71 percent respectively against those figures. Independent assessments have repeatedly found that the unorganised sector handles the bulk of Indian e-waste, commonly estimated at between 70 and 90 percent.

The divergence is not a puzzle to be “resolved” by picking the better error. It is evidence for the argument of this chapter. The formal system measures against the official denominator; the country loses material against the international one. The ratio between them is a crude but usable proxy for the legibility dimension of the execution gap. Steeply rising formal processing rates against the smaller denominator, while independent estimates of informal processing remain flat, is phantom circularity in textbook form: improvement in the measurement apparatus read as improvement in material outcomes. An AI system trained on portal data inherits this bias structurally. It learns what the formal system can see, optimises inside that boundary, and is blind by construction to most of the material it is supposed to govern.

### 4.3 Composition and scarcity of facilities

The formal execution layer for this volume comprises roughly 322 registered recyclers and 72 registered refurbishers. Registration counts on the CPCB EPR portal are dynamic and have ranged between approximately 300 and 450 authorised dismantlers and recyclers across recent reporting cycles, depending on category definition and reporting date. The composition of that register is more stable than the headline count, and composition is what matters analytically.

Three features stand out. Absolute density is thin: a few hundred facilities serve a device population numbering in the billions, a facility-to-population ratio at least an order of magnitude below that of jurisdictions with comparable circular ambition. There are roughly 4.5 recyclers for every refurbisher, so the formal system is biased toward the lower end of the R-hierarchy. That is availability expressed as systematic distortion rather than random shortage: even a perfect optimiser recommending refurbishment at scale would face an execution layer about four and a half times thinner than the layer for material recycling. Licensing categories, moreover, are built around dismantling and material recovery rather than component-level harvesting, repair-grade parts qualification, or module-level remanufacturing. The intermediate R-strategies that retain the most value for semiconductor devices have no dedicated regulatory home and therefore no reliable execution layer.

Capacity is also spatially concentrated. Registered recycling facilities are present in only a minority of states, and installed processing capacity is heavily concentrated in a small number of industrial regions that handle a disproportionate share of national throughput. Generation is national. A large share of arisings originates outside the metropolitan cores that host processing capacity, and a substantial share originates in districts several hundred kilometres from any licensed facility. That mismatch—where devices are retired versus where they can be processed—is the material basis of the accessibility dimension.

### 4.4 The shadow execution layer: the informal sector

By formal accounting, about 30 percent of India’s e-waste is processed through informal channels; by independent estimate, considerably more. The analytical point is not the percentage. It is the functional role. The informal sector is not the absence of an execution layer. It is a second execution layer, with a materially better profile on three of the five executability dimensions and a catastrophic profile on the remaining two.

Accessibility is strong: in dense urban settlements and in small towns and villages without formal collection, itinerant buyers reach households at the doorstep. Viability is strong as well. Cash is paid on the spot at prices formal buy-back schemes seldom match, because the cost structure excludes compliance, environmental control, formal labour cost, and taxation. Capacity is elastic; the network absorbs volume spikes without capital investment. Legibility is close to zero. Transactions leave no digital trace, and actors are structurally excluded from a portal-based EPR architecture that presupposes registration, documentation, and formal invoicing. Circular quality fails on environmental and occupational grounds: open burning, acid leaching, and manual desoldering recover part of the available metal content while imposing severe health externalities on workers and surrounding communities (Chatterjee & Kumar, 2009; Wath et al., 2011; Awasthi & Li, 2017).

The strategic implication is uncomfortable and hard to avoid. Across much of India the informal sector is the only actor capable of performing collection and aggregation at all. An AI architecture that treats informality purely as a compliance problem to be eliminated will issue recommendations that cannot be executed outside a handful of metropolitan clusters. An architecture that treats it as an execution asset to be selectively formalised—keeping its accessibility and viability advantages while progressively substituting its processing functions—faces a different feasibility frontier. Sections 7 and 8 develop that design choice.

---

## 5. Stage-by-Stage Bottleneck Analysis: The Smartphone Circular Chain

### 5.1 Stage 1: Discard decision and collection

The household decision is where residual-value models are usually asked to work. They price the handset, point the owner toward a formal channel, and quote a buy-back. None of that is execution. Execution still requires a collection point within a distance the owner will actually travel, or a reverse pickup that beats the cash offer at the door. Outside metropolitan India those two conditions are rarely both present. Take-back lives inside organised retail and brand service networks; those networks are urban. Formal quotes lose to immediate cash. Many retired handsets then sit in drawers for years, and residual value decays before any downstream plant is even in play. Accessibility and viability bind at this stage, well before capacity at a recycler can matter.

### 5.2 Stage 2: Aggregation and consolidation

A 180-gram device does not pay its own way as a singleton shipment. Reverse logistics works only when loads are bundled. Routing software can draw pickup paths and name consolidation points; it cannot invent a shed, a lock, or a custody trail. Below the district, formal aggregation is thin or missing. Informal *kabadiwalas* and small traders already perform that function, but they are outside the digital system and therefore outside the optimiser’s world model. Accessibility failure and legibility failure meet here. For most Indian e-waste, this is the point of irreversible exit from the formal pathway.

### 5.3 Stage 3: Triage and grading

Machine vision and diagnostic software can assign an initial R-strategy, grade cosmetic condition, and verify component functionality. This is the most substrate-coupled stage, and it is where AI currently adds the most demonstrable operational value. It also requires a facility with imaging apparatus, diagnostic rigs, and trained operators. India’s formal triage capacity is largely confined to a small number of refurbishment and trade-in operations. Grading standards are not nationally harmonised, so a grade assigned at one node cannot be read as equivalent to a grade assigned at another. That is a technical form of legibility failure, and a direct obstacle to distributed triage.

### 5.4 Stage 4: Reconditioning and refurbishment

For a functional handset with a degraded battery, refurbishment is almost always the value-maximising strategy, because it retains the device’s full embodied impact. Lawful, warrantied resale requires genuine or qualified spare parts, service documentation, diagnostic access, and an authorised entity. Availability binds immediately and hard: there are 72 registered refurbishers nationally. Manufacturers’ parts policies further restrict the supply of spares for older models, and repairability varies considerably across device designs. India’s evolving right-to-repair framework bears directly on this stage, because it acts on the constraint that determines whether the highest-value R-strategy is executable at all.

### 5.5 Stage 5: Component harvesting

Where full refurbishment is not feasible, salvaging display assemblies, camera modules, connectors, and memory for the repair market yields substantially more value than shredding. Component-level value estimation is a pattern-recognition problem at which models excel, and it is among the strategies AI systems most readily recommend. It is also the strategy with the thinnest formal implementation in India. Harvesting occupies a regulatory interstice between dismantling and refurbishment, has no dedicated authorisation category, and has no qualification standard that would allow harvested parts to enter formal repair channels under warranty. Informal clusters, meanwhile, harvest components at scale and with considerable skill. The capacity exists, but it is illegible and unqualified, and is therefore unavailable to the formal system.

### 5.6 Stage 6: Dismantling and fraction separation

Manual and semi-automated dismantling separates battery, display, board, housing, and cable fractions for divergent downstream processing. This is where India’s formal capacity is genuinely concentrated and where authorised dismantlers operate. Binding constraints here are capacity and throughput rather than availability, together with a technical constraint rarely encoded in recommendation systems: lithium-ion batteries are classified as hazardous for transport, and devices containing them are subject to routing restrictions that a naïve distance-minimising optimiser will violate.

### 5.7 Stage 7: Refining and material recovery

Recovering gold, silver, palladium, copper, and cobalt from board fractions requires hydrometallurgical or pyrometallurgical capability, a technical standard only a fraction of registered recyclers meet. India’s integrated capacity to refine high-value precious metals from electronic scrap is limited, and part of the highest-value fraction is exported for refining—an outcome that satisfies material circularity in the global aggregate while forgoing domestic value capture. Rare-earth elements are recovered from Indian e-waste at a negligible rate, consistent with the global pattern in which recovery meets on the order of one percent of demand. At this stage the binding constraints are capacity and viability, and the limiting factor is the sophistication of installed technology rather than the number of registered facilities.

### 5.8 Stage 8: Resale of recovered materials and refurbished devices

The loop closes only when recovered materials and refurbished devices re-enter production and consumption. India has a large and growing secondary smartphone market, which is a genuine structural advantage: demand for value-retained devices is not the limiting factor. Trust and standardisation are. A refurbished handset without a credible grade, warranty, and provenance record attracts a steep discount, and that discount cascades backward through the chain, destroying the viability of the refurbishment pathway that produced the device. A digital product passport architecture would generate a disproportionate return at this stage precisely because it addresses a legibility failure at the point where value is realised rather than where material is handled.

### 5.9 Synthesis

**Table 2.** Stage-wise comparison of algorithmic capability and formal execution capability in India’s smartphone circular chain.

| Stage | AI capability maturity | Formal execution capability | Binding gap dimension |
| --- | --- | --- | --- |
| 1. Discard and collection | High | Low outside metropolitan areas | Accessibility, Viability |
| 2. Aggregation | High | Very low; informally dominated | Accessibility, Legibility |
| 3. Triage and grading | Very high | Low; unstandardised | Availability, Legibility |
| 4. Repair and refurbishment | Moderate | Very low (72 registered entities) | Availability |
| 5. Component harvesting | High | Near zero formally; high informally | Availability, Legibility |
| 6. Dismantling | Moderate | Moderate; spatially concentrated | Capacity, Accessibility |
| 7. Material recovery | Moderate | Limited at high-value tiers | Capacity, Viability |
| 8. Resale | High | Moderate and improving | Legibility |

Read across the table and a consistent pattern appears: algorithmic capability is highest exactly where formal execution capability is lowest. Triage, harvesting, and residual-value estimation—the tasks models perform best—depend on refurbishment and harvesting layers that barely exist in India’s formal system. Conversely, the stages where the marginal AI contribution is smallest, dismantling and bulk material recovery, are the stages where India holds real capacity. The execution gap is not spread evenly along the chain; it is concentrated where the algorithmic promise is greatest. Intervention strategies that overlook this inverse relationship will misdirect both computational and capital investment.

---

## 6. The Urban–Rural Execution Divide

### 6.1 Distance, mass, and consolidation

Whether circularity is worth performing on a low-mass, high-value device is governed by the cost of moving that device to a capable facility. That cost has two components with very different behaviour. One is a haulage component, roughly proportional to distance and to mass. The other is a fixed component per consignment (vehicle call-out, stop time, handling, custody, and documentation) that is incurred once per shipment regardless of how many devices the shipment carries, and is therefore divided across the consolidation factor. Recoverable value per device, meanwhile, is bounded and modest for a mid-range end-of-life smartphone. There is consequently a break-even distance beyond which moving a device costs more than the value recoverable from it and, independently, a distance beyond which transport emissions exceed the emissions avoided by the circular intervention. Above either threshold the recommendation is not merely uneconomic but counterproductive.

Rural circularity is not simply a harder version of urban circularity. The same device generates a different cost structure depending on whether a consignment can be assembled around it. An optimiser that represents neither distance nor consolidation will systematically recommend value-destroying actions across most of India’s geography while reporting them as circular successes.

### 6.2 A break-even analysis

Let the net circular surplus of routing one device from an origin to a capable facility be:

\[
S = V_{rec} - C_{acq} - C_{agg} - C_{proc} - C_{comp} - C_{cons}/n - c_{t} \cdot \delta \cdot m \tag{3}
\]

where \(V_{rec}\) is recoverable value, \(C_{acq}\) the acquisition price paid to the holder, \(C_{agg}\) aggregation and handling cost, \(C_{proc}\) processing cost, \(C_{comp}\) compliance and documentation cost, \(C_{cons}\) the fixed cost of assembling and dispatching one consignment, \(n\) the consolidation factor (devices per consignment), \(c_{t}\) the haulage cost per tonne-kilometre, \(\delta\) the effective road distance, and \(m\) the device mass. Writing \(M = V_{rec} - C_{acq} - C_{agg} - C_{proc} - C_{comp}\) for the margin before transport, the break-even distance is:

\[
\delta_{be} = (M - C_{cons}/n) / (c_{t} \cdot m) \tag{4}
\]

and the minimum viable consignment size at a given distance is:

\[
n_{min} = C_{cons} / (M - c_{t} \cdot \delta \cdot m) \tag{5}
\]

Appendix A derives (4) and (5) from (3). Note that (3) departs from the formulation most commonly used in reverse-logistics costing, which expresses transport cost purely as a tonne-kilometre term. For a 180-gram device that formulation is dimensionally correct but empirically misleading, because the mass–distance product is so small that the haulage term becomes negligible against the per-consignment fixed cost. Separating the two components is what allows the model to identify the operative constraint rather than the nominal one.

Four structural properties follow for any reasonable parameterisation.

First, the break-even distance increases with the consolidation factor but is bounded above by \(M/(c_{t} \cdot m)\). For a smartphone that bound is very large. Distance therefore does not bind through haulage cost; consolidation binds, and distance matters chiefly because it determines whether a consignment can be assembled at all within the value-retention window.

Second, at constant value the break-even distance is inversely proportional to device mass, which explains why smartphones are simultaneously the most attractive devices to recover and among the most fragile to route: their high value density supports long-distance movement when consolidated and collapses to a near-zero viable radius when they are handled individually.

Third, consolidation cannot rescue a pathway whose margin before transport is non-positive. Where \(M \le 0\), expression (5) admits no finite \(n_{min}\). Aggregation repairs viability failures caused by cost allocation; it does not repair viability failures intrinsic to the pathway’s economics.

Fourth, \(C_{comp}\) enters with the same sign as transport cost. Every additional layer of documentation, verification, and compliance imposed on a formal pathway contracts the region in which that pathway is viable and expands the region in which the informal pathway is the only economically rational choice. Compliance design is, unintentionally, spatial policy.

### 6.3 Three territorial regimes: an illustrative computation

To show what these properties imply, we evaluate (3) and (1) for three territorial regimes and three retention strategies under the parameter assumptions set out in Appendix B. The parameters are plausible order-of-magnitude values drawn from published freight tariffs and secondary-market prices; they are not measured operator data, and the results below are a demonstration of structure, not an estimate of Indian circularity.

**Table 3.** Illustrative computation of per-device net surplus and Execution Feasibility Index by territorial regime and retention strategy, under the parameter assumptions of Appendix B. Values in Indian rupees per device. These are illustrative computations, not empirical estimates.

| Territorial regime | \(\delta\) (km) | \(n\) | Transport ₹/device | Strategy | \(M\) (₹) | \(S\) (₹) | Binding term | \(\varphi\) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metropolitan core | 25 | 200 | 2.03 | Refurbishment | 850 | 848 | — | 0.70 |
| Metropolitan core | 25 | 200 | 2.03 | Component harvesting | 200 | 198 | Availability | 0.00 |
| Metropolitan core | 25 | 200 | 2.03 | Material recycling | -35 | -37 | Viability | 0.00 |
| Mid-periphery | 180 | 40 | 22.71 | Refurbishment | 850 | 827 | — | 0.48 |
| Mid-periphery | 180 | 40 | 22.71 | Component harvesting | 200 | 177 | Availability | 0.00 |
| Mid-periphery | 180 | 40 | 22.71 | Material recycling | -35 | -58 | Viability | 0.00 |
| Hinterland, no node | 520 | 1 | 250.59 | Refurbishment | 850 | 599 | Accessibility | 0.01 |
| Hinterland, no node | 520 | 1 | 250.59 | Component harvesting | 200 | -51 | Availability | 0.00 |
| Hinterland, no node | 520 | 1 | 250.59 | Material recycling | -35 | -286 | Viability | 0.00 |
| Hinterland with node | 520 | 60 | 23.93 | Refurbishment | 850 | 826 | — | 0.51 |
| Hinterland with node | 520 | 60 | 23.93 | Component harvesting | 200 | 176 | Availability | 0.00 |
| Hinterland with node | 520 | 60 | 23.93 | Material recycling | -35 | -59 | Viability | 0.00 |

Three findings follow. First, across the full range examined, the haulage term contributes between ₹0.03 and ₹0.59 per device, a spread of about ₹0.56 across 495 kilometres, while the consolidation term contributes between ₹2.00 and ₹250.00, a spread of ₹248. The consolidation factor dominates haulage distance by more than two orders of magnitude. The widely repeated claim that distance is the primary obstacle to rural circularity for small devices is, on this parameterisation, incorrect in its mechanism even though it is correct in its conclusion: what makes remote devices unroutable is that no consignment can be assembled around them, not that they are far away.

Second, inserting an aggregation node in the hinterland raises the per-device net surplus of the refurbishment pathway from ₹599 to ₹826 and, more importantly, raises its Execution Feasibility Index from approximately 0.01 to approximately 0.51, because consolidation brings a distant but existing refurbisher into the effectively reachable system. This is the quantitative case for the aggregation node as the highest-leverage infrastructure asset in rural circularity.

Third, and against the grain of that conclusion, consolidation does nothing for component harvesting. Its net surplus is comfortably positive in three of the four regimes, yet its Execution Feasibility Index is zero everywhere, because the availability term is zero: no authorisation category exists for component harvesting anywhere in India. Similarly, formal material recycling of an individual handset is value-negative in every regime, and no consolidation factor repairs it; registered recyclers sustain themselves on mixed bulk streams and certificate revenue rather than on per-handset margin. Aggregation infrastructure and licensing reform are therefore complements, not substitutes. Building nodes without opening a harvesting category converts an accessibility failure into an availability failure and leaves \(\varphi\) at zero.

This is the answer to RQ2, and it is conditional. Under present institutional arrangements an AI recommendation issued for a rural end-of-life device cannot be executed at a cost and environmental impact that make circularity worthwhile, unless an aggregation layer is interposed that converts individual devices into consolidated flows before the transport cost is allocated, and unless a licensing category exists for the strategy the optimiser selects. Either condition alone leaves the recommendation inexecutable.

### 6.4 Design implications

This inverts the conventional intervention logic. The standard prescription for rural circularity is to push formal collection and processing capacity outward from the core. The break-even structure shows that to be the more expensive of two options: because per-device transport cost falls as \(C_{cons}/n\), low-capital aggregation nodes—which require storage, a custody protocol, a digital identity, and a payment rail but no processing plant—extend the viable radius far more cheaply than duplicating processing capacity. Such nodes can be hosted within existing rural physical networks of national coverage, including the postal network, cooperative structures, common service centres, and organised retail.

It also redefines what AI should be doing in rural India. Per-device pathway recommendation is not a useful computation there, because it is precisely the computation whose output cannot be acted upon. The useful computation is aggregation-node siting and consolidation scheduling: where to place a node, at what cost, to convert the largest volume of currently inexecutable recommendations into executable volume, and when to dispatch once accumulated volume makes dispatch worthwhile. That is a facility-location and inventory-routing problem under uncertainty, a class of problems with mature methods, and one tractable with data India already collects.

---

## 7. Institutional, Policy and Market Conditions for Closing the Gap

### 7.1 What the E-Waste (Management) Rules, 2022 cover, and what they do not

The regime notified in November 2022 and in force from April 2023 is ambitious on paper. Product coverage is wider than under earlier rules. Registration and filing run through a central CPCB portal. Collection targets rise by compliance year. Recyclers earn tradable EPR certificates against quantities recycled; producers buy those certificates to discharge their obligations. Circularity, in this design, is administered as a digital compliance market.

The five executability conditions expose how incomplete that market is. Legibility for registered actors is the dimension the Rules take most seriously: a national data spine now exists where none did. Viability is touched only indirectly, through certificate revenue that improves recycler economics. Availability is untouched. Nothing in a certificate market requires a plant in an underserved district or an authorisation category that does not already exist. Accessibility is not merely neglected; certificates are spatially fungible, so a certificate generated in a high-capacity industrial state can discharge an obligation arising from devices sold in a state with no facilities. Capacity signalling is absent as well. The portal records completed transactions, not unused throughput.

Spatial fungibility has a predictable equilibrium. The cheapest discharge of an obligation is a certificate bought from the lowest-cost recycler, and that recycler is already where capacity is concentrated. The market therefore pays for clustering. Accessibility worsens as a designed outcome, not as an oversight. Measurement in processed tonnes, rather than retained value, produces a second equilibrium: refurbishment and shredding are compliance-equivalent. A mass-recycling metric cannot preferentially pull activity up the R-hierarchy. The four-and-a-half-to-one ratio of recyclers to refurbishers in Section 4.3 is consistent with that incentive, not an accident of industrial history.

### 7.2 Digital public infrastructure as a coordination substrate

India’s digital public infrastructure is the most credible existing asset for addressing the legibility and viability dimensions together: a population-scale identity layer, a real-time low-cost payment rail, a consent-based data-sharing architecture, and an open network protocol for digital commerce. Its relevance to circularity remains largely unexplored.

The mechanism is specific. The exclusion of informal aggregators from the EPR system is not a matter of intent but of transaction infrastructure: registration is costly, invoicing presumes formal accounting, and a handover cannot be paid for and evidenced at low cost. A tiered digital identity for aggregators, instant account-to-account settlement on handover, and a lightweight cryptographic handover receipt would convert an illegible transaction into a legible one without requiring the aggregator to re-engineer their business. An open network protocol layer could then publish facility capacity, current buy-back prices, and accepted device categories as discoverable machine-readable offers: exactly the data the capacity and viability terms of the Execution Feasibility Index require, and exactly the data no current system publishes.

The caveat is the one this chapter exists to press. Digital public infrastructure improves coordination, and coordination raises the productivity of existing capacity. It does not create capacity. A perfectly instrumented market containing 72 registered refurbishers will allocate those 72 refurbishers efficiently and will still be unable to refurbish at national scale. Digital coordination is necessary; it is plainly not sufficient.

### 7.3 Five institutional conditions

In summary, the execution gap can be compressed only by the joint application of five institutional conditions.

- **Spatially differentiated compliance.** Certificate value should be modulated by the origin of the device rather than the location of processing, so that discharging an obligation with material collected from an underserved district is worth more than discharging it with metropolitan material. This converts a spatially blind market into an instrument for funding access.
- **Strategy-differentiated compliance.** Certificate value should be modulated by the level of value retention, so that material recycling is rated below refurbishment and qualified component harvesting. Without this, no market signal will correct the availability distortion at the top of the R-hierarchy.
- **A licensing category for component harvesting and parts qualification.** The intermediate strategies that retain the most value for semiconductor-dense devices currently have no regulatory home, and the informal capacity that already performs them cannot be brought into the formal system without a category to bring it into.
- **Formalisation of the aggregation layer.** A registration tier adapted to the real operating conditions of small aggregators (low documentation burden, digital identity, verified handover, guaranteed settlement) would capture the accessibility advantage of the informal network rather than competing with it. Indian experience with the integration of waste pickers into municipal solid waste systems provides precedent, and the evidence there indicates that inclusion outperforms displacement (Chintan, 2014; Wilson et al., 2006).
- **A public capacity register.** Facility throughput, current utilisation, accepted categories, and buy-back prices should be published in machine-readable form in the public domain. This is the precondition for the capacity term of any execution-aware optimiser, and it is the cheapest of the five conditions to implement.

---

## 8. Designing Circular AI for Infrastructure-Constrained Settings

### 8.1 A shift in framing

Most circular-AI systems still rank R-strategies first and treat infrastructure as something to be “implemented” after the ranking is done. **Infrastructure-Constrained Circular AI (ICCAI)** inverts that sequence. The state of the execution environment enters the objective function before ranking, and search is restricted to the executable feasible set rather than the technically ideal set. The output is not the best thing that could be done to the device in an unconstrained world. It is the best thing that can be done to this device, from this place, given the plants that exist, the throughput they have today, and the surplus the chain can actually share.

### 8.2 Architecture

ICCAI comprises four layers.

The **inference layer** performs conventional device-state estimation: classification, condition rating, component functionality assessment, residual-value prediction, and technical R-strategy ranking. This layer is analogous to existing practice, and existing models can be reused within it directly.

The **constraint layer** is the novel component. It maintains a live model of the execution environment and computes the Execution Feasibility Index for each candidate device–strategy pair. Table 4 sets out the variables it must carry, their plausible sources, and the gap dimensions each addresses.

**Table 4.** Constraint-layer variables, data sources, and the gap dimensions they address.

| Constraint variable | Data source | Update frequency | Gap dimension addressed |
| --- | --- | --- | --- |
| Facility register with licensed strategies | CPCB EPR portal; state pollution control boards | Weekly | Availability |
| Facility geolocation and road-network distance | Public geospatial data; routing services | Static, with route updates | Accessibility |
| Real-time utilisation and queue depth | Facility-reported capacity register | Daily to hourly | Capacity |
| Transport tariffs, consolidation state, hazardous-routing rules | Logistics providers; transport regulation | Daily | Accessibility, Viability |
| Secondary market prices and buy-back quotes | Marketplaces; open network protocol catalogues | Hourly | Viability |
| Aggregator network state and coverage | Tiered registration and handover records | Daily | Accessibility, Legibility |
| Compliance and documentation cost by pathway | Regulatory schedules; portal fee structures | Quarterly | Viability, Legibility |

The **decision layer** ranks strategies by expected executed value, that is, technical retained value multiplied by the Execution Feasibility Index, rather than by technical value alone. It emits a pathway, a designated facility, an aggregation route, a dispatch window, and an explicit feasibility score. Where no strategy clears the feasibility threshold, it returns a deferral with a stated reason: hold pending consolidation, hold pending capacity, or route to the highest-integrity channel available with the binding constraint recorded. A deferral is not a recommendation, and the distinction matters for reporting.

The **feedback layer** closes the loop that present systems leave open. Every recommendation is linked to a verified outcome, and every deviation is recorded as an execution failure attributed to a specific gap dimension. This telemetry is the raw material of the aggregate Circularity Execution Ratio, and it is what converts a recommendation system into a diagnostic instrument for infrastructure planning.

### 8.3 Five design principles

**Principle 1: Constrain, then rank.** Compute feasibility first and rank desirability within the feasible set. A rank-first, filter-second architecture will systematically over-promise, because the filter stage is invariably weaker than the ranking stage and is frequently absent from deployment altogether.

**Principle 2: Geographical realism.** Distance, route quality, hazardous-materials routing restrictions, and consolidation state must enter the objective function directly. A system that assumes a spatially uniform facility network will generate recommendations that are correct in the metropolitan core and systematically wrong outside it. That, we argue, describes most circular AI currently deployed in India.

**Principle 3: Temporal realism about value and capacity.** A device whose residual value halves in three weeks cannot be assigned to a pathway that becomes available in six. Capacity should be modelled as a stochastic resource indexed by time, not as a static property of a facility.

**Principle 4: Mixed-channel routing.** The optimiser’s action space must admit informal and semi-formal actors as first-class nodes with their own feasibility profiles, rather than excluding them by definitional fiat. A model restricted to routes between registered entities is blind to the actors who perform most of the collection in the country, and its recommendations are therefore void by construction across most of the country’s geography.

**Principle 5: Reflexive execution telemetry.** The system should measure and expose its own execution gap. This is the principle of greatest institutional value and least technical difficulty: a national Circularity Execution Ratio disaggregated by district, device class, and gap dimension would convert a diffuse infrastructure debate into a targeted investment problem, and would make phantom circularity visible in the one place it currently is not: the reporting layer.

### 8.4 Distributional and governance considerations

This design raises three governance problems. Feasibility-aware optimisation is conservatively biased against underserved regions: the hinterland has low \(\varphi\), so an expected-value optimiser will rationally deprioritise it, potentially entrenching the very inequity the framework diagnoses. This must be countered explicitly, either by weighting the objective for equity or by separating the operational optimiser from a planning optimiser whose objective is to maximise the gain in feasibility per rupee of infrastructure investment. Second, routing to informal actors raises legitimate concerns about environmental and labour standards; the design response is graduated integration with verified handover and progressive substitution of processing functions, not unconditional inclusion. Third, capacity registers and handover records contain commercially sensitive and personally identifiable data, and the consent architecture governing them should conform to the data-minimisation and purpose-limitation norms already established in Indian digital public infrastructure practice.

---

## 9. Implications, Limitations and Future Research

### 9.1 Theoretical implications

This chapter adds an explicit construct of executability to circular-economy theory, and in doing so argues that the R-hierarchy is an incomplete decision framework, because it orders strategies without reference to the systems that execute them. It also offers a counterpoint to the AI-for-sustainability literature: model accuracy and system outcome are not monotonically related, and the relationship can flatten entirely in infrastructure-constrained settings. The AI–Physical Execution Gap generalises beyond e-waste to any domain in which algorithmic capacity has outstripped physical capacity: precision agriculture without cold chains, diagnostic AI without treatment capacity, credit scoring without enforcement infrastructure. We propose, as a hypothesis for testing, that capable inference paired with incapable execution is the characteristic form of the AI transition in emerging economies.

### 9.2 Implications for practice and policy

For producers and platform operators, circular targets defined over recommendation volume or certificate acquisition are not evidence of circular performance; the quantity that should be governed is a Circularity Execution Ratio computed against verified outcomes. For technology developers, the highest-value application of AI in India’s circular economy is not per-device pathway recommendation but infrastructure planning: siting aggregation nodes, scheduling consolidation, and identifying where marginal capacity converts the greatest volume of currently inexecutable recommendations into executable ones. For regulators, the two highest-leverage and lowest-cost measures identified here are spatial and strategy differentiation of EPR certificate value and a public machine-readable capacity register. Both address structural distortions that no degree of algorithmic sophistication can compensate for.

### 9.3 Limitations

Three limitations qualify these claims. First, this is a conceptual and formal framework that has not been empirically validated: the Execution Feasibility Index and the Circularity Execution Ratio are proposed instruments, and their parameters, particularly the accessibility decay parameters and the consolidation factor, require calibration against operator-level logistics and facility data that are not currently public. Second, the break-even computation in Section 6 is illustrative. Its parameter values are plausible order-of-magnitude figures rather than measured data, and it is intended to establish structure and relative magnitude rather than to estimate absolute quantities; the ranking of binding constraints it produces should be treated as a hypothesis, not a result. Third, the analysis is specific to smartphones. Its conclusions should extrapolate with adjustment to other small, semiconductor-dense devices, but large appliances, with different mass-to-value ratios and different transport economics, will exhibit materially different break-even structures and possibly a different rank-ordering of binding constraints.

### 9.4 Future research

Five lines of work follow. First, empirical estimation of the Execution Feasibility Index using facility registry data, road-network distances, and operator cost data, to produce the first district-level map of executable circularity in India. Second, calibration of the accessibility decay parameters by device class against observed reverse-logistics behaviour. Third, controlled comparison of conventional and constraint-aware recommendation systems on the same device population, measuring divergence in realised rather than recommended outcomes. Fourth, treatment of aggregation-node interventions as natural experiments, in order to test the consolidation predictions of Section 6.2 directly. Fifth, comparative application of the framework to other emerging markets (Nigeria, Indonesia, Brazil) to establish whether the structure of the gap is India-specific or a general property of infrastructure-constrained circular transitions.

### 9.5 Consequences for circular business models

The execution gap reshapes which circular business models can operate viably in an emerging market. Three consequences follow for firms. Product-as-a-service, leasing, and take-back models depend on reverse logistics whose useful radius is set by the consolidation factor rather than by customer demand, so a subscription model that is profitable in a metropolitan cluster may be structurally unprofitable two hundred kilometres away in the same country. Because certificate-based compliance is spatially fungible and indifferent between refurbishment and shredding, producers face no market incentive to develop the higher-value models the R-hierarchy prefers: a firm that invests in refurbishment capacity earns no compliance premium over one that simply buys recycling certificates. And the highest-return position for a circular venture in India may not be processing at all but aggregation: a low-capital, digitally legible intermediary that converts inexecutable recommendations into executable volume and monetises the spread between informal cash offers and formal buy-back prices.

### 9.6 Relevance to the Sustainable Development Goals

The framework bears most directly on SDG 12, in that it separates reported circular intent from verified circular execution and supplies a measure, the Circularity Execution Ratio, that resists phantom circularity in national reporting. It bears on SDG 9 in that its principal concrete output is a district-level map identifying where marginal infrastructure investment would convert the greatest volume of currently inexecutable circularity into executable circularity. And it bears on SDG 8 in that it treats the informal sector as an execution asset to be graduated into the formal system rather than displaced from it.

---

## 10. Conclusion

The opening vignette was a working smartphone in a village in Odisha and a model that could name, in under a second, what ought to happen next. Inference of that kind is now cheap in India. Physical execution is not. Much of the AI-and-circularity literature has treated the first as if it were the second.

We do not argue for delaying AI until every district has a plant, nor for building plants first and models later. The useful change is in the objective. Infrastructure-Constrained Circular AI puts facility availability, distance, transport economics, and live capacity inside the optimiser, and it records unused recommendations as execution failures rather than as circular achievements. Fewer pathways will be recommended. More of those that are recommended will be ones a territory can actually run. Where none can, the honest output is a dated deferral together with the binding constraint.

The last mile will settle India’s circular transition: the aggregation shed, the consolidated load, the qualified spare, and the aggregator who can be paid and counted. Algorithms are well suited to locating, district by district, where that last mile is missing. That is not, at present, the question they are being asked.

---

## Declarations

**Funding.** The authors received no specific funding for this work.

**Conflicts of interest.** The authors declare no competing interests.

**Data availability.** No new data were generated. The illustrative computation reported in Section 6.3 uses the parameter values stated in Appendix B and can be reproduced from equations (1) and (3).

**Declaration on the use of generative AI.** The authors used generative AI tools to assist with language editing and structural revision of the manuscript. All conceptual content, formal derivations, parameter choices, interpretations, and conclusions are the authors’ own, and the authors take full responsibility for the content of the published work.

---

## References

Awasthi, A. K., & Li, J. (2017). Management of electrical and electronic waste: A comparative evaluation of China and India. *Renewable and Sustainable Energy Reviews, 76*, 434–447.

Baldé, C. P., Kuehr, R., Yamamoto, T., McDonald, R., D’Angelo, E., Althaf, S., Bel, G., Deubzer, O., Fernandez-Cubillo, E., Forti, V., Gray, V., Herat, S., Honda, S., Iattoni, G., Khetriwal, D. S., Luda di Cortemiglia, V., Lobuntsova, Y., Nnorom, I., Pralat, N., & Wagner, M. (2024). *The Global E-waste Monitor 2024*. International Telecommunication Union and United Nations Institute for Training and Research.

Blomsma, F., & Brennan, G. (2017). The emergence of circular economy: A new framing around prolonging resource productivity. *Journal of Industrial Ecology, 21*(3), 603–614.

Central Pollution Control Board. (2024). *Annual report on implementation of E-Waste (Management) Rules*. Ministry of Environment, Forest and Climate Change, Government of India.

Chatterjee, S., & Kumar, K. (2009). Effective electronic waste management and recycling process involving formal and non-formal sectors. *International Journal of Physical Sciences, 4*(13), 893–905.

Chintan Environmental Research and Action Group. (2014). *Failing the grade: How cities across India are breaking the rules that make waste pickers count*. Chintan.

Corvellec, H., Stowell, A. F., & Johansson, N. (2022). Critiques of the circular economy. *Journal of Industrial Ecology, 26*(2), 421–432.

Ellen MacArthur Foundation. (2019). *Artificial intelligence and the circular economy: AI as a tool to accelerate the transition*. Ellen MacArthur Foundation.

Geissdoerfer, M., Savaget, P., Bocken, N. M. P., & Hultink, E. J. (2017). The circular economy: A new sustainability paradigm? *Journal of Cleaner Production, 143*, 757–768.

Ghisellini, P., Cialani, C., & Ulgiati, S. (2016). A review on circular economy: The expected transition to a balanced interplay of environmental and economic systems. *Journal of Cleaner Production, 114*, 11–32.

Ghoreishi, M., & Happonen, A. (2020). New promises AI brings into circular economy accelerated product design: A review on supporting literature. *E3S Web of Conferences, 158*, 06002.

Government of India. (2022). *E-Waste (Management) Rules, 2022*. Ministry of Environment, Forest and Climate Change, Gazette Notification.

Gundupalli, S. P., Hait, S., & Thakur, A. (2017). A review on automated sorting of source-separated municipal solid waste for recycling. *Waste Management, 60*, 56–74.

Jensen, S. F., Kristensen, J. H., Adamsen, S., Christensen, A., & Waehrens, B. V. (2023). Digital product passports for a circular economy: Data needs for product life cycle decision-making. *Sustainable Production and Consumption, 37*, 242–255.

Kirchherr, J., Reike, D., & Hekkert, M. (2017). Conceptualizing the circular economy: An analysis of 114 definitions. *Resources, Conservation and Recycling, 127*, 221–232.

Nowakowski, P., & Pamuła, T. (2020). Application of deep learning object classifier to improve e-waste collection planning. *Waste Management, 109*, 1–9.

Potting, J., Hekkert, M., Worrell, E., & Hanemaaijer, A. (2017). *Circular economy: Measuring innovation in the product chain*. PBL Netherlands Environmental Assessment Agency.

Reike, D., Vermeulen, W. J. V., & Witjes, S. (2018). The circular economy: New or refurbished as CE 3.0? *Resources, Conservation and Recycling, 135*, 246–264.

Sarc, R., Curtis, A., Kandlbauer, L., Khodier, K., Lorber, K. E., & Pomberger, R. (2019). Digitalisation and intelligent robotics in value chain of circular economy oriented waste management. *Waste Management, 95*, 476–492.

Velenturf, A. P. M., & Purnell, P. (2021). Principles for a sustainable circular economy. *Sustainable Production and Consumption, 27*, 1437–1457.

Wath, S. B., Dutt, P. S., & Chakrabarti, T. (2011). E-waste scenario in India, its management and implications. *Environmental Monitoring and Assessment, 172*(1), 249–262.

Wilson, D. C., Velis, C., & Cheeseman, C. (2006). Role of informal sector recycling in waste management in developing countries. *Habitat International, 30*(4), 797–808.

Wilts, H., Bakas, I., Herczeg, M., Christis, M., Fischer, S., & Watson, D. (2016). *Digital circular economy: Opportunities and limits*. Wuppertal Institute for Climate, Environment and Energy.

---

## Appendix A. Derivation of the Break-Even Distance and the Minimum Viable Consignment

Equation (3) gives the net circular surplus of routing one device from an origin to a capable facility as

\[
S = V_{rec} - C_{acq} - C_{agg} - C_{proc} - C_{comp} - C_{cons}/n - c_{t} \cdot \delta \cdot m
\]

Collect the terms that are invariant with respect to distance and consolidation into a single margin term,

\[
M \equiv V_{rec} - C_{acq} - C_{agg} - C_{proc} - C_{comp}
\]

so that

\[
S = M - C_{cons}/n - c_{t} \cdot \delta \cdot m \tag{A.1}
\]

The break-even distance \(\delta_{be}\) is the distance at which \(S = 0\) for a given consolidation factor. Setting (A.1) to zero and solving for \(\delta\):

\[
0 = M - C_{cons}/n - c_{t} \cdot \delta_{be} \cdot m \implies c_{t} \cdot \delta_{be} \cdot m = M - C_{cons}/n
\]

\[
\delta_{be} = (M - C_{cons}/n) / (c_{t} \cdot m) \tag{A.2}
\]

reproducing equation (4).

Expression (A.2) is defined and positive only where \(M > C_{cons}/n\). Taking the limit as consolidation increases without bound gives the upper envelope of the viable radius,

\[
\lim_{n \to \infty} \delta_{be} = M / (c_{t} \cdot m) \tag{A.3}
\]

which establishes the first structural property of Section 6.2: the break-even distance is increasing in \(n\) but bounded above by a quantity that depends only on the margin, the haulage tariff, and the device mass. Because \(m\) is small for a smartphone, this bound is large, and the haulage term is therefore not the operative constraint over any plausible domestic distance.

The minimum viable consignment size at a fixed distance follows by setting (A.1) to zero and solving for \(n\) instead:

\[
C_{cons}/n_{min} = M - c_{t} \cdot \delta \cdot m \implies n_{min} = C_{cons} / (M - c_{t} \cdot \delta \cdot m) \tag{A.4}
\]

reproducing equation (5).

Expression (A.4) admits a finite positive solution only where \(M > c_{t} \cdot \delta \cdot m\). Where \(M \le 0\), no consolidation factor renders the pathway viable, which establishes the third structural property: aggregation repairs viability failures arising from the allocation of fixed cost, but not viability failures intrinsic to the margin of the pathway itself.

Finally, differentiating (A.2) with respect to \(C_{comp}\) gives \(\partial \delta_{be}/\partial C_{comp} = -1/(c_{t} \cdot m) < 0\), and differentiating with respect to the haulage tariff gives \(\partial \delta_{be}/\partial c_{t} < 0\) likewise. Compliance cost and transport cost therefore enter the viable radius with the same sign, which establishes the fourth structural property.

---

## Appendix B. Parameter Values Used in the Illustrative Computation of Section 6.3

The values below are plausible order-of-magnitude figures assembled from published road freight tariffs, observed Indian secondary-market handset prices, and reported informal buy-back offers. They are stated assumptions adopted to demonstrate the structure of the framework. They are not measured operator data, and no empirical claim is made for them. All monetary values are in Indian rupees per device unless otherwise noted.

**Table B1.** Strategy parameters.

| Strategy | \(V_{rec}\) | \(C_{acq}\) | \(C_{agg}\) | \(C_{proc}\) | \(C_{comp}\) | \(M\) = margin before transport |
| --- | --- | --- | --- | --- | --- | --- |
| Refurbishment | 3000 | 1200 | 150 | 700 | 100 | 850 |
| Component harvesting | 1400 | 700 | 150 | 250 | 100 | 200 |
| Material recycling | 120 | 60 | 30 | 40 | 25 | -35 |

**Table B2.** Territorial regime parameters. Common to all regimes: haulage tariff \(c_t = ₹6\) per tonne-kilometre; device mass \(m = 0.19\) kg, giving \(c_t \cdot m = ₹0.00114\) per device-kilometre.

| Territorial regime | Effective road distance \(\delta\) (km) | Consignment fixed cost \(C_{cons}\) (₹) | Consolidation factor \(n\) | Fixed cost per device \(C_{cons}/n\) (₹) | Haulage cost per device \(c_t \cdot \delta \cdot m\) (₹) |
| --- | --- | --- | --- | --- | --- |
| Metropolitan core | 25 | 400 | 200 | 2.00 | 0.03 |
| Mid-periphery | 180 | 900 | 40 | 22.50 | 0.21 |
| Hinterland, no node | 520 | 250 | 1 | 250.00 | 0.59 |
| Hinterland with node | 520 | 1400 | 60 | 23.33 | 0.59 |

Execution Feasibility Index components in Table 3 are assigned as follows. \(A(r) = 1\) for refurbishment and material recycling, for which authorisation categories exist, and \(A(r) = 0\) for component harvesting, for which none does. \(Acc(d, r)\) is evaluated from the logistic form of Section 3.3 with the consolidation-adjusted effective distance. \(Cap(r, t)\) is set at 0.80 in the metropolitan core and mid-periphery and 0.75 where dispatch is batched. \(V(d, r) = 1\) where \(S > 0\) and 0 otherwise, consistent with the minimum-across-chain definition. \(L(d, r)\) reflects the share of the pathway passing through registered actors. Because \(A\), \(V\), and \(L\) are effectively binary at these parameter values, \(\varphi\) is driven almost entirely by whether an authorised executor exists and whether the pathway is value-positive, rather than by the continuous terms.
