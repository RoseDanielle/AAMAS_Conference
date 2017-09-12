package za.redbridge.simulator.NEAT;

import org.encog.ml.data.MLData;
import org.encog.ml.data.basic.BasicMLData;
import org.encog.neural.neat.NEATNetwork;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import sim.util.Double2D;
import za.redbridge.simulator.phenotype.Phenotype;
import za.redbridge.simulator.sensor.AgentSensor;
import za.redbridge.simulator.Morphology;

public class NEATPhenotype implements Phenotype {

	private final NEATNetwork network;
	private final Morphology morphology;

	private final MLData input;
	private final List<AgentSensor> sensors;

	/**
	Constructs an experiment phenotype (ANN + morphology)
	@param NEATNetwork network: NEAT's phenotype, the ANN for the robot's controller
	@param Morphology morphology: the morphology that each robot will take on
	**/
	public NEATPhenotype (NEATNetwork network, Morphology morphology) {
		this.network = network;
		this.morphology = morphology;

		// Initialise sensors
		final int numSensors = morphology.getNumSensors();
		sensors = new ArrayList<>(numSensors);
		for (int i = 0; i < numSensors; i++) {
		    sensors.add(morphology.getSensor(i));
		}

		//Construct this object with blank data and a specified size.
		input = new BasicMLData(numSensors);
	}

	public NEATNetwork getNetwork () {
		return network;
	}

	public Morphology getMorphology () {
		return morphology;
	}

	@Override
	public List<AgentSensor> getSensors() {
	    return sensors;
	}

	@Override
	public Double2D step(List<List<Double>> sensorReadings) {
	    final MLData input = this.input;
	    for (int i = 0, n = input.size(); i < n; i++) {
	        input.setData(i, sensorReadings.get(i).get(0));
	    }

	    MLData output = network.compute(input);
	    return new Double2D(output.getData(0) * 2.0 - 1.0, output.getData(1) * 2.0 - 1.0);
	}

	@Override
	public Phenotype clone() {
	    return new NEATPhenotype(network, this.morphology.clone());
	}

	@Override
	public void configure(Map<String, Object> stringObjectMap) {
	    throw new UnsupportedOperationException();
	}

	@Override
	public String toString() {
		String toPrint = "Experiment phenotype: \n";
		for (AgentSensor a : sensors) {
			toPrint += "\t " + a.toString();
		}
		return toPrint;
	}
}