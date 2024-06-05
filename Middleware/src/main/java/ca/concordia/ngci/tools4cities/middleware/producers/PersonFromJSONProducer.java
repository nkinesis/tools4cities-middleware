package ca.concordia.ngci.tools4cities.middleware.producers;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import ca.concordia.ngci.tools4cities.middleware.middleware.AbstractProducer;
import ca.concordia.ngci.tools4cities.middleware.middleware.IProducer;
import ca.concordia.ngci.tools4cities.middleware.producers.PersonFromJSONProducer.Person;

// TODO This Particular JSON producer should be a subclass of a general JSON producer
public class PersonFromJSONProducer extends AbstractProducer<List<Person>>
		implements IProducer<List<Person>> {

	public static class Person {
		private String name;
		private int age;
		private String city;

		public Person(String name, int age, String city) {
			this.name = name;
			this.age = age;
			this.city = city;
		}

		public int getAge() {
			return this.age;
		}

		public String getName() {
			return this.name;
		}

		@Override
		public String toString() {
			return "Person [name=" + name + ", age=" + age + ", city=" + city
					+ "]";
		}

	}

	private final Gson gson = new Gson();

	public PersonFromJSONProducer() {
	}

	@Override
	public List<Person> fetchData() throws IOException {
		final String json = Files
				.readString(Paths.get("src/main/resources/Data/person.json"));
		final List<Person> data = gson.fromJson(json,
				new TypeToken<List<Person>>() {
				}.getType());
		return data;
	}

	//	public void sendData() {
	//		for (Person person : data) {
	//			consumer.consumeData(person);
	//		}
	//	}
}