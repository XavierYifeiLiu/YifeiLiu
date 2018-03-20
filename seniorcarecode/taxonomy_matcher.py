class TaxonomyMatcher:
  def __init__(self, data):
    print(data)
    self.data = data
    self.matched_taxonomies = [ ]


  def match(self):
  	#food

  	if self.isSeniorFoodNeeds():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Senior Meals","Meals on Wheels"]
  	if self.isBasicFood():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Food Pantries","Holman","Hot Meals","Groceries"]
            #self.matched_taxonomies = ["Service","Emergency and Crisis"]


  	if self.isFoodExpenseAssistance():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Food expense assistance","CalFresh / Food Stamps","WIC"]

  	if self.isMiscFoodNeeds():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Food","Holiday Assistance"]
  	#utlity-assistance
  	if self.isElectricServicePaymentAssistance():
 		        self.matched_taxonomies = []
            self.matched_taxonomies = ["Electric service","Electric payment","Electric"]
  	if self.isGasServicePaymentAssistance():
            self.matched_taxonomies = []
            self.matched_taxonomies=["Gas assistance"]

  	#housing
  	if self.isDomesticViolence():
 	          self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Domestic Violence Shelters"]

  	if self.isTenantRights():
  		      self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Landlord/Tenant Assistance","Tenant Rights Information/Counseling"]

  	if self.isYouthShelter():
  		      self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Youth Shelters", "Runaway shelters"]

  	if self.isRentPaymentAssistance():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Section 8 Housing Choice Vouchers", "Rent payment assistance"]
  		#print matched_taxonomies

  	if self.isLowCostListing():
  		      self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Low Income/Subsidized Private Rental Housing","Home Rental Listings", "Home low cost listings"]

  	if self.isVeteranRentalAssistance():
  		      self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["shelter for veterans","rental assistance"]
  	
  	if self.isHIVRentalAssistance():
 		        self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["AIDS"]

  	if self.isHomeless():
        		self.matched_taxonomies = [ ]
            if self.isHomelessVeteran():
	               self.matched_taxonomies = ["Homeless Veterans"]

            elif self.isAtRiskOfHomeless():
	               self.matched_taxonomies = ["At Risk for Homelessness"]

        		elif self.isHomelessMale():
        			   self.matched_taxonomies = ["Homeless Men"]
        		
        		elif self.isHomelessFemale():
                 self.matched_taxonomies = ["Homeless Women"]
            else:
                 self.matched_taxonomies = ["Homeless Families"]

    #senior
    if self.isAdaptiveTech():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = [""]
    
    if self.isSeniorCenters():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = [""]
    
    if self.isCaregiverSupportGroups():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Caregiver/Care Receiver Support Groups"]
    
    if self.isCaregiverTraining():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Caregiver Training"]
    
    if self.isIHSS():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["In Home Supportive Services Application","In Home Supportive Services Subsidies"]
    
    if self.isPersonalCare():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["I need a caregiver"]
    
    if self.isRespiteCare():
            self.matched_taxonomies = [ ]
            self.matched_taxonomies = ["Adult In Home Respite Care"]


  	return self.matched_taxonomies
	
  def isBasicFood(self):
    return self.data["service_type"] == "food/basic-food"

  def isFoodExpenseAssistance(self):
    return self.data["service_type"] == "food/food-expense-assistance"

  def isSeniorFoodNeeds(self):
    #print(self.data)
    return self.data["service_type"] == "food/senior-food-needs"

  def isMiscFoodNeeds(self):
    return self.data["service_type"] == "food/misc-food-needs"

  def isElectricServicePaymentAssistance(self):
    return self.data["service_type"] == "utility-assistance/electric-service-payment-assistance"

  def isGasServicePaymentAssistance(self):
    return self.data["service_type"] == "utility-assistance/gas-service-payment-assistance"

  def isDomesticViolence(self):
    return self.data["service_type"] == "housing/domestic-violence"

  def isTenantRights(self):
    return self.data["service_type"] == "housing/tenant-rights"

  def isYouthShelter(self):
    return self.data["service_type"] == "housing/youth-shelter"

  def isRentPaymentAssistance(self):
    return self.data["service_type"] == "housing/rental-assistance/rent-payment-assistance"

  def isLowCostListing(self):
    return self.data["service_type"] == "housing/rental-assistance/low-cost-listing"

  def isVeteranRentalAssistance(self):
    return self.data["service_type"] == "housing/rental-assistance/veterans"

  def isHIVRentalAssistance(self):
    return self.data["service_type"] == "housing/rental-assistance/hiv-patients"

  def isHomeless(self):
    return self.data["service_type"] == "housing/homeless"

  def isHomelessVeteran(self):
    return self.data["parameters"]['is_veteran'] == "true"

  def isAtRiskOfHomeless(self):
    return self.data["parameters"]['homeless_state'] == "future"

  def isCurrentlyHomeless(self):
    return self.data["parameters"]['homeless_state'] == "current"

  def isNotHomeless(self):
    return self.data["parameters"]['homeless_state'] == "none"

  def isHomelessMale(self):
    return self.data["parameters"]['user_identity'] == "single-male"

  def isHomelessFemale(self):
    return self.data["parameters"]['user_identity'] == "single-female"
 
  def isAdaptiveTech(self):
    return self.data["service_type"] == "care/adaptive-tech"

  def isSeniorCenters(self):
    return self.data["service_type"] == "care/senior-centers"

  def isCaregiverSupportGroups(self):
    return self.data["service_type"] == "care/senior-care-support/caregiver-support-groups"

  def isCaregiverTraining(self):
    return self.data["service_type"] == "care/senior-care-support/caregiver-training"

  def isIHSS(self):
    return self.data["service_type"] == "care/senior-care-support/ihss"

  def isPersonalCare(self):
    return self.data["service_type"] == "care/senior-care-support/personal-care"

  def isRespiteCare(self):
    return self.data["service_type"] == "care/senior-care-support/respite-care"

  



