package ca.concordia.ngci.tools4cities.middleware.middleware;

import java.util.Set;

import ca.concordia.ngci.tools4cities.middleware.producer.IProducer;

public interface IOperations<T> {
	IProducer fetchdata(Set<IProducer> p);
}
