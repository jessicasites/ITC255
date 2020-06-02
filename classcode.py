class Customers():
    def __init__(self, customerID, customerLastName, customerFirstName, customerEmail):
        self.customerID = customerID
        self.customerLastName = customerLastName
        self.customerFirstName = customerFirstName
        self.customerEmail = customerEmail

 # Get customerID.
  def getcustomerID(self):
    return self.__customerID

  # Set customerID.
  def setcustomerID(self, id):
    self.__customerID = id

  # Get customerLastName.
  def getcustomerLastName(self):
    return self.__customerLastName

  # Set customerLastName
  def setcustomerLastName(self, name):
    self.__customerLastName = name

  # Get customerFirstName.
  def getcustomerFirstName(self):
    return self.__customerFirstName

  # Set customerFirstName
  def setcustomerFirstName(self, name):
    self.__customerFirstName = name
  
  # Get customerEmail
  def getcustomerEmail(self):
    return self.__customerEmail

  # Set customerEmail 
  def setcustomerEmail(self, customerEmail):
    self.__customerEmail = customerEmail

class Employee():
    def __init__(self, employeeID, employeeLastName, employeeFirstName, employeePosition):
        self.employeeID = employeeID
        self.emplpoyeeLastName = employeeLastName
        self.employeeFirstName = employeeFirstName
        self.employeePosition = employeePosition

 # Get employeeID.
  def employeeID(self):
    return self.__employeeID

  # Set employeeID.
  def setemployeeID(self, id):
    self.__employeeID = id

  # Get employeeLastName.
  def getemployeeLastName(self):
    return self.__employeeLastName

  # Set employeeLastName
  def setemployeeLastName(self, name):
    self.__employeeLastName = name

  # Get employeeFirstName.
  def getemployeeFirstName(self):
    return self.__employeeFirstName

  # Set employeeFirstName
  def setemployeeFirstName(self, name):
    self.__employeeFirstName = name
  
  # Get employeePosition
  def getemployeePosition(self):
    return self.__employeePosition

  # Set customerPosition 
  def setemployeePosition(self, employeePosition):
    self.__employeePosition = employeePosition

class Sale:
  def __init__(self, id, items, total):
    self.__saleID = id
    self.__saleItems = []
    self.__orderTotal = 0

  # Get saleID.
  def getsaleID(self):
    return self.__saleID

  # Set saleID.
  def setsaleID(self, id):
    self.__saleID = id

  #Get items
  def getSaleItems(self):
    return self.__saleItems

 # Set items.
  def setsaleItmes(self, items):
    self.__saleItems = items
  
  # Get total.
  def getsaleTotal(self):
    return self.__saleTotal

class Items():
    def __init__(self, itemID, itemName, itemPrice, itemDesc:
        self.itemID = itemID
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemDesc = itemDesc

    # Get itemID.
  def itemID(self):
    return self.__itemID

  # Set itemID.
  def itemID(self, id):
    self.__itemID = id

  # Get itemName.
  def getitemName(self):
    return self.__itemName

  # Set itemName
  def setitemName(self, name):
    self.__itemName = name

  # Get itemPrice.
  def getitemPrice(self):
    return self.__itemPrice

  # Set itemPrice
  def itemPrice(self, price):
    self.__itemPrice = price
  
  # Get itemDesc
  def itemDesc(self):
    return self.__itemDesc

  # Set itemDesc 
  def setitemDesc(self, description):
    self.__itemDesc = itemDesc


