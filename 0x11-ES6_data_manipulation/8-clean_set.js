export default function cleanSet(set, startString) {
  if (!startString || !(typeof startString === 'string')) {
    return '';
  }

  const cleanSet = [];

  set.forEach((word) => {
    if (word && typeof word === 'string' && word.startsWith(startString)) {
      cleanSet.push(word.replace(startString, ''));
    }
  });
  return cleanSet.join('-');
}
