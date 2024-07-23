export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  const filteredValues = [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length));

  return filteredValues.join('-');
}
