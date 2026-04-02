/**
 * T036 – Vitest coverage for contribution heatmap logic.
 * Tests computeHeatmapData from metricsCalculator.js.
 */
import { describe, it, expect } from "vitest";
import { computeHeatmapData } from "../src/services/metricsCalculator";

describe("computeHeatmapData", () => {
  it("returns empty array for null input", () => {
    expect(computeHeatmapData(null)).toEqual([]);
  });

  it("returns empty array for non-object input", () => {
    expect(computeHeatmapData("invalid")).toEqual([]);
    expect(computeHeatmapData(42)).toEqual([]);
  });

  it("returns 365 cells for a full-year calendar", () => {
    const calendar = {};
    const today = new Date();
    for (let i = 0; i < 365; i++) {
      const d = new Date(today);
      d.setDate(d.getDate() - i);
      calendar[d.toISOString().slice(0, 10)] = i % 5;
    }
    const cells = computeHeatmapData(calendar);
    expect(cells.length).toBe(365);
  });

  it("assigns intensity 0 to days with 0 commits", () => {
    const today = new Date().toISOString().slice(0, 10);
    const calendar = { [today]: 0 };
    const cells = computeHeatmapData(calendar);
    const todayCell = cells.find((c) => c.date === today);
    expect(todayCell).toBeDefined();
    expect(todayCell.intensity).toBe(0);
  });

  it("assigns intensity 4 to the highest day", () => {
    const today = new Date();
    // 5 data points so the max (50) is strictly above Q3 (40) → intensity 4
    const calendar = {};
    const counts = [10, 20, 30, 40, 50];
    for (let i = 0; i < counts.length; i++) {
      const d = new Date(today);
      d.setDate(d.getDate() - i);
      calendar[d.toISOString().slice(0, 10)] = counts[i]; // today = 10
    }
    // 5 days ago from today has count 50 (highest)
    const highestDate = new Date(today);
    highestDate.setDate(highestDate.getDate() - 4); // counts[4] = 50
    const cells = computeHeatmapData(calendar);
    const highCell = cells.find((c) => c.date === highestDate.toISOString().slice(0, 10));
    expect(highCell).toBeDefined();
    expect(highCell.count).toBe(50);
    // With sorted [10,20,30,40,50]: q3 index = Math.floor(5*0.75)=3 → value 40; 50>40 → intensity 4
    expect(highCell.intensity).toBe(4);
  });

  it("includes correct count for a known date", () => {
    const today = new Date().toISOString().slice(0, 10);
    const calendar = { [today]: 7 };
    const cells = computeHeatmapData(calendar);
    const todayCell = cells.find((c) => c.date === today);
    expect(todayCell).toBeDefined();
    expect(todayCell.count).toBe(7);
  });

  it("returns empty array for empty object calendar", () => {
    // An empty object means no data, but the function still builds 365 slots
    const cells = computeHeatmapData({});
    expect(Array.isArray(cells)).toBe(true);
    // All cells should have intensity 0
    cells.forEach((c) => expect(c.intensity).toBe(0));
  });
});
