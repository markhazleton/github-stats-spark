/**
 * T037 – Vitest coverage for activity timeline data derivation.
 * Tests computeTimelineData from metricsCalculator.js.
 */
import { describe, it, expect } from "vitest";
import { computeTimelineData } from "../src/services/metricsCalculator";

const SAMPLE_WEEKLY = [
  { week: "2025-W01", label: "Jan 6", commits: 12, active_repos: 3 },
  { week: "2025-W02", label: "Jan 13", commits: 8, active_repos: 2 },
  { week: "2025-W03", label: "Jan 20", commits: 20, active_repos: 5 },
];

describe("computeTimelineData", () => {
  it("returns empty labels and datasets for null input", () => {
    const result = computeTimelineData(null);
    expect(result.labels).toEqual([]);
    expect(result.datasets).toEqual([]);
  });

  it("returns empty result for empty array input", () => {
    const result = computeTimelineData([]);
    expect(result.labels).toEqual([]);
    expect(result.datasets).toEqual([]);
  });

  it("returns correct number of labels from weekly data", () => {
    const result = computeTimelineData(SAMPLE_WEEKLY);
    expect(result.labels).toHaveLength(3);
    expect(result.labels[0]).toBe("Jan 6");
  });

  it("returns two datasets (commits and active_repos)", () => {
    const result = computeTimelineData(SAMPLE_WEEKLY);
    expect(result.datasets).toHaveLength(2);
    expect(result.datasets[0].label).toBe("Commits");
    expect(result.datasets[1].label).toBe("Active Repos");
  });

  it("commits dataset contains correct values", () => {
    const result = computeTimelineData(SAMPLE_WEEKLY);
    expect(result.datasets[0].data).toEqual([12, 8, 20]);
  });

  it("active_repos dataset contains correct values", () => {
    const result = computeTimelineData(SAMPLE_WEEKLY);
    expect(result.datasets[1].data).toEqual([3, 2, 5]);
  });

  it("handles missing commits/active_repos with 0 fallback", () => {
    const partial = [{ week: "2025-W04", label: "Jan 27" }];
    const result = computeTimelineData(partial);
    expect(result.datasets[0].data[0]).toBe(0);
    expect(result.datasets[1].data[0]).toBe(0);
  });

  it("assigns separate y-axis IDs for each series", () => {
    const result = computeTimelineData(SAMPLE_WEEKLY);
    expect(result.datasets[0].yAxisID).toBe("yCommits");
    expect(result.datasets[1].yAxisID).toBe("yRepos");
  });
});
