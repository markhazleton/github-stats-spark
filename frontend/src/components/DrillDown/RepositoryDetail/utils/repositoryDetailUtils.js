const dependencyStatusPriority = {
  major_outdated: 0,
  minor_outdated: 1,
  unknown: 2,
  current: 3,
};

export function getScreenshotUrl(screenshotPath) {
  if (!screenshotPath) return null;
  const basePath = import.meta.env.BASE_URL || "/";
  const normalizedPath = screenshotPath.replace(/\\/g, "/");
  return `${basePath}${normalizedPath}`;
}

export function formatDate(dateString) {
  if (!dateString) return "N/A";
  try {
    const date = new Date(dateString);
    if (isNaN(date.getTime())) return "N/A";
    return date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    });
  } catch {
    return "N/A";
  }
}

export function formatRelativeDate(days) {
  if (days == null) return "N/A";
  if (days === 0) return "Today";
  if (days === 1) return "Yesterday";
  if (days < 30) return `${days} days ago`;
  if (days < 365) return `${Math.floor(days / 30)} months ago`;
  return `${Math.floor(days / 365)} years ago`;
}

export function formatNumber(num) {
  if (num == null || isNaN(num)) return "N/A";
  return num.toLocaleString();
}

export function formatSize(size) {
  if (size == null || isNaN(size)) return "N/A";
  return parseFloat(size).toFixed(1);
}

export function calculateLanguagePercentage(languageStats, bytes) {
  if (!languageStats) return 0;
  const total = Object.values(languageStats).reduce(
    (sum, value) => sum + value,
    0,
  );
  return total > 0 ? ((bytes / total) * 100).toFixed(1) : 0;
}

export function formatReason(reason) {
  if (!reason || reason === "none") return null;
  return reason.replace(/_/g, " ");
}

export function getAvailabilityBadgeClass(styles, availability) {
  if (availability === "available") return styles.badgeSuccess;
  if (availability === "partial") return styles.badgeWarning;
  return styles.badgeError;
}

export function getSecurityStateBadgeClass(styles, overallState) {
  if (overallState === "clear") return styles.badgeSuccess;
  if (overallState === "alerts_detected") return styles.badgeError;
  return styles.badgeInfo;
}

export function getDependencyBadgeClass(styles, status) {
  if (status === "major_outdated") return styles.badgeError;
  if (status === "minor_outdated") return styles.badgeWarning;
  if (status === "current") return styles.badgeSuccess;
  return styles.badgeInfo;
}

export function getTopDependencies(repository) {
  return [...(repository.tech_stack?.dependencies || [])]
    .sort((a, b) => {
      const aPriority = dependencyStatusPriority[a.status] ?? 99;
      const bPriority = dependencyStatusPriority[b.status] ?? 99;
      if (aPriority !== bPriority) {
        return aPriority - bPriority;
      }
      return a.name.localeCompare(b.name);
    })
    .slice(0, 8);
}
