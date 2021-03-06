package za.redbridge.simulator.phenotype.heuristics;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

import sim.util.Double2D;

/**
 * Created by jamie on 2014/09/10.
 */
public class HeuristicSchedule {
    private final PriorityQueue<Heuristic> schedule = new PriorityQueue<>();

    private final List<Heuristic> addList = new ArrayList<>();
    private final List<Heuristic> removeList = new ArrayList<>();

    private String activeHeuristic = "none";

    public Double2D step(List<List<Double>> readings) {
        schedule.addAll(addList);
        addList.forEach(h -> h.setSchedule(this));
        addList.clear();

        schedule.removeAll(removeList);
        removeList.forEach(h -> h.setSchedule(null));
        removeList.clear();

        Double2D wheelDrive = null;
        String activeHeuristic = "none";
        // for each heuristic in schedule check if readings are returned
        for (Heuristic heuristic : schedule) {
            wheelDrive = heuristic.step(readings);
            if (wheelDrive != null) {
                // Update the robot's paint
                heuristic.getRobot().setColor(heuristic.getColor());
                //Update active heuristic
                activeHeuristic = heuristic.getClass().getSimpleName();
                break;
            }
        }
        return wheelDrive;
    }

    public void addHeuristic(Heuristic heuristic) {
        if (!addList.contains(heuristic)) {
            addList.add(heuristic);
        }
    }

    public void removeHeuristic(Heuristic heuristic) {
        if (!removeList.contains(heuristic)) {
            removeList.add(heuristic);
        }
    }

    public synchronized String getActiveHeuristic() { return activeHeuristic; }
}
