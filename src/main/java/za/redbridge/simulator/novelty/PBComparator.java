package za.redbridge.simulator.novelty;

import java.util.Comparator;

public class PBComparator implements Comparator<PhenotypeBehaviour> {
	@Override
    public int compare(PhenotypeBehaviour x, PhenotypeBehaviour y)
    {
    	if (x.getBehaviouralSparseness() < y.getBehaviouralSparseness()) {
    		return -1;
    	}
    	if (x.getBehaviouralSparseness() > y.getBehaviouralSparseness()) {
    		return 1;
    	}
        return 0;
    }
}