export function getPercentages(a, b) {
  const total = a + b;
  if (total === 0) return { a: 50, b: 50 };
  return {
    a: Math.round((a / total) * 100),
    b: Math.round((b / total) * 100),
  };
}
