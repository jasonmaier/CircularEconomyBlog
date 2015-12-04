class webtool:
	def VirginFeedStock(Mass, Fr, Fu):
		VirginFeed = Mass * (1 - Fr - Fu)
		return VirginFeed



	def UnrecovWaste(Mass, Cr, Cu, Ef, Ec, Fr, Fu):
		W0 = Mass * (1 - Cr - Cu)
		Wf = Mass * ((1 - Ef)*Fr/Ef)
		Wtot = W0 + (Wf + Wc)/2
		return Wtot, Wc, Wf

	def LinearFlowIndex(Mass, Fr, Fu, Cr, Cu, Ef, Ec):
		VirginFeed = VirginFeedStock(Mass, Fr, Fu)
		Wtot, Wc, Wf = UnrecovWaste(Mass, Cr, Cu, Ef, Ec, Fr, Fu)
		LFI = (VirginFeed + Wtot)/(2 * Mass + (Wf - Wc)/2)
		return LFI

	def Utility(L, Lav, U, Uav):
		X = (L/Lav)*(U/Uav)
		return X

	def MatCircInd(LFI, X):
		MCIx = 1 - LFI * (0.9/X)
		MCI = max(0, MCIx)
		return MCI

