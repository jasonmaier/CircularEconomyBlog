
# coding: utf-8

# #Functions for Material Circularity Indicator

# In[1]:

## Calculate Virgin Feedstock
#M = mass
#Fr = Fraction of feedstock from recycled materials
#Fu = Fraction of materials from reused sources
def VirginFeedStock(Mass, Fr, Fu):
    VirginFeed = Mass * (1 - Fr - Fu)
    #print "Virgin Feedstock = %s" % VirginFeed
    return VirginFeed


# In[3]:

X = VirginFeedStock(100, 0.5, 0.1)
print X


# In[10]:

##Calculate Unrecoverable Waste
#Cr = Fraction of mass collected for recycle
#Cu = Fraction of mass collected for reuse
#Wo = Unrecoverable Waste Init
#Wc = Unrecoverable waste from Recycling
#Wf = Unrecovereable waste from Recycling Feed
#Wf = Waste generated to produce recycled Feedstock
#Ec = efficiency of recycling process
#Ef = efficiency of recycling process for feedstock
#Wtot = Total unrecoverable waste

def UnrecovWaste(Mass, Cr, Cu, Ef, Ec, Fr, Fu):
    W0 = Mass * (1 - Cr - Cu)
    print W0
    Wc = Mass * (1 - Ec) * Cr
    print Wc
    Wf = Mass * ((1 - Ef)*Fr/Ef)
    print Wf
    Wtot = W0 + (Wf + Wc)/2
    print "Total unrecoverable waste = %s" % Wtot
    return Wtot, Wc, Wf


# In[11]:

UnrecovWaste(100, 0.1, 0.1, 0.9, 0.1, 0.1, 0.1)


# In[14]:

##Calculating Linear Flow Index
## LFI = Linear Flow Index (between 0, 1 where 0 is completely linear)
def LinearFlowIndex(Mass, Fr, Fu, Cr, Cu, Ef, Ec):
    VirginFeed = VirginFeedStock(Mass, Fr, Fu)
    print VirginFeed
    Wtot, Wc, Wf = UnrecovWaste(Mass, Cr, Cu, Ef, Ec, Fr, Fu)
    LFI = (VirginFeed + Wtot)/(2 * Mass + (Wf - Wc)/2)
    return LFI


# In[15]:

LinearFlowIndex(100, 0.1, 0.1, 0.9, 0.1, 0.1, 0.1)


# In[16]:

##Calculating the Utility
#X = Utility
#L = Length of Use
#Lav = Average Length of use
#U = intensity of use
#Uav = average intensity of use
def Utility (L, Lav, U, Uav):
    X = (L/Lav)*(U/Uav)
    return X
    


# In[17]:

##Calculate Material Circularity Indicator
###MCIp = MCI for a product
def MatCircInd(LFI, X):
    MCIx = 1 - LFI * (0.9/X)
    MCI = max(0, MCIx)
    return MCI


# In[18]:

MatCircInd(0.9, 1)


# In[ ]:



