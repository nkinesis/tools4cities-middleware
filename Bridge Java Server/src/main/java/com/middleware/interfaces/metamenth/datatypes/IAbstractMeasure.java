package com.middleware.interfaces.metamenth.datatypes;

import com.middleware.enums.MeasurementUnit;
public interface IAbstractMeasure {
    String toString();
    String getMeasurementUnit();
    void setMeasurementUnit(MeasurementUnit measurementUnit);
}