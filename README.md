
<h1 style="color:red;"> Identify Underreporting (UR) issues in covid by using mathematical models </h1> 
<p style="font: italic small-caps bold 12px/30px Georgia, serif;">UR is a composite problem including UA and UE, therefore, solving UR must take the issue of Under Ascertain and Under Estimation in consideration</p>
<h2> Heterogeneity of Data Samples </h2> 
<p> Due to the limited resources of available datasets that can serve for specific analysis purposes of the paper, some parameters would be extracted and calculated from different sets of data record. Hence, we should assume that the result of each parameter can be used universally <p>
<p> For the dataset that I use to estimate the rate of UA, I assumed that people from postcode "2026" representing for the whole NSW's susceptible population and the number of infected in this dataset are the one who is under-ascertainment. </p>
 <p> => In order to create a more precise figure of underascertainment, we should conduct a real test following my proposed method to estimate the number of underreported cases </p>



<h2> UA (Under Ascertainment): this is the underreported number of people who are considered to be infectious but did not attend to local hospital admission:</h2>
<li> Firstly, we will build up a SEIR model to for the initial phase of the outbreak (before vaccination stage and under 200 infected cases). In order to do this, we need to estimate the conditional probability of a contact between “an infected” and “a susceptible” that is not observed. If we do not observe who-infects-whom, the conditional probability that j was infected by i ∈ Vj  given the observed data is: </li>
  <p align="center">
    <img src="https://res.cloudinary.com/stephenblogdata-herokuapp-com/image/upload/v1609143477/conditional_prob_xsnzwg.png" />
  </p>
<p align="center">Figure: Probability of an underreported individual got infected</p>

<ul>
<li> After receiving the underreported rate of infection, I will compute the counting process process with expectation for each i ∈ Vj : 
  </li>
<p align="center">
    <img src="https://res.cloudinary.com/stephenblogdata-herokuapp-com/image/upload/v1609143909/conditional_prob_hxvdvc.png" />
  </p>
<li>Then we will use the exposed and death number to compare with the real figure of people participating testing activities in their local clinics (NSW dataset) </li>
<li>	We should assume that all people with testing results (either positive or negative) might have interactions with covid infected patients (things would be complicated if we need to filter the types of people going to clinic, in fact, little information of personal diagnostic data can be found online (or at least for free). After that, we will take the probability of exposed population attending healthcare services </li>
<li>Things will be different in the stage of social distancing where regional areas will behave more normally during the outbreak than people in cities like Sydney. However, cross-regional interactions are certain to occur since the travel ban policy was only imposed on inter-state travelling. A new model should be used for this case - SISIR ( (Manfredi, 2017): </li>

![SISIR Model](https://res.cloudinary.com/stephenblogdata-herokuapp-com/image/upload/v1609077390/SISIR_vwnycw.png)
Figure: SISIR Model used for the social distancing period






<li>	From the infected people we can use the rate of  E->I (exposed to infected) from the SEIR model above to measure the potential exposed population => we can find the UA’s number (people who are exposed but refuse to have a medical check-up that can be recorded by official data) just like step iii. </li>
<li>To classify regions with b or n, I will put the threshold of  classification equalling to the mean of the infected number among postcode areas
<li>	Then we came to final stage of covid where vaccination are implemented to preclude the further expansion of the outbreak. There are 3 types of models will be used in this stage: </li>
=>	The model with only vaccination 
=> The model with only self-protective action
=>	Hybrid model incorporating 2 types mentioned above 
<li>	Further extension of the work: we can predict the number of reported until the dieout of the outbreak</li>
</ul>
<h2> UE (Under Estimate): Those who attended healthcare testing practices but receive True Negative results. </h2>
Since surveillance data are rare and unreliable, we should only use the official dataset from the gov to estimate the false rating of covid testing. Several approaches can be used for UE (which have been used as baseline models): 

<li>	Generalized Poisson-Mixed </li>
<li>	Negative-Binomial </li>
<li>	Gaussian Poisson </li>
<li>	Beta-Poisson</li>

